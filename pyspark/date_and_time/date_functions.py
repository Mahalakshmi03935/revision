# Databricks notebook source
from pyspark.sql.functions import datediff, months_between, date_add, date_sub, add_months
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DateFunctionsExample").getOrCreate()

data = [('2024-01-26', '2024-06-26')]

df = spark.createDataFrame(data, ['d1', 'd2'])

df = df.withColumn('datediff', datediff(df.d2, df.d1)) \
       .withColumn('monthsbetween', months_between(df.d2, df.d1)) \
       .withColumn('addmonths', add_months(df.d2, 3)) \
       .withColumn('submonths', add_months(df.d2, -3)) \
       .withColumn('daysadd', date_add(df.d2, 3)) \
       .withColumn('subdays', date_sub(df.d2, 3))

df.show()

