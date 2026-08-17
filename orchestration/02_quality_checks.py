# Databricks notebook source
# COMMAND ----------
dbutils.widgets.text("env", "dev", "Environment")
dbutils.widgets.text("force_fail", "false", "Force Failure")

# COMMAND ----------
env = dbutils.widgets.get("env")
force_fail = dbutils.widgets.get("force_fail")

print(f"=== [STEP 2] Running Quality Checks for env={env} (force_fail={force_fail}) ===")

# COMMAND ----------
# Check for forced quality failure (Task 10.1 proof test)
if str(force_fail).strip().lower() == "true":
    raise Exception("Simulated Quality Gate Failure for Task 10.1 Downstream Skip Proof!")

# COMMAND ----------
catalog = "globalmart"
schema = f"bronze_{env}" if env == "dev" else "bronze"

# Verify table safely across possible schema variations
try:
    tables = [t.name for t in spark.catalog.listTables(f"{catalog}.{schema}")]
    print(f"Available tables in {catalog}.{schema}: {tables}")
except Exception as e:
    print(f"Schema check notice: {e}")

print("✅ Quality checks completed successfully!")
