with orders as (
    select * from {{ ref('stg_orders') }}
)
select
    customer_id,
    count(distinct order_id) as total_orders_placed,
    min(order_purchase_timestamp_ist) as first_order_timestamp,
    max(order_purchase_timestamp_ist) as most_recent_order_timestamp
from orders
group by 1