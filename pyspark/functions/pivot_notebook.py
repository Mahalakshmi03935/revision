# Databricks notebook source
data = [(1, 'maha', 'female', 'IT'),\
(2, 'viswa', 'male', 'IT'), \
(3, 'swetha', 'female', 'HR'), \
(4, 'sesha', 'male', 'IT'),\
(5, 'darshini', 'female', 'IT'),\
(6, 'bhuvanesh', 'male', 'HR'), \
(7, 'hemanth', 'male', 'HR'),\
(8, 'adhithya', 'male', 'IT')\
]
schema = ['id', 'name', 'gender', 'dep']
df = spark.createDataFrame (data, schema)
df.show()
df.groupBy('dep','gender').count().show()
df.groupBy('dep').pivot('gender').count().show()
df.groupBy('dep').pivot('gender',['female']).count().show()

