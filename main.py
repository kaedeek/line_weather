from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
import requests, schedule, threading

# token
token = "line notify token"

# API
API = 'https://notify-api.line.me/api/notify'

def send(message):
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + token}
    requests.post(API, data=payload, headers=headers)

def main():
    if send == send:
        send(f"起動したう\n毎朝7時に天気予報をお届けするよ")
        aihi_weather()
        hiroshima_weather()
        schedule.every().days.at('07:00').do(aihi_weather)
        schedule.every().days.at('07:00').do(hiroshima_weather)
        while True:
            schedule.run_pending()
            sleep(1)
    else:
        send(f"えらーだよ")

def aihi_weather():
    city_code = "230010"
    url = "https://weather.tsukumijima.net/api/forecast/city/" + city_code
    try:
        responese = requests.get(url)
        responese.raise_for_status() # ステータスコード200番台以外は例外とす
    except requests.exceptions.RequestException as e:
        print("ERROR:{}".format(e))
    else:
        weather_json = responese.json()
        print(weather_json['forecasts'][0]['chanceOfRain'])
    now_hour = datetime.now().hour
    if 0 <= now_hour and now_hour < 6:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T00_06']
    elif 6 <= now_hour and now_hour < 12:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T06_12']
    elif 12 <= now_hour and now_hour < 18:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T12_18']
    else:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T18_24']
    r = requests.get('https://weather.yahoo.co.jp/weather/jp/23/5110.html')
    soup = BeautifulSoup(r.content, "html.parser")
    wc = soup.find(class_="forecastCity")
    ws = [i.strip() for i in wc.text.splitlines()]
    wl = [i for i in ws if i != ""]
    message = ("<愛知 今日>" + "\n\n" + "> 天気" + "\n" + wl[1] + "\n\n" + f"> 降水確率 : {cor}" + "\n\n" + "> 気温" + "\n" "最高気温:" + wl[2] + "\n"+ "最低気温:" + wl[3])
    send(message)

def hiroshima_weather():
    city_code = "340010"
    url = "https://weather.tsukumijima.net/api/forecast/city/" + city_code
    try:
        responese = requests.get(url)
        responese.raise_for_status() # ステータスコード200番台以外は例外とす
    except requests.exceptions.RequestException as e:
        print("ERROR:{}".format(e))
    else:
        weather_json = responese.json()
        print(weather_json['forecasts'][0]['chanceOfRain'])
    now_hour = datetime.now().hour
    if 0 <= now_hour and now_hour < 6:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T00_06']
    elif 6 <= now_hour and now_hour < 12:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T06_12']
    elif 12 <= now_hour and now_hour < 18:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T12_18']
    else:
        cor = weather_json['forecasts'][0]['chanceOfRain']['T18_24']
    r = requests.get('https://weather.yahoo.co.jp/weather/jp/34/6710.html')
    soup = BeautifulSoup(r.content, "html.parser")
    wc = soup.find(class_="forecastCity")
    ws = [i.strip() for i in wc.text.splitlines()]
    wl = [i for i in ws if i != ""]
    message = ("<広島 今日>" + "\n\n" + "> 天気" + "\n" + wl[1] + "\n\n" + f"> 降水確率 : {cor}" + "\n\n" + ">気温" + "\n" "最高気温:" + wl[2] + "\n"+ "最低気温:" + wl[3])
    send(message)

if __name__ == "__main__":
    main()