import requests
GENDER = ("GENDER")
WEIGHT_KG = ("WEIGHT")
HEIGHT_CM = ("HEIGHT")
# Replace these with your actual values
AGE = ("AGE")

APP_ID = ("e5818f60")
API_KEY = ("63d27d880990fed539339053530db7a8b")

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

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)