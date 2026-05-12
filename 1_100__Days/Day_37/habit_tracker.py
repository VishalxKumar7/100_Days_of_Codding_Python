import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = "vishalvanday"
TOKEN = "dhw85nct58en982y476n92"
GRAPH_ID = "studytime1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameter)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Time",
    "unit": "hours",
    "type": "float",
    "color": "sora",
    "timezone": "Asia/Kolkata",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ***********************************************************************************************

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
yesterday = today - timedelta(days=1)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How may hours have you studied today: ")
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# ****************************************************************************************

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "7"
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)