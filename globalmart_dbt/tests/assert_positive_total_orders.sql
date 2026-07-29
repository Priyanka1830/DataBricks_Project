select
    order_month,
    total_orders
from {{ ref('fct_monthly_orders') }}
where total_orders <= 0