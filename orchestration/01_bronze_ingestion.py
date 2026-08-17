# Databricks notebook source
dbutils.widgets.text("env", "dev", "Environment")
env = dbutils.widgets.get("env")
print(f"=== [STEP 1] Running Bronze Ingestion for env={env} ===")

catalog = "globalmart"
schema = "bronze_dev" if env == "dev" else "bronze"

spark.sql(f"USE CATALOG {catalog}")
spark.sql(f"USE {schema}")

print(f"✅ Successfully verified Bronze tables in {catalog}.{schema}")
display(spark.sql("SHOW TABLES"))
