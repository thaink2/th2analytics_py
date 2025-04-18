# **th2analytics**

[![PyPI version](https://badge.fury.io/py/th2analytics.svg)](https://pypi.org/project/th2analytics/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python Versions](https://img.shields.io/pypi/pyversions/th2analytics.svg)](https://pypi.org/project/th2analytics/)

**th2analytics** is a Python library that provides a simple and efficient wrapper for interacting with the [thaink2](https://thaink2.com/) analytics APIs. It enables users to generate future forecasts rapidly while adapting to various types of data.

---

## **Features**
- Generate forecasts quickly using an intuitive interface.
- Supports multiple forecasting models like ARIMA, XGBOOST, Random, and others.
- Customizable parameters for forecast horizon, grouping, and target variables.
- Lightweight and easy to integrate into existing workflows.

---

## **Installation**

Install the package using pip:

```bash
pip install th2analytics
```

A bearer token is needed in order to perform the API request, use the following url to generate a valid token [thaink2 token generator](https://clever.thaink2.fr/app_direct/th2token/)

```python
from th2analytics.forecasting import ForecastingAPI
import numpy as np
import pandas as pd

api_token = "************" # get your token here: https://clever.thaink2.fr/app_direct/th2token/


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

forecast_df = pd.json_normalize(forecast)
print(forecast_df)

```