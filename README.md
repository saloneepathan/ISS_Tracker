# 🛰️ ISS Overhead Notifier

This Python script notifies you via email when the **International Space Station (ISS)** is currently flying overhead and it’s nighttime at your location—making it visible in the night sky.

---

## 🌍 What It Does

- Tracks the real-time location of the ISS using [Open Notify API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/).
- Fetches sunrise and sunset times for your location from [Sunrise-Sunset API](https://sunrise-sunset.org/api).
- If the ISS is overhead **and** it's dark outside, the script sends you an email alert to look up!

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/iss-overhead-notifier.git
cd iss-overhead-notifier
```

### 2. Install Required Libraries
This script uses built-in and external libraries. Install the required external library:
```bash
pip install requests
```

### 3. Set Your Configuration

In the Python script:  
- Replace `MY_EMAIL` and `MY_PASSWORD` with your actual email and password (or app password if using 2FA).  
- Update `MY_LAT` and `MY_LNG` with your actual geographic coordinates.  
- Use [latlong.net](https://www.latlong.net/) to find yours.

```python
MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_password"
MY_LAT = 51.507351   # Example: London
MY_LNG = -0.127758
```

## 🧪 How to Run

Run the script manually or schedule it using a cron job or Task Scheduler:
```bash
python iss_notifier.py
```

## 🛰️ APIs Used

- [Open Notify - ISS Location](https://chatgpt.com/c/6815adea-88d0-800b-be61-8556e4efeb89#:~:text=%F0%9F%8C%90%20APIs%20Used-,Open%20Notify%20%2D%20ISS%20Location,-Sunrise%2DSunset%20API)
- [Sunrise-Sunset API](https://chatgpt.com/c/6815adea-88d0-800b-be61-8556e4efeb89#:~:text=Notify%20%2D%20ISS%20Location-,Sunrise%2DSunset%20API,-%F0%9F%93%A7%20Example%20Notification)


### 📧 Example Notification

```text
Subject: Look Up👆

The ISS is above you in the sky. Enjoy!!
```

### 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and open a pull request.
