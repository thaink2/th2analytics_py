import requests
import pandas as pd
import numpy as np

def th2forecast_api(api_token = "", input_data = None):
    # API request preparation
    base_url = "https://apis-dev.thaink2.fr/"
    # base_url = "http://127.0.0.1:3838/"
    end_point = "thaink2/forecasting"
    req_url = f"{base_url}{end_point}"
    req_body = {
        "actuals": input_data.to_json(orient="records", date_format = "iso"),
        "fcast_horizon": 30,
    #   "group_target": group_target,
        "target_var": "value",
        "date_var": "date",
        "models_list": ["xgboost"]
    }

    # Make the API request
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(req_url, json=req_body, headers=headers)
    # Process the response
    return response