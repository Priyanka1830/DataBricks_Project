with raw_customers as (
    select * from {{ source('bronze', 'bronze_orders') }}
),
deduped as (
    select *,
        row_number() over (
            partition by customer_id 
            order by _ingested_at desc
        ) as rn
    from raw_customers
    where customer_id is not null
)
select
    customer_id,
    order_priority,
    _ingested_at
from deduped
where rn = 1