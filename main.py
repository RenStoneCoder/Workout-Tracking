import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
AUTH_USER_NAME = os.getenv("AUTH_USER_NAME")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

GENDER = "Female"
WEIGHT_KM = "40.8"
HEIGHT_CM = "152.4"
AGE = "23"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KM,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url= exercise_endpoint, headers=headers, json=parameters)
result = response.json()
print(result)

today = datetime.now()
time_now = today.strftime("%X")
today_formatted = today.strftime("%d/%m/%Y")

for exercise in result["exercises"]:
    post_parameters = {
        "workout": {
            "date": today_formatted,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
    }
}


    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=post_parameters, auth=(AUTH_USER_NAME, AUTH_PASSWORD))
    print(sheet_response.text)
