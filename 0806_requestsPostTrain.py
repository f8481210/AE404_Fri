'''
台鐵查詢台北到台中，2021/08/06
'''
import requests
from bs4 import BeautifulSoup

#我要傳遞的資料
payload = {"startStation": "1000-臺北",
            "endStation": "3300-臺中",
            "transfer": "ONE",
            "rideDate": "2021/08/06",
            "startOrEndTime": "true",
            "startTime": "00:00",
            "endTime": "23:59",
            "trainTypeList": "ALL"}
#網址Request URL
res = requests.post("https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime",data = payload)

soup = BeautifulSoup(res.text,"html.parser")

#取前11筆火車車次
for i in range(11):
    trainNumber = soup.find_all('ul',class_="train-number")[i]
    for each_a in trainNumber:
        a = each_a.find('a')
        if a != -1:
            print("車次",a.text)
    
    '''
    trainTime = soup.find_all('div',class_="ui-block-b")[i]
    nonReservedNumber = soup.find_all('div',class_="ui-block-c")[i]
    print("車次:"+trainNumber.text)
    print("出發-抵達(行車時間):"+trainTime.text)
    print("自由座車廂數:"+nonReservedNumber.text)
    print("=====================================================")
    '''