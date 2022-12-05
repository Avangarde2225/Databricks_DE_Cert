# Databricks notebook source
files = dbutils.fs.ls("dbfs:/mnt/demo/dlt/demo_pipeline")
display(files)

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/mnt/demo/dlt/demo_pipeline/system/events")
display(files)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM delta.`dbfs:/mnt/demo/dlt/demo_pipeline/system/events`

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/mnt/demo/dlt/demo_pipeline/tables")
display(files)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo_pipeline_dlt_db.cn_daily_customer_books

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo_pipeline_dlt_db.fr_daily_customer_books
