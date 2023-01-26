# Databricks notebook source
# MAGIC %run ../setup/mount_adls

# COMMAND ----------

# MAGIC %md ###Ingest circuits.CSV File

# COMMAND ----------

# MAGIC %md #### step 1: Reading circuits.csv file into dataframe

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

# MAGIC %fs ls /mnt/formula1adls2sa/raw

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1adls2sa/raw")

# COMMAND ----------


