
  
  
  
  create or replace view `globalmart`.`bronze_dev`.`stg_customers`
  
  as (
    with raw_customers as (
    select * from `globalmart`.`bronze`.`bronze_orders`
)
select distinct
    customer_id,
    order_priority,
    fulfillment_channel
from raw_customers
where customer_id is not null
  )
