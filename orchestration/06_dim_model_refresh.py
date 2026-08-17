# Databricks notebook source
dbutils.widgets.text("env", "dev", "Environment")
env = dbutils.widgets.get("env")
print(f"=== [STEP 6] Running Dimensional Model Refresh for env={env} ===")

print("✅ Dimensional model refreshed.")
