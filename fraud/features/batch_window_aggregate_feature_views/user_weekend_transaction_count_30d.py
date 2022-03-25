from tecton import batch_feature_view, FeatureAggregation, Input, transformation, const
from fraud.entities import user
from fraud.data_sources.transactions import transactions
from datetime import datetime

@transformation(mode="snowflake_sql")
def is_weekend(input_view, timestamp_col):
    return f"""
        SELECT
            USER_ID,
            DAYNAME({timestamp_col}) = 'Sat' OR DAYNAME({timestamp_col}) = 'Sun' as IS_WEEKEND,
            TIMESTAMP
        FROM
            {input_view}
    """

@transformation(mode="snowflake_sql")
def select_weekend_cols(input_view):
    return f"""
        SELECT
            USER_ID,
            IS_WEEKEND,
            TIMESTAMP
        FROM
            {input_view}
    """

@batch_feature_view(
    source=transactions,
    entities=[user],
    mode='pipeline',
    aggregation_slide_period='1d',
    aggregations=[FeatureAggregation(column='IS_WEEKEND', function='sum', time_windows=['30d'])],
    online=False,
    offline=False,
    feature_start_time=datetime(2021, 4, 1),
    tags={'cost-center': 'finance'},
    description='How many weekend transactions the user has made in the last 30 days.'
)
def user_weekend_transaction_count_30d(transactions):
    augmented = is_weekend(transactions, const('TIMESTAMP'))
    return select_weekend_cols(augmented)
