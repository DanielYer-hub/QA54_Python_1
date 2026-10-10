#dumps()- pyton->json str
#loads() -json-> pyton object str
import json

#dump()save Pyton object- > file.json (file)
#load() file.json ->> Pyton (file)

user = {"username":"kristina","age": 25,"is_admin":True}
json_str = json.dumps(user)
print(json_str)
print(type(json_str))

user = json.loads(json_str)
print()
print(user)
print(type(user))
print(user["username"])

test_config = {
    "url": "http://127.0.0.1:8000",
    "username": "kristina",
    "password": "Aa123456!",
    "timeout": 20
}

with open("config.json","w",encoding="utf-8") as file:
    json.dump(test_config,file,indent=4,ensure_ascii=False)

with open("config.json","r",encoding="utf-8") as file:
    config = json.load(file)
    print(config)
    print(config["url"])

def save_profile(name,age,city):
    profile = {
        "name":name,
        "age": 39,
        "city":name
    }
    with open("profile.json","w",encoding="utf-8") as file:
         json.dump(profile,file,indent=4)
save_profile("daniel","28","Haifa")



