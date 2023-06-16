# Databricks notebook source
import pandas as pd
import numpy as np
from datetime import datetime
import requests
import json

# COMMAND ----------

dbutils.widgets.text("a", "7")

# COMMAND ----------

a = dbutils.widgets.get("a")

# COMMAND ----------

if a == "7":
  api_response = requests.get('https://jsonplaceholder.typicode.com/todos')
  print(api_response.status_code)
  data = api_response.text
  parse_json = json.loads(data)

  pd.DataFrame(parse_json)
else:
  print("Not a Seven, skipping run ...")

# COMMAND ----------


