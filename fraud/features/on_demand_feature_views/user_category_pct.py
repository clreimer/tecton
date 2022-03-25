from tecton import RequestDataSource, on_demand_feature_view, Input
from pyspark.sql.types import BooleanType, DoubleType, StructType, StructField
from fraud.features.batch_window_aggregate_feature_views.user_transaction_counts import user_transaction_counts
from fraud.features.batch_window_aggregate_feature_views.user_category_count import user_category_count

# Schema of the output feature value(s)
output_schema = StructType([
    StructField('user_category_pct', DoubleType())
])

# This On-Demand Feature View compares request data ('amount')
# to a feature ('amount_mean_24h') from a pre-computed Feature View ('user_transaction_amount_metrics').
@on_demand_feature_view(
    inputs={
        'user_transaction_counts': Input(user_transaction_counts),
        'user_category_count': Input(user_category_count)
    },
    mode='python',
    output_schema=output_schema,
    family='fraud',
    owner='matt@tecton.ai',
    tags={'release': 'production'},
    description='Percent of a users transcations that have been in this category, in the last 40 days'
)
def user_category_pct(user_transaction_counts, user_category_count):
    transaction_count_40d = user_transaction_counts['TRANSACTION_COUNT_960H_1D']
    category_count_40d = user_category_count['TRANSACTION_COUNT_960H_1D']
    if transaction_count_40d is None or transaction_count_40d == 0:
        return {'user_category_pct': 0}
    return {'user_category_pct': float(category_count_40d) / float(transaction_count_40d)}
