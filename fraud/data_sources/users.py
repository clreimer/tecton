from tecton import BatchDataSource, SnowflakeDSConfig
from datetime import datetime


users = BatchDataSource(
    name="users",
    batch_ds_config=SnowflakeDSConfig(
      database="TECTON_DEMO_DATA",
      schema="DAVID_DBT",
      table="NEW_USERS",
      timestamp_key="SIGNUP_TIMESTAMP",
    ),
)
