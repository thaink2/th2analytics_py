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

d,ldz,l,zdz


```python
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

```