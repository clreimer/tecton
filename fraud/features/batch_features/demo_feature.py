from tecton import batch_feature_view, FilteredSource
from fraud.entities import user
from fraud.data_sources.credit_scores_batch import credit_scores_batch
from datetime import datetime, timedelta

@batch_feature_view(
    sources=[FilteredSource(credit_scores_batch)],
    entities=[user],
    mode='spark_sql',
    online=False,
    offline=False,
    feature_start_time=datetime(2020, 10, 10),
    batch_schedule=timedelta(days=1),
    ttl=timedelta(days=30),
    description='Whether the user has a good credit score (over 670).'
)
def user_has_good_credit(credit_scores):
    return f'''
        SELECT
            user_id,
            IF (credit_score > 670, 1, 0) as user_has_good_credit,
            date as timestamp
        FROM
            {credit_scores}
        '''