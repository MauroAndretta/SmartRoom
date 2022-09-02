# -*- coding: utf-8 -*-
from pyswip import Prolog

global prolog
prolog = None

def initialize():
    global prolog
    prolog = Prolog()
    prolog.consult("smarthome.pl")   
    readFromFile()  
  


def writeToFile(query):
    f = open("mylog.pl", "a")
    f.write(query + "\n"  )
    f.close()    
    
    
def readFromFile():
    file = open("mylog.pl", "r")
    for line in file:
        line = line.replace(' ','')
        print(line)
        if '\n'  != line and '' != line:           
            if "set" in line:
                list(prolog.query(str(line)))
            elif "replace_existing_fact" in line:
                list(prolog.query(str(line)))
            elif "remove_existing_fact" in line:
                list(prolog.query(str(line)))
            else: 
                prolog.assertz((str(line)))
    print("ho finito di leggere i log")
    file.close()
    
def assertz(cmd):
    prolog.assertz(cmd)
    writeToFile(cmd)
    
def query(query):
    if "set" in query:
        writeToFile(query)
    elif "replace_existing_fact" in query:
        writeToFile(query)
    elif "remove_existing_fact" in query:
        writeToFile(query)
    return list(prolog.query(query))

def getSensorType(sensorID):
    return query("sensor(" + sensorID +" ,X)")


def getSensorNameByType(typeId):
    return query("sensor(X, "+typeId+")")

def getActuatorType(actuatorID):
    return query("actuator(" + actuatorID +" ,X)")


def getSensorNameByTypeAndLocation(typeId, location):
    if location == "inside":
        return getSensorNameByTypeInsideOnly(typeId)
    elif location == "outside":
        return getSensorNameByTypeOutsideOnly(typeId)

def getSensorNameByTypeInsideOnly(typeId):
    return query("sensor(X, "+typeId+"),inside(X)")


def getSensorNameByTypeOutsideOnly(typeId):
    return query("sensor(X, "+typeId+"), outside(X)")

def getActuatorNameByTypeAndLocation(typeId, location):
    if location == "inside":
        return getActuatorNameByTypeInsideOnly(typeId)
    elif location == "outside":
        return getActuatorNameByTypeOutsideOnly(typeId)

def getActuatorNameByTypeInsideOnly(typeId):
    return query("actuator(X, "+typeId+"),inside(X)")


def getActuatorNameByTypeOutsideOnly(typeId):
    return query("actuator(X, "+typeId+"), outside(X)")
       

def getSensorValue(sensorID):
    query_list = query("sensorValue(" + sensorID +" ,X)")
    if len(query_list) == 1:
        return str(query_list[0]["X"])
    else: return query_list 
    

def getActuatorValue(actuatorID):
    query_list = query("actuatorValue(" + actuatorID +" ,X)")
    if len(query_list) == 1:
        return str(query_list[0]["X"])
    else: return query_list 

def saveNewPreference(name, typeID, Value, Actuators):
    if bool(checkPreferencesWithActuator(name, typeID, Actuators))== False:
        assertz("preferencesInstance("+str(name)+", "+str(typeID)+", "+str(Value)+", "+str(Actuators)+")")
        return True
    else : return False


def setActuatorType(actuatorID, typeID, location):
    if bool(getSensorType(actuatorID)) == False and bool(getActuatorType(actuatorID)) == False:
        assertz("actuator(" + actuatorID+ ", "+typeID+")")
        assertz("actuatorValue(" + actuatorID+ ", 0)")
        if location == "inside":
            assertz(location + "(" + actuatorID+ ")")
        return True
    else : return False
    
def setSensorType(sensorID, typeID, location):
    if bool(getSensorType(sensorID)) == False and bool(getActuatorType(sensorID))  == False:
        assertz("sensor(" + sensorID+ ", "+typeID+")")
        assertz("sensorValue(" + sensorID+ ", 0)")
        if location == "inside":
            assertz(location + "(" + sensorID+ ")")
        return True
    else : return False

