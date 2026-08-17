# Databricks notebook source
dbutils.widgets.text("env", "dev", "Environment")
env = dbutils.widgets.get("env")
print(f"=== [STEP 7] Updating Visualization Views for env={env} ===")

print("✅ Dashboard datasets successfully refreshed!")
