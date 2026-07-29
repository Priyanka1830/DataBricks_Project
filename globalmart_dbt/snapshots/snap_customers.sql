{% snapshot snap_customers %}

{{
    config(
      target_catalog='globalmart',
      target_schema='bronze_dev',
      unique_key='customer_id',
      strategy='check',
      check_cols='all'
    )
}}

select * from {{ ref('stg_customers') }}

{% endsnapshot %}