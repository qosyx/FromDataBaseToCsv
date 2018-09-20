import csv
import datetime
import json
import now
from bson.json_util import dumps
from pymongo import MongoClient

now = datetime.datetime.now()

class Bus(object):

    def __init__(self,_id,label,code,registration_number,seats,brand,model,year,description,length,width,mileage,serial_number,status,type,date_creation,date_updated,id):
        self._id=_id
        self.label = label

        self.code = code

        self.registration_number = registration_number

        self.seats = seats

        self.brand = brand

        self.model = model

        self.year = year

        self.description = description

        self.length = length

        self.width = width

        self.mileage = mileage

        self.serial_number = serial_number

        self.status = "AVAILABLE"

        self.type = type

        self.date_creation = str(now.day)+'/'+str(now.month)+'/'+str(now.year)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)

        self.date_updated = str(now.day)+'/'+str(now.month)+'/'+str(now.year)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)

        self.id = 2

class BusCsv(object):

            def __init__(self,label, code, registration_number, seats, brand, model, year, description, length,
                         width, mileage, serial_number, status, type, date_creation, date_updated, id):
                self.label = label

                self.code = code

                self.registration_number = registration_number

                self.seats = seats

                self.brand = brand

                self.model = model

                self.year = year

                self.description = description

                self.length = length

                self.width = width

                self.mileage = mileage

                self.serial_number = serial_number

                self.status = "AVAILABLE"

                self.type = type

                self.date_creation = date_creation

                self.date_updated = date_updated

                self.id = 2

            def __iter__(self):
                return (self.label,self.code ,  self.registration_number , self.seats,self.brand,self.model,self.year ,self.description,self.length,self.width ,self.mileage,self.serial_number,
                self.status,
                self.type ,
                self.date_creation,
                self.date_updated,
                self.id)



client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.mydatabase
f = open("/home/archange/Documents/template.csv", 'w', newline="", encoding='utf8')
cursor = db.posts.find()
for fi in cursor:
    #print(dumps(fi))
    ti = dumps(fi)
    j = json.loads(ti)
    u = Bus(**j)
    buscsv = BusCsv(u.label, u.code, u.registration_number, u.seats, u.brand, u.model, u.year, u.description, u.length,
                    u.width, u.mileage, u.serial_number, u.status, u.type, u.date_creation, u.date_updated, u.id)
    #obtention en json qui n'est plus utilisé
    buscsvToJson = json.dumps(buscsv.__dict__)
    #La classe en String pour l'ajout dans le CSV
    buscsvToString=buscsv.__iter__()
    item_id = buscsv.label
    writer = csv.writer(f)
    writer.writerow( buscsvToString)