from tecton import BatchDataSource, SnowflakeDSConfig
from datetime import datetime


users = BatchDataSource(
    name="users",
    batch_ds_config=SnowflakeDSConfig(
      database="TECTON_DEMO_DATA",
      schema="FRAUD",
      table="USERS",
      timestamp_key="SIGNUP_DATE",
    ),
)
