from tecton.compat import batch_feature_view, Input, BackfillConfig
from fraud.entities import user
from fraud.data_sources.credit_scores_batch import credit_scores_batch
from datetime import datetime


@batch_feature_view(
    inputs={'credit_scores': Input(credit_scores_batch)},
    entities=[user],
    mode='pyspark',
    online=False,
    offline=False,
    feature_start_time=datetime(2021, 1, 1),
    batch_schedule='1d',
    ttl='120d',
    backfill_config=BackfillConfig("multiple_batch_schedule_intervals_per_job"),
    family='fraud',
    tags={'release': 'production'},
    owner='matt@tecton.ai',
    description='Whether the user has a good credit score (over 670).'
)
def user_has_good_credit_pyspark(credit_scores):
    from pyspark.sql.functions import when, col
    return credit_scores.withColumn('user_has_good_credit', when(col('credit_score') > 670, 1).otherwise(0)) \
                        .select('user_id', 'user_has_good_credit', 'timestamp')
