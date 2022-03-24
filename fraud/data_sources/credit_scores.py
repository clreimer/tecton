from tecton import BatchDataSource, SnowflakeDSConfig
from datetime import datetime


credit_scores = BatchDataSource(
    name="credit_scores",
    batch_ds_config=SnowflakeDSConfig(
      database="TECTON_DEMO_DATA",
      schema="FRAUD",
      table="CREDIT_SCORES",
      timestamp_key="TIMESTAMP",
    ),
)
