# -*- coding: utf-8 -*-
from prolog import * 
import requests
import random
from faker import Faker
from bs4 import BeautifulSoup



def brightnessValue(skyinfo, time):
    weatherList_eng = [ "clear",
                        "Sunny",
                        "mostly sunny",
                        "Mostly cloudy",
                        "partly cloudy",
                        "Cloudy",
                        "Overcast",
                        "Rain",
                        "Drizzle",
                        "Snow",
                        "Stormy"]
        
    weatherList_ita =["sereno",
                      "Soleggiato",
                       "Per lo più soleggiato",
                       "Per lo più nuvoloso",
                       "Parzialmente nuvoloso",
                       "Nuvoloso",
                       "Coperto",
                       "Pioggia",
                       "Pioggia",
                       "Neve",
                       "Tempestoso"]
     
    brightnessIndex = [80,
                       70,
                       50,
                       50,
                       40,
                       40,
                       25,
                       30,
                       20]
    sunriseIndex = [7,12, 17, 20]
    deltaBrighnesValue = [0, 0.95, 1, 0.5, 0]
    weatherIndex = 99
    alphaBrighnesValue = 0
     
    hour,_ = time.split(":")
     
    for i in range(len(sunriseIndex)):
         if int(hour) > sunriseIndex[i]:
             alphaBrighnesValue = i+1
    
         
    for i in range(len(weatherList_eng)):
        if skyinfo.lower() in weatherList_eng[i].lower() or skyinfo.lower() in weatherList_ita[i].lower():
            weatherIndex = i
            break
         
    brightness_value = 99
    if weatherIndex != 99:
         brightness_value = random.randint(-5, 15) + (brightnessIndex[weatherIndex] * deltaBrighnesValue[alphaBrighnesValue])
         
    return brightness_value

def temperatureInsideHome(tempOutisde):
    temperatureInsideValue = int(tempOutisde) - random.randint(-10, 10) 
    if temperatureInsideValue < 0:
        return 0
    else: return temperatureInsideValue
    
def decibelValue(wind):
    dbValue = 0
    if int(wind) >= 40 :
        dbValue = 80 + random.randint(-5, 5)
    elif int(wind) >= 30 :
        dbValue = 60 + random.randint(-5, 5)
    elif int(wind) >= 20 :
        dbValue = 40 + random.randint(-5, 5)
    elif int(wind) >= 10 :
        dbValue = 20 + random.randint(-5, 5)
    elif int(wind) >= 0 :
        dbValue = 10 + random.randint(0, 5)
        
    return dbValue
        
    

def weather(city):   

    city = city.replace(" ", "+")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    day, time = time.split(" ")
    skyinfo = soup.select('#wob_dc')[0].getText().strip()
    temperature = soup.select('#wob_tm')[0].getText().strip()
    wind = soup.select('#wob_ws')[0].getText().strip()
    wind,_ = wind.split(" ")

    return location, day, time, skyinfo, temperature, wind

def simulateSensorValues():
    print("simulando i sensori")
    # fake = Faker()
    # city = fake.administrative_unit()
    # print(city)

    location,day,time,skyinfo,tempOutisde, wind =weather("Bari"+ " weather")
    
    db = int(decibelValue(wind))
    temperatureInside = int(temperatureInsideHome(tempOutisde))
    brightness = int(brightnessValue(skyinfo, time))
   
    return location,day,time,skyinfo,tempOutisde,wind,db,temperatureInside,brightness

# def changeSensorByPrefrence(preference):
#     query_list = query("preferencesInstance("+preference+", Y, Desired, _)")
#     print("cerco i sensori precedenti")
#     print(query_list)
#     if bool(query_list):
#         for i in range(len(query_list)):
#             if type(query_list[0]['Y']) == str:
#                 print(query_list[0]['Y'])
#                 if preference == "turn_off" :
#                     location,day,time,skyinfo,tempOutisde,wind,db,temperatureInside,brightness=getSensorsValues()
#                     type_preference = query_list[i]['Y']
#                     value_preference = query_list[i]['Desired']
#                     location = "inside"
#                     setSensorValueByType(type_preference,location,value_preference)
#                     setSensorValueByType("temp", location, str(temperatureInside))
#                 else:                    
#                     type_preference = query_list[i]['Y']
#                     value_preference = query_list[i]['Desired']
#                     location = "inside"
#                     setSensorValueByType(type_preference,location,value_preference)

def changeSensorByActuators():
    type_list = sorted(getAllType(), key=str.lower)
    type_list.remove('noise')
    for i in range(len(type_list)):
        typeId = type_list[i]
        #lista attuatori interni per il tipo
        query_actuator_list = getActuatorNameByTypeAndLocation(typeId, "inside")
        max_value = 0
        for i in range(len(query_actuator_list)):
            value = int(getActuatorValue(query_actuator_list[i]['X']))
            if max_value < value:
                max_value = value
        #se nessun attuatore interno dovesse essere acceso allora prendo valore da fuori
        if max_value == 0 :
            query_actuator_list = getActuatorNameByTypeAndLocation(typeId, "outside")
            max_value = 0
            for i in range(len(query_actuator_list)):
                value = int(getActuatorValue(query_actuator_list[i]['X']))
                if max_value < value:
                    max_value = value
            value_sensor_outside = int(getSensorValue(getSensorNameByTypeAndLocation(typeId, "outside")[0]['X']))
            if max_value > value_sensor_outside:
                max_value = value_sensor_outside
        
        print(max_value)
        if max_value == 0 and typeId == 'temp':
            _,_,_,_,_,_,_,temperatureInside,_=getSensorsValues()
            setSensorValueByType(typeId, "inside", str(temperatureInside))
        else: setSensorValueByType(typeId,"inside",max_value)
        
        
                    
def newSensorValueByType(typeID, location):
    query_list = getSensorNameByTypeAndLocation(typeID, location)
    return getSensorValue(query_list[0]['X'])
             
def getSensorsValues():
    print("restituendo i sensori")
    return location,day,time,skyinfo,tempOutisde,wind,db,temperatureInside,brightness


location,day,time,skyinfo,tempOutisde,wind,db,temperatureInside,brightness = simulateSensorValues()

