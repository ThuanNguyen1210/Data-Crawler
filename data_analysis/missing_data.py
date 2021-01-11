import pandas as pd
import numpy as np
import re
header_list = ["job_title", "company", "salary", "location", "position", "job_description", "job_requirement", "benefit", "quantity"]
df = pd.read_excel('data.xlsx', engine='openpyxl')
df_check = df.isna()
df1 = df[df.isna().any(axis=1)]
print(df1)