def setSensorValue(sensorID, value):
    old_value = str(getSensorValue(sensorID))
    query("replace_existing_fact(sensorValue(" + str(sensorID) +" ,"+str(old_value)+"), sensorValue(" + str(sensorID)+ ", "+str(value)+"))")
    # query("replace_existing_fact(sensorValue(" + sensorID +" ,_), sensorValue(" + sensorID+ ", "+value+"))")
    
def setSensorValueByType(typeID, location, value):
    list_sensor = getSensorNameByTypeAndLocation(typeID,location)
    for i in range(len(list_sensor)):
        name_sensor = list_sensor[i]['X']
        setSensorValue(name_sensor,value)     
    

def setActuatorValue(actuatorID, value):
    old_value = str(getActuatorValue(actuatorID))
    query("replace_existing_fact(actuatorValue(" + str(actuatorID) +" ,"+str(old_value)+"), actuatorValue(" + str(actuatorID)+ ", "+str(value)+"))")
    # query("replace_existing_fact(actuatorValue(" + actuatorID +" ,_), actuatorValue(" + actuatorID+ ", "+value+"))")

def removeInstance(ID):
    check = False
    if bool(getSensorType(ID)) == True:
        query("remove_existing_fact(sensor(" + ID + ", _))")
        query("remove_existing_fact(sensorValue(" + ID + ", _))")
        query("remove_existing_fact(inside(" + ID + "))")
        check = True
    elif bool(getActuatorType(ID)) == True:
        query("remove_existing_fact(actuator(" + ID + ", _))")
        query("remove_existing_fact(actuatorValue(" + ID + ", _))")
        query("remove_existing_fact(inside(" + ID + "))")
        check = True
    elif bool(checkPreferencesByName(ID)) == True:
        query("remove_existing_fact(preferencesInstance(" + ID + ",  _, _, _))")
        check = True
    return check
           
    
def getAllActuatorByType(typeID):
    actuatorList = query("actuator(X,"+ typeID + ")")
    dictActuator = set()
    for i in range(len(actuatorList)):
        dictActuator.add(actuatorList[i]["X"])
          
    return dictActuator 

def getAllSensorByType(typeID):
    sensorList = query("sensor(X,"+ typeID + ")")
    dictSensor = set()
    for i in range(len(sensorList)):
        dictSensor.add(sensorList[i]["X"])
          
    return dictSensor 


def getAllActuator():
    actuatorList = query("actuator(X,Y)")
    dictActuator = {}
    for i in range(len(actuatorList)):
        dictActuator [actuatorList[i]["X"]]= actuatorList[i]["Y"]
        
    newdict = {}
    for k,v in dictActuator.items():
        temp = query("actuatorValue("+ str(k) +",Y)")
        if bool(temp):
            newdict[k]= [v, temp[0]["Y"]]
    return newdict

def getAllSensor():
    sensorList = query("sensor(X,Y)")
    dictsensor = {}
    for i in range(len(sensorList)):
        dictsensor [sensorList[i]["X"]]= sensorList[i]["Y"]
        
    newdict = {}
    for k,v in dictsensor.items():
        temp = query("sensorValue("+str(k)+",Y)")
        if bool(temp):
            newdict[k]= [v, temp[0]["Y"]]
    return newdict

def setPreference(PIId):
    query("set("+PIId+")")
    
def getAllPreferences():
    listQuery = query("preferencesInstance(X, _, _, _)")
    listOfPrefernces = set()
    for i in range(len(listQuery)):
        listOfPrefernces.add(listQuery[i]["X"])
    
    return listOfPrefernces

def checkPreferencesByName(name):
    return bool(query("preferencesInstance("+name+", _, _, _)"))


def checkPreferences(name, typeID):
    return bool(query("preferencesInstance("+name+","+ typeID +", _, _)"))

def checkPreferencesWithActuator(name, typeID, actuators):
    
    if type(actuators) == list:
        for i in range(len(actuators)):
            if(bool(query("preferencesInstance("+name+","+ typeID +", _, X), memberCheck("+actuators[i]+",X)"))) == True:
                return True
        return False
    else : return bool(query("preferencesInstance("+name+","+ typeID +", _, X), memberCheck("+actuators+",X)"))


