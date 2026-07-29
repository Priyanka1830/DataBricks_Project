-- back compat for old kwarg name
  
  
  
  
  
  
      
          
          
      
  

    merge
    into
        `globalmart`.`bronze_dev`.`fct_orders_incremental` as DBT_INTERNAL_DEST
    using
        `fct_orders_incremental__dbt_tmp` as DBT_INTERNAL_SOURCE
    on
        
              DBT_INTERNAL_SOURCE.`order_id` <=> DBT_INTERNAL_DEST.`order_id`
          
    when matched
        then update set
            *
    when not matched
        then insert
            *
