from flask import Flask, render_template
from requests import get


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", menu=MENU)


@app.get("/menu")
def menu():
    return render_template("menu.html", menu=MENU)


@app.get("/weather")
def weather():
    url = "https://open-weather13.p.rapidapi.com/city/landon/EN"

    headers = {
        "x-rapidapi-key": "957b13c0dcmsh79cbdd448703f03p1c0563jsnb79aebaa0309",
        "x-rapidapi-host": "open-weather13.p.rapidapi.com",
    }

    response = get(url, headers=headers)
    data = response.json()

    temp = data.get("main").get("temp")
    pressure = data.get("main").get("pressure")
    humidity = data.get("main").get("humidity")

    weather_dict = {
        "temp": temp,
        "pressure": pressure,
        "humidity": humidity,
    }

    return render_template("weather.html",all_weather=weather_dict, menu=MENU)


MENU = {
    index.__name__,
    menu.__name__,
    weather.__name__,
}

if __name__ == "__main__":
    app.run(
        host="0.0.0.1",
        port=8080,
        debug=True,
    )