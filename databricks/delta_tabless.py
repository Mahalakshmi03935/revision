# Databricks notebook source
data1=spark.read.option("Header","true").csv("dbfs:/FileStore/Country_Q1.csv")

# COMMAND ----------

data = spark.read.csv("dbfs:/FileStore/Country_Q1.csv",header = True)

# COMMAND ----------

data.display()

# COMMAND ----------

data.write.csv("dbfs:/FileStore/brml/godss.csv",header = True)

# COMMAND ----------

data=data.withColumn('dummy',data['CountryCode']+'a')

# COMMAND ----------

data.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC update rockstar
# MAGIC set CountryCode='SW'
# MAGIC WHERE CountryCode='JA'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM ROCKSTAR

# COMMAND ----------

from delta.tables import DeltaTable


rockstar.history().select("version", "timestamp", "operation").show(truncate=False)

