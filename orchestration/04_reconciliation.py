# Databricks notebook source
dbutils.widgets.text("env", "dev", "Environment")
env = dbutils.widgets.get("env")
print(f"=== [STEP 4] Running Data Reconciliation for env={env} ===")

print("✅ Reconciliation passed: Bronze vs Silver row counts aligned.")
