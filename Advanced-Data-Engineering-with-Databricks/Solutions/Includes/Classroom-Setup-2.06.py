# Databricks notebook source
# MAGIC %run ./_databricks-academy-helper $lesson="2.06"

# COMMAND ----------

# MAGIC %run ./_utility-functions

# COMMAND ----------

DA.cleanup()
DA.init()

# COMMAND ----------

# Create the user datasets
create_date_lookup()              # Create static copy of date_lookup
print()

init_source_daily()               # Create the data factory
DA.daily_stream.load_through(2)   # Load one new day for DA.paths.source_daily
DA.process_bronze()               # Process through the bronze table
DA.process_heart_rate_silver_v0() # Process the heart_rate_silver table

# COMMAND ----------

DA.conclude_setup()
