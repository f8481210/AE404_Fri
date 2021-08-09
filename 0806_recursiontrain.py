'''
台鐵查詢台北到台中，
之後在執行程式碼記得輸入最近日期(過去的會沒資料)
這個是利用遞迴查詢當天的所有車次
'''
import requests
from bs4 import BeautifulSoup
import time


theDay = input("哪一天要搭台鐵(格式:2020/02/21)?")
timeSelect = input("想搭乘什麼時間(格式:06:30，24小時制)?")

def search(theDay, timeSelect):
    #我要傳遞的資料
    payload = {"startStation": "1000-臺北",
                "endStation": "3300-臺中",
                "transfer": "ONE",
                "rideDate": theDay,
                "startOrEndTime": "true",
                "startTime": timeSelect,
                "endTime": "23:59",
                "trainTypeList": "ALL"}
    #網址Request URL
    res = requests.post("https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime",data = payload)
    
    soup = BeautifulSoup(res.text,"html.parser")
    
    Finish = False

    for i in range(11):
        #車次
        trainNumber = soup.find_all('ul',class_="train-number")[i]
        a = trainNumber.find('a')
        #時間
        trainTime = soup.find_all('span',class_="time")[i]
        #print(trainTime)
        
        if len(trainTime.text)<5:
            Finish = True
            break
        print("車次:"+a.text)
        print("出發-抵達(行車時間):",trainTime.text)
        print("=====================================================")
    
    if Finish:
        print("查詢完成")
    else:
        timeSelect = trainTime.text[0:3]+str(int(trainTime.text[4])+1)
        time.sleep(1)
        return search(theDay,timeSelect)
        
search(theDay, timeSelect)