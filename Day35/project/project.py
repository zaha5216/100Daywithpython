import os
import requests
from twilio.rest import Client

account_sid = os.environ["AC179ff9833121c3a84abf707a49a8ecb8"]
auth_token = os.environ["10137707459abe9fe7acec20860b4cd5"]
client = Client(account_sid, auth_token)

twilio_number = os.environ["18655127387"]
my_number = os.environ["79817375216"]

LATITUDE =  59.938480
LONGITUDE = 30.312481

api_key = os.environ["9598fe56acff757ba215814cdbf622bd"]
api_url = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(api_url, params=params)
response.raise_for_status()

data = response.json()

for hourly_data in data["hourly"][:12]:
    condition_code = hourly_data["weather"][0]["id"]
    if condition_code < 700:
        message = client.messages.create(
            body="It's gonna rain! Don't forget to bring an ☔",
            from_=twilio_number,
            to=my_number
        )
        break
