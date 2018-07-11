import requests

#Clé d'API https://home.openweathermap.org 

apiKey = "289b67765b5ae65f3fbb150b8de66b33" 

#API CALL : http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY} 
URLForge = "http://api.openweathermap.org/data/2.5/weather?id=3007535&APPID="+apiKey

answer = requests.get(URLForge)
if answer != 200:
	raise ApiError('GET /tasks/ {}'.format(answer.status_code))

for todo_item in answer.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))