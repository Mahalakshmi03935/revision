# Databricks notebook source
# MAGIC %md
# MAGIC TYPE 1 : COMBO BOX
# MAGIC - Combination of text and dropdown. Select a value from a provided list or input one in the text box
# MAGIC

# COMMAND ----------

dbutils.widgets.combobox(name = 'Godscb',defaultValue='Krishna',choices = [ 'Krishna','Shiva','Parvati','Ganapathi','Ayyappa','Muruga'],label='Gods Combo Box')

# COMMAND ----------

# MAGIC %md
# MAGIC TYPE 2 : DROP DOWN
# MAGIC -provide a list of options, and users can select one or more items from the list. They are useful for offering predefined choices for data filtering or analysis.

# COMMAND ----------

dbutils.widgets.dropdown(name = "Godsdd",defaultValue = "Krishna",choices = ["Krishna","Shiva","Parvati","Ganapathi","Ayyappa","Muruga"],label="Gods Drop Down")

# COMMAND ----------

# MAGIC %md
# MAGIC TYPE 3 : MULTI SELECT
# MAGIC -are similar to dropdowns, but they allow users to select multiple items from a list. This is particularly useful for filtering data with multiple criteria.

# COMMAND ----------

dbutils.widgets.multiselect(name = "GodsMS",defaultValue="Shiva",choices = ["Krishna","Shiva","Parvati","Ganapati","Ayyappa","Muruga"],label = "Gods ms")

# COMMAND ----------

# MAGIC %md
# MAGIC TYPE 4 : TEXT
# MAGIC -allow you to enter text or numeric values that can be used as parameters in your code. These are ideal for accepting user inputs.

# COMMAND ----------

dbutils.widgets.text(name = "godstxt",defaultValue="Ganapathi",label = "Gods txt")

# COMMAND ----------

# MAGIC %md
# MAGIC TYPE 5 : GET
# MAGIC

# COMMAND ----------

dbutils.widgets.get('godstxt')

# COMMAND ----------

dbutils.widgets.get("GodsMS")

# COMMAND ----------

# MAGIC %md
# MAGIC TYPE 6 : REMOVE

# COMMAND ----------

dbutils.widgets.remove("Godsdd")
