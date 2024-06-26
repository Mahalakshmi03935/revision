# Databricks notebook source
dbutils.widgets.text('color',"")

# COMMAND ----------

val=dbutils.widgets.get('color')

# COMMAND ----------

print(val)

# COMMAND ----------


