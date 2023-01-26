# Databricks notebook source
storage_account_name = "formula1adls2sa"
client_id = dbutils.secrets.get(scope="formula1-scope",key="databricks-app-client-id")
tenenat_id = dbutils.secrets.get(scope="formula1-scope",key="databricks-app-tenant-id")
client_secret = dbutils.secrets.get(scope="formula1-scope",key="databricks-app-client-secret")

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": f"{client_id}",
          "fs.azure.account.oauth2.client.secret": f"{client_secret}",
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenenat_id}/oauth2/token"}


# COMMAND ----------

def mount_adls(container):
    container_name = container
    dbutils.fs.mount(
      source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
      mount_point = f"/mnt/{storage_account_name}/{container_name}",
      extra_configs = configs)

# COMMAND ----------

containers = ["raw","processed"]
for i in containers:
    try:
        mount_adls(i)
    except Exception as e:
        pass

# COMMAND ----------



# COMMAND ----------