def getAllType():
    listQuery = query("propertyType(X)")
    listOfType = set()
    for i in range(len(listQuery)):
        listOfType.add(listQuery[i]["X"])
    
    return listOfType

def getPreviusValue(nameid):
    for line in reversed(open("mylog.pl").readlines()):
        print(line)
        if "replace_existing_fact(" in line:
            line = line.replace('replace_existing_fact(','')
            line = line.split(',')
            name = line[0][line[0].find("(")+1:len(line[0])]
            name = name.replace(' ','')
            if str(name) == str(nameid):
                return line[1].replace(')','').replace(' ','')
    return str(0)        
        
    

def why(actuatorID):
    for line in reversed(open("mylog.pl").readlines()):
        if "replace_existing_fact" in line:
            if "Value(" + actuatorID in line:
                return "Actuator has been manually modified with the value of: " + getActuatorValue(actuatorID)
        elif "set" in line:
            preference_name = line[line.find("(")+1:line.find(")")]
            list_prefrences = list(prolog.query("preferencesInstance("+preference_name+", Y, Desired, X), memberCheck("+actuatorID+",X)"))
            if bool(list_prefrences):
                answer = "The preference '" + preference_name + "' has modified the actuator's value '"+actuatorID+"' because:\n"
                for i in range(len(list_prefrences)):
                    if i > 0 :
                        answer += "But this value has been replaced because:\n"
                    type_preference = list_prefrences[i]["Y"]
                    value_desired_preference = str(list_prefrences[i]["Desired"])
                    if type_preference == "temp":
                        name_sensor_outside = getSensorNameByTypeOutsideOnly(type_preference)[0]['X']
                        value_outside = getSensorValue(name_sensor_outside)
                        name_sensor_inside = getSensorNameByTypeInsideOnly(type_preference)[0]['X']
                        value_inside = getPreviusValue(name_sensor_inside)
                        comparator_outside = "equal"
                        comparator_inside = "equal"
                        
                        if int(value_outside) > int(value_desired_preference):
                            comparator_outside = "higher"
                        elif int(value_outside) < int(value_desired_preference):
                            comparator_outside = "lower"
                        
                        if int(value_inside) > int(value_desired_preference):
                            comparator_inside = "higher"
                        elif int(value_inside) < int(value_desired_preference):
                            comparator_inside = "lower"
                            
                        answer += "considirening the "+ type_preference + " and the related value of the sensor '" +name_sensor_outside+ "' equal to\n'"
                        answer += value_outside + "' which is "+comparator_outside+ " than the desired value equal to '" 
                        answer += value_desired_preference + "'\n" + "and also considering that the value of the sensor '"+ name_sensor_inside+ "' equal to\n'"
                        answer += value_inside + "' is " + comparator_inside + " than the desired value,\n"+ "then the actuator '" 
                        answer += actuatorID + "' has been set to: '" + getActuatorValue(actuatorID) + "'.\n"        
                    else:     
                        name_sensor = getSensorNameByTypeOutsideOnly(type_preference)[0]['X']
                        value_sensor = getSensorValue(name_sensor)
                        
                        comparator= "equal"
                        
                        if int(value_sensor) > int(value_desired_preference):
                            comparator = "higher"
                        elif int(value_sensor) < int(value_desired_preference):
                            comparator = "lower"
                        
                        
                        answer += "considirening the " + str(type_preference) + " and the related value of the sensor '" + str(name_sensor) + "'"
                        answer += "\n" +"which has value equal to '" + str(value_sensor) + "' that is " + str(comparator) + " than the desired value for the prefrence,\n" + "that is '" 
                        answer += str(value_desired_preference) + "', then the actuator '"  + str(actuatorID) + "' has been set to: '" + str(getActuatorValue(actuatorID)) +"'.\n"  
                return answer
    return "NO ANSWER FOUND"