import requests
import pandas as pd
import numpy as np

import th2apis

api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MzQ1MzkxMjEsInVzZXJfbWFpbCI6ImZhcmlkLmF6b3Vhb3VAdGhhaW5rMi5jb20iLCJ0YXJnZXRfc2VydmljZSI6ImZvcmVjYXN0aW5nIiwiYWRkaXRpb25faW5mbyI6InRlc3QifQ.SlzjcfMEvP4zu4MpY6p_d3nZVaYhIihQEor-yCu6A9M" # get your token here: https:\\opensource.thaink2.com\app\th2token
# Generate random time-series data
np.random.seed(42)
dates = pd.date_range(start='2022-01-01', periods=100, freq='D')
values = np.random.randn(100).cumsum()
# Create a DataFrame from the generated data
input_data = pd.DataFrame({'date': dates, 'value': values})

th2apis.th2forecast_api(api_token = api_token, input_data = input_data)