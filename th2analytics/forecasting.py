import requests

class ForecastingAPI:
    def __init__(self, base_url, api_token):
        """
        Initialize the API wrapper with a base URL and API token.
        """
        self.base_url = base_url
        self.api_token = api_token

    def th2forecast_api(self, actuals, fcast_horizon, group_target, target_var, date_var, models_list):
        """
        Generate a forecast by sending a request to the API.
        """
        endpoint = "thaink2/forecasting"
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "actuals": actuals.to_json(orient="records", date_format = "iso"),
            "fcast_horizon": fcast_horizon,
            "group_target": group_target,
            "target_var": target_var,
            "date_var": date_var,
            "models_list": models_list
        }

        # Make the API call
        response = requests.post(url, json=payload, headers=headers)

        # Handle response
        if response.status_code == 200:
            return response.json()  # Return the parsed JSON response
        else:
            response.raise_for_status()  # Raise an exception for HTTP errors



def th2forecast_api(api_token = "", input_data = None):
    # API request preparation
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