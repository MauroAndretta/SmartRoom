# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:16:00 2022

@author: Mauro-Pc
"""
# class sensors():
#     nome
#     propieta
#     valore



class Log():
    def __init__(self):
        self.row = []
    
    def readLog(self,path):
        import csv

        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    # print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    data = self.Row(row[0], row[1], row[2], row[3])
                    self.row.append(data)

            
    def writeLog(self, path):
        with open(path, 'w') as file:
            writer = csv.writer(file)
            for i in range(len(self.row)):
                print(self.row[i])
                writer.writerow(self.row[i].toCsv())
        
        
    
    class Row():
        def __init__(self, day, time, sensors, action):
            self.day = str(day)
            self.time = str(time)
            self.sensors = str(sensors)
            self.action = str(action)
            
        def getDay(self):
            return self.day
    
        def getTime(self):
            return self.time
        def getSensors(self):
            return self.sensors
        def getAction(self):
            return self.action
        
        def __str__(self):
            return "["+self.day +" "+ self.time +" "+ self.sensors +" "+ self.action +"]"
        def toCsv(self):
            return [self.day , self.time , self.sensors , self.action]
    
import csv 
log = Log()
log.readLog("C:/Users/Mauro-Pc/Desktop/progetto/log.csv")
log.writeLog("C:/Users/Mauro-Pc/Desktop/progetto/logTest.csv")