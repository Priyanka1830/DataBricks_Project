

with source_orders as (
    select * from `globalmart`.`bronze_dev`.`stg_orders`
)

select
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp_ist,
    _ingested_at
from source_orders


  where _ingested_at >= (select max(_ingested_at) - interval 3 days from `globalmart`.`bronze_dev`.`fct_orders_incremental`)
