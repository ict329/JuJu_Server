from mongoconf import *
from pymongo import MongoClient

class MGEngine:
    def __init__(self):
        self.client = MongoClient(MONGO_CONFIG['HOST'], MONGO_CONFIG['PORT'])
        dbname = MONGO_CONFIG['DB']
        self.db = self.client[dbname]
    
    def findone(self):
        one = self.db.test.find_one()
        print one

    def find(self,tablename,condition,order,returnfileds,offset,limit):
        return None

    def update(self,tablename,condition,update,multiple):
        return None

    def insert(self,tablename,condition):
        return None
    
    def delete(self,tablename,condition):
        return None
    
    def count(self,tablename,condition):
        return None


"""
find
insert
update
delete

"""

engine = MGEngine()
engine.findone()
