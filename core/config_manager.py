import json 
from pathlib import Path


class ConfigManager:

    def __init__(self,config_path="config/config.json"):
        self.config_path = Path(config_path)
        self.config = {}
        self.load()
    def load(self):
        with open(self.config_path,"r") as file:
            self.config = json.load(file)

    def save(self):
        with open(self.config_path,"w") as file:
            json.dump(self.config,file,indent=4)   
               
    def get(self,key,default=None):
        return self.config.get(key,default)
    
    def set(self,key,value):
        self.config[key] = value
        self.save()

    def reload(self):
        self.load()