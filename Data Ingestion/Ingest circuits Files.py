# Databricks notebook source
# MAGIC %run ../setup/mount_adls

# COMMAND ----------

# MAGIC %md ###Ingest circuits.CSV File

# COMMAND ----------

# MAGIC %md #### step 1: Reading circuits.csv file into dataframe

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/formula1adls2sa/raw

# COMMAND ----------

df = spark.read.csv("dbfs:/mnt/formula1adls2sa/raw/circuits.csv",inferSchema=True,header=True)

# COMMAND ----------

display(df)

# COMMAND ----------


