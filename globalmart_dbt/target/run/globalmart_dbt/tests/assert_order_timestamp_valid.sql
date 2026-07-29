
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  -- Custom singular test: Ensure order timestamps are not greater than ingestion timestamp
select
    order_id,
    order_purchase_timestamp_ist,
    _ingested_at
from `globalmart`.`bronze_dev`.`stg_orders`
where order_purchase_timestamp_ist > _ingested_at
  
  
      
    ) dbt_internal_test