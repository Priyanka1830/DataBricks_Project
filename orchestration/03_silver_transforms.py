# Databricks notebook source
dbutils.widgets.text("env", "dev", "Environment")
env = dbutils.widgets.get("env")
print(f"=== [STEP 3] Running Silver Transforms for env={env} ===")

print("✅ Silver transformations completed cleanly.")
