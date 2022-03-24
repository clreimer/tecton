# from tecton import FeatureService
# from fraud.features.stream_window_aggregate_feature_views.user_transaction_amount_metrics import user_transaction_amount_metrics
# from fraud.features.batch_window_aggregate_feature_views.user_transaction_counts import user_transaction_counts
# from fraud.features.stream_feature_views.last_transaction_amount_sql import last_transaction_amount_sql
# from fraud.features.on_demand_feature_views.transaction_amount_is_high import transaction_amount_is_high
# from fraud.features.on_demand_feature_views.transaction_amount_is_higher_than_average import transaction_amount_is_higher_than_average
# from fraud.features.batch_feature_views.user_distinct_merchant_transaction_count_30d import user_distinct_merchant_transaction_count_30d
# from fraud.features.stream_window_aggregate_feature_views.last_transactions import user_recent_transactions
# # from fraud.features.batch_feature_views.user_has_great_credit import user_has_great_credit
#
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
#
#
# minimal_fs = FeatureService(
#     name='minimal_fs',
#     features=[
#         transaction_amount_is_higher_than_average
#     ]
# )
