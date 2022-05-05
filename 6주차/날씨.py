import requests
import json

city='Seoul'
lang='kr'
APIkey='2ce32eb348d1b635987a559b87df00e8'

url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}&lang={lang}&units=metric'
request=requests.get(url)

data=json.loads(request.text)
print(request.text)

print(data['name'],'의 날씨 정보입니다.')
print('오늘 날씨는 ', data['weather'][0]['description'],'이네요')
print('온도는 ',data['main']['temp'],'도 이지만, 이게 중요한게 아니고 실제 체감온도는 ', data['main']['feels_like'],'도 입니다.')
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
print("습도는 ",data["main"]["humidity"],"입니다.")
print("기압은 ",data["main"]["pressure"],"입니다.")
print("풍향은 ",data["wind"]["deg"],"입니다.")
print("풍속은 ",data["wind"]["speed"],"입니다.")