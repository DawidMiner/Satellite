import requests
import datetime as dt
from geopy.geocoders import Nominatim

LATITUDE = 52.179013
LONGITUDE = 23.104983

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}

satellite_request = requests.get(url="http://api.open-notify.org/iss-now.json")

iss_latitude = float(satellite_request.json()["iss_position"]["latitude"])
iss_longitude = float(satellite_request.json()["iss_position"]["longitude"])


response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

actual_time = dt.datetime.now().hour

if actual_time > sunset or actual_time < sunrise:
    if LATITUDE - 10 < iss_latitude < LATITUDE + 10 and LONGITUDE - 50 < iss_longitude < LONGITUDE + 50:
        print("look up")

geolocator = Nominatim(user_agent="geoapiExercises")

location = geolocator.reverse(str(iss_latitude) + "," + str(iss_longitude))
if location is not None:
    print(f"Aktualna lokalizacja satelity:\nDługość geograficzna: {round(iss_longitude, 2)}\nSzerokość geograficzna: {round(iss_latitude, 2)}\nPaństwo:{location}")
else:
    print(f"Aktualna lokalizacja satelity:\nDługość geograficzna: {round(iss_longitude, 2)}\nSzerokość geograficzna: {round(iss_latitude, 2)}\nSatelita aktualnie nie znajduje się nad żadnym państwem.")


