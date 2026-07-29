{% macro convert_tz(column_name, target_tz='Asia/Kolkata') %}
    from_utc_timestamp({{ column_name }}, '{{ target_tz }}')
{% endmacro %}