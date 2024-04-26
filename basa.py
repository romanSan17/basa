import json
json_data='{nimi":"Roman Sandakov","vanus":51,"prillid":true}'
data=json.loads(json_data)
print(data["nimi"])

print(data)
for id_,dat in enumerate(data):
    print(id_,"-",dat)

for key, value in data.items():
    print(key,":",value)

data2={
    "nimi":"Anna",
    "vanus":"55",
    "abielus":True,
    "lapsed":("Inna","Mati"), 
    "koduloomad":None,
    "autod":
    [
        {"muudel":"BMW","värv":"punane","jõud":500,"number":"123ABC"},
        {"muudel":"Ford","värv":"punane","must":300,"number":"321CBA"},
     ]
    }
print(json.dumps(data2))
print(json.dumps(data2,indent=2,separators=(".","="),sort_keys=True))
with open("data_file.json","w") as w_file:
    json.dump(data2,w_file)

print("Andmed failist:")
with open("data_file.json","r") as r_file:
    data2=json.loads(r_file)

print(data2)