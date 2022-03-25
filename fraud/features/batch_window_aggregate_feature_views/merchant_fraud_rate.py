from tecton import batch_feature_view, Input, FeatureAggregation
from fraud.entities import user, merchant
from fraud.data_sources.transactions import transactions
from datetime import datetime


@batch_feature_view(
    source=transactions,
    entities=[merchant],
    mode='snowflake_sql',
    aggregation_slide_period='1d',
    aggregations=[FeatureAggregation(column='IS_FRAUD', function='mean', time_windows=['24h','72h','168h', '960h'])],
    online=True,
    offline=True,
    feature_start_time=datetime(2020, 10, 10),
    owner='david@tecton.ai',
    description='Merchant fraud rate over various time windows, updated daily.'
)
def merchant_fraud_rate(transactions):
    return f'''
        SELECT
            MERCHANT,
            IS_FRAUD,
            TIMESTAMP
        FROM
            {transactions}
        '''
