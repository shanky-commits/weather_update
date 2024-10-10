import requests
from twilio.rest import Client

# WeatherMap API setup
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "3069781dd037aa577ba5afgsdie3wydh7"  # Replace with your actual API key
account_sid = "AC99cc8c9c9b2103fa5d2694989ghdhgh2"  # Replace with your actual account_sid
auth_token = "74766470fbc9f91ed5651ce0aefed7fa"     # Replace with your actual auth token

# Weather parameters
weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}

try:
    response = requests.get(OWM_Endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()

    # Check for rain
    will_rain = False
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True

    # Send SMS if it will rain
    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="+13344234999",  # Your Twilio number in E.164 format
            body="It's going to rain today. Remember to bring an ☔️",
            to="+91813983913"  # Replace with the recipient's phone number in E.164 format
        )
        print(f"Message sent with status: {message.status}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
