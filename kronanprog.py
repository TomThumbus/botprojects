import json
from math import trunc
import utilities
from random import randint

class Data:
    def __init__(self, datadictionary):
        dump = json.dumps(datadictionary)
        self.data = json.loads(dump)
    
class CreatureData(Data):
    def __init__(self, datadictionary):
        dump = json.dumps(datadictionary)
        self.data = json.loads(dump)
    
    def __repr__(self):
        return json.dumps(self.data)
    
    def __str__(self):
        return json.dumps(self.data)




class Creature:
    def __init__(self):
        self.type = "Creature"
        self.data = CreatureData({"type":"Creature", "DNA":"ABCCDCCCAAAAABABDDDD"})
    
    def readData(self):
        print(json.dumps(self.data.data))


# creature = Creature()
# creature.readData()

# new_creature = utilities.generateCreature(str(creature.data.data))

creatureslist = {"Creatures":[]}
raw_data = {}
with open("creature_log.json", "r") as f:
    raw_data = json.load(f)

for creature in raw_data["Creatures"]:
    creatureslist["Creatures"].append(creature)

# creatureslist["Creatures"].append(new_creature)

print("<<DEBUG>> dump creatures list data")
# print(json.dumps(creatureslist, indent=4, ensure_ascii=True))

with open("creature_log.json", 'w') as f:
    f.write(json.dumps(creatureslist, indent=4, ensure_ascii=True))

print("<<DEBUG>> wrote to file")
child = {}
p1 = creatureslist["Creatures"][randint(0, len(creatureslist["Creatures"]) - 1)]
p2 = creatureslist["Creatures"][randint(0, len(creatureslist["Creatures"]) - 1)]

ch1 = utilities.reproduce(p1, p2)
if ch1 is None:
    exit()
else:
    new_ch = utilities.generateCreature(ch1)



    print("<<DEBUG>> new child data")
    print(json.dumps(new_ch, indent=4, ensure_ascii=True))

    with open("creature_log.json", 'w') as f:
        creatureslist["Creatures"].append(new_ch)
        ded = creatureslist["Creatures"].pop(0)
        f.write(json.dumps(creatureslist, indent=4, ensure_ascii=True))

print("<<DEBUG>> debug dump")
# print(json.dumps(new_creature, indent=4, ensure_ascii=True))
