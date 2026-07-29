with raw_orders as (
    select * from {{ source('bronze', 'bronze_orders') }}
),
deduped as (
    select *,
        row_number() over (
            partition by order_id 
            order by _ingested_at desc, order_purchase_timestamp desc
        ) as rn
    from raw_orders
    where order_id is not null
)
select
    order_id,
    customer_id,
    order_status,
    {{ convert_tz('order_purchase_timestamp') }} as order_purchase_timestamp_ist,
    _ingested_at
from deduped
where rn = 1