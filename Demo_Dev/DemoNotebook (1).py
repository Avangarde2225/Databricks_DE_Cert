# Databricks notebook source
print('Hello World')

# COMMAND ----------

# MAGIC %run ../Includes/Includes

# COMMAND ----------

print(name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------



# COMMAND ----------


