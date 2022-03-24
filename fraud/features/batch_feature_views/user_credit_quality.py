from tecton import batch_feature_view, Input, BackfillConfig
from fraud.entities import user
from fraud.data_sources.credit_scores import credit_scores
from datetime import datetime

@batch_feature_view(
    source=credit_scores,
    entities=[user],
    mode='snowflake_sql',
    online=True,
    offline=True,
    feature_start_time=datetime(2021, 1, 1),
    batch_schedule='1d',
    ttl='3650d',
    description="Metrics describing the quality of a users credit score"
)
def user_credit_quality(credit_scores):
    return f'''
        SELECT
            USER_ID,
            IFF (CREDIT_SCORE > 670, 1, 0) as USER_HAS_GOOD_CREDIT,
            IFF (CREDIT_SCORE > 730, 1, 0) as USER_HAS_GREAT_CREDIT,
            TIMESTAMP
        FROM
            {credit_scores}
        '''
