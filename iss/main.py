import requests
from datetime import datetime



MY_LAT = 38.907192
MY_LONG = 77.036873
FORMAT = 0


def is_iss_overhead():

	response = requests.get(url="http://api.open-notify.org/iss-now.json")
	response.raise_for_status()

	data = response.json()
	longitude = data["iss_position"]["longitude"]
	latitude = data["iss_position"]["latitude"]

	iss_position = (longitude, latitude)

	# if the iss is close to my current positon / + or - 5
	if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
		return True


def in_night():
	parameters = {
	"lat": MY_LAT,
	"lng": MY_LONG,
	"formatted": FORMAT
	}
	response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
	response.raise_for_status()
	data = response.json()
	sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
	sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()# and it is currently dark 
# 

