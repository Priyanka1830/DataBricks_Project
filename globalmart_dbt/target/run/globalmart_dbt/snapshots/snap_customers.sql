
      
  
    
        create or replace table `globalmart`.`bronze_dev`.`snap_customers`
      
      
    using delta
  
      
      
      
      
      
      
      
      
      as
      select *,
        md5(coalesce(cast(customer_id as string ), '')
         || '|' || coalesce(cast(
    current_timestamp()
 as string ), '')
        ) as dbt_scd_id,
        
    current_timestamp()
 as dbt_updated_at,
        
    current_timestamp()
 as dbt_valid_from,
        
  
  coalesce(nullif(
    current_timestamp()
, 
    current_timestamp()
), null)
  as dbt_valid_to

    from (
        select * from `globalmart`.`bronze_dev`.`stg_customers`
    ) sbq


  
  