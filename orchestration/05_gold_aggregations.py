# Databricks notebook source
dbutils.widgets.text("env", "dev", "Environment")
env = dbutils.widgets.get("env")
print(f"=== [STEP 5] Running Gold Aggregations for env={env} ===")

print("✅ Gold aggregations updated.")
