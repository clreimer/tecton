from tecton import BatchDataSource, SnowflakeDSConfig
from datetime import datetime


transactions = BatchDataSource(
    name="transactions",
    batch_ds_config=SnowflakeDSConfig(
      database="TECTON_DEMO_DATA",
      schema="DAVID_DBT",
      table="NEW_TRANSACTIONS",
      timestamp_key="TIMESTAMP",
    ),
)
