
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  select
    order_month,
    total_orders
from `globalmart`.`bronze_dev`.`fct_monthly_orders`
where total_orders <= 0
  
  
      
    ) dbt_internal_test