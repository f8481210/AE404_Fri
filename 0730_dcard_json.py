'''
AE404-5課堂實作:使用Dcard提供的API取得寵物版熱門文章前40篇貼文
標題、id、topics。
'''

import json
import requests

#拿掉網址參數的before就會從第一篇開始、limit=40抓40篇

respond = requests.get("https://www.dcard.tw/service/api/v2/forums/pet/posts?popular=true&limit=40")
#json格式 -> python
jsonData = json.loads(respond.text)

#另一種轉換方式
#jsonData = respond.json()
#print(jsonData)


for i in jsonData:
    #title id topics
    data = {
        "Title" : i['title'],
        "ID" : i['id'],
        "Topics" : i['topics']
        }
    
    with open ("dcardpet.json","a", encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii = False)
    
    
    
    