from datetime import datetime

import requests

APP_ID = "d8fa5ce2"
API_KEY = "97bba323f94e1b9dcf8aa0e1c586b9b4"

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 175
AGE = 25
SHEET_ENDPOINT = "https://api.sheety.co/824058f8790a10294d39693ca6110eba/workoutTracking/workouts"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs)

    print(sheet_response.text)
