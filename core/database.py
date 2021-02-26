from pymongo import MongoClient

from .files import Data

client = MongoClient(Data("config").yaml_read()['mongo-uri'])

class Punishments:
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.db = client["main"]
        self.col = client["main"]["punishments"]

    
    def getCases(self, **kwargs):
        return [r for r in self.col.find(kwargs)]
    
    def getCase(self, **kwargs):
        return self.col.find_one(kwargs)
    
    def addCase(self, **kwargs):
        ids = [i["_id"] for i in self.getCases()]
        try:
            kwargs["_id"] = next(_id+1 for _id in ids if _id+1 not in ids)
        except:
            kwargs["_id"] = 0
        kwargs["user"] = self.user_id
        self.col.insert_one(kwargs)
    
    def removeCase(self, **kwargs):
        self.col.delete_one(kwargs)