from th2analytics.forecasting import ForecastingAPI
import numpy as np
import pandas as pd

api_token = "************" # get your token here: https:\\opensource.thaink2.com\app\th2token


# Initialize the API wrapper
api = ForecastingAPI(
    base_url = "https://apis-dev.thaink2.fr/",
    api_token = api_token
)

np.random.seed(42)
dates = pd.date_range(start='2022-01-01', periods=100, freq='D')
values = np.random.randn(100).cumsum()
# Create a DataFrame from the generated data
input_data = pd.DataFrame({'date': dates, 'value': values})
# Generate the forecast
forecast = api.th2forecast_api(
    actuals = input_data,
    fcast_horizon = 30,
    group_target = None,
    target_var = "value",
    date_var = "date",
    models_list = ["xgboost"]
)
# Print the forecast
print("Forecast Results:", forecast)
