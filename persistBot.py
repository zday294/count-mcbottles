import json
from discord.ext import commands
from details import details



class PersistBot(commands.Bot):
    def __init__(self, persistFile: str, prefix: str):
        super.__init__(prefix)
        self.fileName = persistFile
        with open(self.fileName) as file:
            data = file.readlines()
            self.persistData = details(json.loads(data)) 

    
    async def close(self):
        print("Saving data")
        data = json.dumps(self.persistData)
        with open(self.filename) as file:
            file.write(data)

        print("Shutting down")

