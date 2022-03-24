from tecton import BatchDataSource, SnowflakeDSConfig
from datetime import datetime


transactions = BatchDataSource(
    name="transactions",
    batch_ds_config=SnowflakeDSConfig(
      database="TECTON_DEMO_DATA",
      schema="FRAUD",
      table="TRANSACTIONS",
      timestamp_key="TIMESTAMP",
    ),
)
