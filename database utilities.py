# Databricks notebook source
# MAGIC %fs
# MAGIC ls

# COMMAND ----------

dbutils fs.ls('/')

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

for folder_name in dbutils.fs.ls('/'):
    print(folder_name)

# COMMAND ----------

dbutils.notebook.help()

# COMMAND ----------


