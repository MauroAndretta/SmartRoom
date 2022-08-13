# -*- coding: utf-8 -*-
from pyswip import Prolog

global prolog
prolog = None

def initialize():
    global prolog
    prolog = None
    prolog = Prolog()
    prolog.consult("C:/Users/Mauro-Pc/Desktop/progetto/smarthome.pl")

    
def assertz(cmd):
    prolog.assertz(cmd)
    
def query(query):
    return list(prolog.query(query))

def getSensorType(sensorID):
    return query("sensor(" + sensorID +" ,X)")

def getActuatorType(actuatorID):
    return query("actuator(" + actuatorID +" ,X)")

def getSensorValue(sensorID):
    return query("sensorValue(" + sensorID +" ,X)")

def getActuatorValue(actuatorID):
    return query("actuatorValue(" + actuatorID +" ,X)")

def saveNewPreference(name, typeID, Value, Actuators):
    if bool(getPreferences(name, typeID))== False:
        assertz("preferncesInstaces("+str(name)+", "+str(typeID)+", "+str(Value)+", "+str(Actuators)+")")
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
    query("replace_existing_fact(sensorValue(" + sensorID +" ,_), sensorValue(" + sensorID+ ", "+value+"))")

def setActuatorValue(actuatorID, value):
    query("replace_existing_fact(actuatorValue(" + actuatorID +" ,_), actuatorValue(" + actuatorID+ ", "+value+"))")

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
        query("remove_existing_fact(preferncesInstaces(" + ID + ",  _, _, _))")
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
    listQuery = query("preferncesInstaces(X, _, _, _)")
    listOfPrefernces = set()
    for i in range(len(listQuery)):
        listOfPrefernces.add(listQuery[i]["X"])
    
    return listOfPrefernces

def checkPreferencesByName(name):
    return bool(query("preferncesInstaces("+name+", _, _, _)"))


def getPreferences(typeID):
    listQuery = query("preferncesInstaces(X, "+ typeID +", _, _)")
    listOfPrefernces = set()
    for i in range(len(listQuery)):
        listOfPrefernces.add(listQuery[i]["X"])
    
    return listOfPrefernces

def getAllType():
    listQuery = query("propertyType(X)")
    listOfType = set()
    for i in range(len(listQuery)):
        listOfType.add(listQuery[i]["X"])
    
    return listOfType
        
