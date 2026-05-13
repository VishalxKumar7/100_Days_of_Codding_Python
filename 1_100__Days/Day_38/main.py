import requests

ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
APP_ID = "app_f293bfdc4cfa482e8df5fbc1"
API_KEY = "nix_live_HOTaGqpfSqXKP7OCScw9YdG1CIHGIgJz"

headers = {
    "x-app-id": "APP_ID",
    "x-app-key": "API_KEY"
}

data = {
    "query": "Swam for 1 hour"
}

response = requests.post(url=ENDPOINT, json=data, headers=headers)
print(response)