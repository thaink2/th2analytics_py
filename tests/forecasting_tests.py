import unittest
import requests
import pandas as pd
import numpy as np
from th2analytics.forecasting import ForecastingAPI

class TestForecastingAPI(unittest.TestCase):
    def setUp(self):
        self.api = ForecastingAPI(base_url="https://apis-dev.thaink2.fr/", api_token="test_token")

    def test_generate_forecast(self):
        # Mock inputs and assert behavior
        actuals = [100, 200, 300]
        fcast_horizon = 10
    #    group_target = "Region"
        target_var = "value"
        date_var = "date"
        models_list = ["xgboost"]
        api_token = "*******************" # get your token here: https:\\opensource.thaink2.com\app\th2token
        # Generate random time-series data
        np.random.seed(42)
        dates = pd.date_range(start='2022-01-01', periods=100, freq='D')
        values = np.random.randn(100).cumsum()
        # Create a DataFrame from the generated data
        input_data = pd.DataFrame({'date': dates, 'value': values})

        from th2analytics.forecasting import ForecastingAPI

        ForecastingAPI(api_token = api_token, input_data = input_data)
        # Simulate a response or mock API call for testing
        # (You can use `unittest.mock` to mock the requests library)

        self.assertTrue(True)  # Replace with actual test logic
