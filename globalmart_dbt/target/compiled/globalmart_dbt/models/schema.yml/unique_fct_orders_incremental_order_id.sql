
    
    

select
    order_id as unique_field,
    count(*) as n_records

from `globalmart`.`bronze_dev`.`fct_orders_incremental`
where order_id is not null
group by order_id
having count(*) > 1


