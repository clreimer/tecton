from tecton import FeatureService
from fraud.features.on_demand_feature_views.user_category_pct import user_category_pct
from fraud.features.batch_window_aggregate_feature_views.user_transaction_counts import user_transaction_counts
from fraud.features.batch_window_aggregate_feature_views.user_category_count import user_category_count

# fraud_detection_feature_service = FeatureService(
#     name='fraud_detection_feature_service',
#     features=[
#         last_transaction_amount_sql,
#         transaction_amount_is_high,
#         transaction_amount_is_higher_than_average,
#         user_transaction_amount_metrics,
#         user_transaction_counts,
#         user_distinct_merchant_transaction_count_30d
#     ]
# )


minimal_fs = FeatureService(
    name='minimal_fs',
    features=[
        user_category_pct,
        user_category_count,
        user_transaction_counts
    ]
)
