import json
data = {
        'Name': "Eric",
        'height': 180.5,
        "Male": True,
        }
'''
#python資料轉JSON格式
toJson = json.dumps(data)
print(toJson)
print(type(toJson))

print()
#JSON格式轉python資料
toPython = json.loads(toJson)
print(toPython)
print(type(toPython))

'''
#python資料寫入json檔案
with open("test.json", "w") as file:
    json.dump(data,file)

#讀取json檔案並轉成python資料
with open("test.json","r") as file:
      jsonRead = json.load(file)
      print(jsonRead)
      print(type(jsonRead))
      print(jsonRead['Name'])
      print(type(jsonRead['Name']))


'''
#課堂實作
data = {
        "name": "diamond",
        "amount": 64,
        "onGround": True,
        "Position": [30.5, 30.825,-500.0]
        }
toJson = json.dumps(data)
with open("practice.json", "w") as file:
    json.dump(data,file)
with open("practice.json","r") as file:
      jsonRead = json.load(file)
      print(jsonRead)
      print(jsonRead["Position"])
'''