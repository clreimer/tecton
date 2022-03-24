from tecton import batch_feature_view, Input, BackfillConfig
from fraud.entities import user
from fraud.data_sources.users import users
from datetime import datetime


@batch_feature_view(
    source=users,
    entities=[user],
    mode='snowflake_sql',
    online=False,
    offline=False,
    batch_schedule='1d',
    ttl='3650days',
    feature_start_time=datetime(2017,1, 1),
    timestamp_key="SIGNUP_DATE",
    description='User date of birth, entered at signup.',
)
def user_date_of_birth(users):
    return f'''
        SELECT
            USER_ID,
            TO_CHAR(DOB) as DATE_OF_BIRTH,
            SIGNUP_DATE
        FROM
            {users}
        '''
