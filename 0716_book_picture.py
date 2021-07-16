import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.books.com.tw/web/sys_saletopb/books")
soup = BeautifulSoup(url.text,"html.parser")
lis = soup.find_all("li",class_='item')

'''
#所有img標籤
for each_li in lis:
    img = each_li.find("img")
    print(img)
'''

'''
#印出書名和圖片網址
for each_li in lis:
    img = each_li.find("img")
    src = img['src'] #圖片網址
    alt = img['alt'] #圖片名稱 書名
    print(alt,src)
'''    

#先爬三張圖
for each_li in lis[:3]:
    img = each_li.find("img")
    src = img['src'] #圖片網址
    alt = img['alt'] #圖片名稱 書名
    imgRespond = requests.get(src)
    #print(imgRespond) #確認圖片網址是否傳送成功
    #print(imgRespond.content) #.content 顯示二進位的內容
    with open(alt+'.jpg',"wb") as f:
        f.write(imgRespond.content)
    
    
    
    
    
    
    