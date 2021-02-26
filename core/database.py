from pymongo import MongoClient

from .files import Data

client = MongoClient(Data("config").yaml_read()['mongo-uri'])

class Punishments:
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.db = client["SMETCH"]
        self.col = client["SMETCH"]["punishments"]

    
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

class Thanks:
    def __init__(self, user_id=None):
        self.user = user_id
        self.col = client["SMETCH"]["thanks"]
        if self.user:
            if not self.col.find_one({"_id":self.user}):
                self.col.insert_one({"_id": self.user, "thanks_daily": 0, "thanks_weekly":0, "thanks_alltime":0})
    
    @property
    def exists(self):
        r = self.col.find_one({"_id":self.user})
        if r: return True
        return False
    
    @property
    def delete(self):
        self.col.delete_one({"_id":self.user})

    @property
    def reset_weekly(self):
        self.col.update_many({}, {"$set": {"thanks_weekly": 0}})

    @property
    def reset_daily(self):
        self.col.update_many({}, {"$set": {"thanks_daily": 0}})

    def add(self, points=1):
        self.col.update_one({"_id":self.user},
        {"$inc": {
            "thanks_daily": points,
            "thanks_weekly": points,
            "thanks_alltime": points
        }})

    def remove(self, points=1):
        self.col.update_one({"_id":self.user},
        {"$inc": {
            "thanks_daily": -points,
            "thanks_weekly": points,
            "thanks_alltime": points
        }})
    
    def get(self):
        return self.col.find_one({"_id":self.user})