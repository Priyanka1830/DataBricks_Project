with orders as (
    select * from `globalmart`.`bronze_dev`.`stg_orders`
)
select
    date_trunc('month', order_purchase_timestamp_ist) as order_month,
    count(distinct order_id) as total_orders
from orders
group by 1