import requests
import os
from datetime import datetime

# OpenWeather API 키
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Seoul"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# README 파일 경로
README_PATH = "README.md"

def get_weather():
    """OpenWeather API를 호출하여 서울의 날씨 데이터를 가져옴"""
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        return f"서울의 현재 날씨: {weather}, 온도: {temp}°C, 습도: {humidity}%"
    else:
        return "날씨 정보를 가져오는 데 실패했습니다."

def update_readme():
    """README.md 파일을 업데이트"""
    weather_info = get_weather()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    readme_content = f"""
# Weather API Status

이 리포지토리는 OpenWeather API를 사용하여 서울의 날씨 정보를 자동으로 업데이트합니다.

## 현재 서울 날씨
> {weather_info}

⏳ 업데이트 시간: {now} (UTC)

---
자동 업데이트 봇에 의해 관리됩니다.
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()

