{{
    config(
        materialized='incremental',
        unique_key='order_id',
        incremental_strategy='merge'
    )
}}

with source_orders as (
    select * from {{ ref('stg_orders') }}
)

select
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp_ist,
    _ingested_at
from source_orders

{% if is_incremental() %}
  where _ingested_at >= (select max(_ingested_at) - interval 3 days from {{ this }})
{% endif %}