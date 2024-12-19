from th2analytics.forecasting import ForecastingAPI
import argparse
import json

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Interact with the Forecasting API")
    parser.add_argument("--base_url", required=True, help="Base URL of the API")
    parser.add_argument("--api_token", required=True, help="API token for authentication")
    parser.add_argument("--actuals", required=True, help="JSON string of actual data")
    parser.add_argument("--fcast_horizon", type=int, required=True, help="Forecast horizon")
    parser.add_argument("--group_target", required=True, help="Grouping target")
    parser.add_argument("--target_var", required=True, help="Target variable")
    parser.add_argument("--date_var", required=True, help="Date variable")
    parser.add_argument("--models_list", required=True, help="JSON string of model names")

    args = parser.parse_args()

    # Convert JSON strings to Python objects
    try:
        actuals = json.loads(args.actuals)
        models_list = json.loads(args.models_list)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON inputs: {e}")
        return

    # Initialize the API wrapper
    api = ForecastingAPI(base_url=args.base_url, api_token=args.api_token)

    # Make the API call
    try:
        forecast = api.generate_forecast(
            actuals=actuals,
            fcast_horizon=args.fcast_horizon,
            group_target=args.group_target,
            target_var=args.target_var,
            date_var=args.date_var,
            models_list=models_list
        )
        print("Forecast result:")
        print(json.dumps(forecast, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
