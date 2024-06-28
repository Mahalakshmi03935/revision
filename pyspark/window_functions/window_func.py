# Databricks notebook source
from pyspark.sql.functions import rank,dense_rank,row_number
from pyspark.sql.window import Window


# COMMAND ----------

employee_data = [('maha', 'HR', 2000), ('swetha', 'IT', 3000), ('ramnesh', 'HR',1500), ('sesha', 'payroll', 3500),
('viswa', 'IT',3000), ('leela', 'IT',4000),\
('tharani', 'payroll', 2000), ('divya', 'IT', 2000), ('hemanth', 'HR', 2000), ('krishna', 'IT', 2500)]
employee_schema = ["emp_name","department","salary"]
df = spark.createDataFrame(employee_data,employee_schema)
df.show()

# COMMAND ----------

df.sort('department').show()
window = Window.partitionBy('department').orderBy('salary')
df.withColumn ('rowNumber', row_number().over (window)).\
withColumn('rank', rank().over (window)).\
withColumn ('denserank', dense_rank().over (window)).show()
