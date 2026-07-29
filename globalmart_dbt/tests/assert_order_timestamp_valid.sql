-- Custom singular test: Ensure order timestamps are not greater than ingestion timestamp
select
    order_id,
    order_purchase_timestamp_ist,
    _ingested_at
from {{ ref('stg_orders') }}
where order_purchase_timestamp_ist > _ingested_at