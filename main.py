import requests
import datetime as dt
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]



Nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}
answer = input("Tell me, what did you do today: ")
print(answer)
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
 "query": answer,
 "gender": "male",
 "weight_kg": 77,
 "height_cm":182,
 "age": 19
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=Nutri_headers)
data = response.json()

data_duration = data['exercises'][0]['duration_min']
data_calories = data['exercises'][0]['nf_calories']
data_exercise = data['exercises'][0]['name'].title()
today = dt.datetime.now()
today2 = today.strftime("%Y/%m/%d")
today3 = today.strftime("%H:%M")
SHEETY_URL = "https://api.sheety.co/99f625a2421bb57b82bb654c0bac3544/myWorkoutsApi/workouts"
sheety_datas = {
    "workout": {
        "exercise": data_exercise,
        "duration": data_duration,
        "calories": data_calories,
        "date": today2 ,
        "time": today3

    }
}

bearer_headers = {
    "Authorization": "Bearer dsaztgfdsazhg232563gsdazhw"
}
response_2 = requests.post(url=SHEETY_URL, json=sheety_datas, headers=bearer_headers)