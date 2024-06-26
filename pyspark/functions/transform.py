# Databricks notebook source
from pyspark.sql.functions import transform, upper
data = [(1, 'maheer', ['azure', 'dotnet']), (2, 'wafa', ['aws', 'java'])] 
schema= ['id', 'name', 'skills']
df = spark.createDataFrame (data, schema)
df.show()
df.printSchema ()

df.select('id', 'name', transform('skills', lambda x: upper(x)).alias('skills')).show()
