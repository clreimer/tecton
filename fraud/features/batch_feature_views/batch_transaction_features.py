from tecton import batch_feature_view, Input, BackfillConfig
from fraud.entities import user
from fraud.data_sources.transactions import transactions
from datetime import datetime

@batch_feature_view(
    source=transactions,
    entities=[user],
    mode='snowflake_sql',
    online=False,
    offline=False,
    batch_schedule='1d',
    ttl='30days',
    feature_start_time=datetime(2021, 5, 20),
    description='Last user transaction amount (batch calculated)'
)
def last_transaction_amount(transactions):
    return f'''
        SELECT
            NAMEORIG as USER_ID,
            AMOUNT,
            TIMESTAMP
        FROM
            {transactions}
        '''
