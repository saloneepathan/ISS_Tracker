# This project will compare your current location with the ISS location,
# if the ISS is above you in the sky then the code will email you asking to look up in the sky to spot the ISS.
# ISS -> International Space Station

import requests
from datetime import datetime
import smtplib

# Replace the text below with your own Email and Password Credentials:
MY_EMAIL = "youremail@emailprovider.com"
MY_PASSWORD = "yourpassword@123"

# This is a sample latitude and longitude position for London,
# you can replace it with the latitude and longitude position for your current location.
# You can use this site to find your current latitude and longitude: https://www.latlong.net/
MY_LAT = 51.507351  # Latitude for London
MY_LNG = -0.127758  # Longitude for London


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def is_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    res = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()
    sunrise = int(res.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(res.json()["results"]["sunset"].split("T")[1].split(":")[0])
    hr_now = datetime.now().hour
    if hr_now >= sunset or hr_now <= sunrise:
        return True


if is_nighttime() and is_iss_overhead():
    # If you use an email provider other than gmail then,
    # make sure to look up the current location of your email providers smtp server
    # for example for yahoo -> "smtp.mail.yahoo.com" and for hotmail -> "smtp.live.com".
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: Look Up👆\n\n The ISS is above you in the sky. Enjoy!!"
    )
