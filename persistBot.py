import json
from discord.ext import commands
from details import Details



class PersistBot(commands.Bot):
    def __init__(self, persistFile, prefix="-"):
        super().__init__(prefix)
        self.fileName = persistFile
        self.details = None
        try:
            with open(self.fileName, "r") as file:
                data = file.readlines()
                self.details = Details(json.loads(data)) 
        except:
            self.details = Details()

    
    async def close(self):
        print("Saving data")
        data = json.dumps(self.details.__dict__)
        with open(self.fileName, "w+") as file:
            file.write(data)

        print("Shutting down")

