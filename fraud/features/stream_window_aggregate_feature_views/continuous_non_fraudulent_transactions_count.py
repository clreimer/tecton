# from tecton import MonitoringConfig, FeatureAggregation, Input, stream_window_aggregate_feature_view
# from fraud.entities import user
# from fraud.data_sources.transactions_stream import transactions_stream
# from datetime import datetime
#
# # The following defines a continuous streaming feature
# # It counts the number of non-fraudulent transactions per user over a 1min, 5min and 1h time window
# # The expected freshness for these features is <1second
# @stream_window_aggregate_feature_view(
#     inputs={'transactions': Input(transactions_stream)},
#     entities=[user],
#     mode='spark_sql',
#     aggregation_slide_period='continuous',
#     aggregations=[
#         FeatureAggregation(column='counter', function='count', time_windows=['1min', '5min', '1h'])
#     ],
#     online=False,
#     offline=False,
#     feature_start_time=datetime(2021, 6, 1),
#     family='fraud',
#     tags={'release': 'production'},
#     owner='kevin@tecton.ai',
#     description='Number of non-fraudulent transactions'
# )
# def continuous_non_fraudulent_transactions_count(transactions):
#     return f'''
#         SELECT
#             nameorig as user_id,
#             1 as counter,
#             timestamp
#         FROM
#             {transactions}
#         WHERE isFraud = 0
#         '''
