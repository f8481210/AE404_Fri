'''
題目：使用selenium，取得商品名稱。
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import time
#開啟瀏覽器視窗(chrome)
chrome = webdriver.Chrome()

#前往網頁 > 搜尋apple的產品
chrome.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=apple")

#讓程式休息三秒 網頁會延遲一下 確保資料有載入
time.sleep(3)

#讓游標往下移
for i in range(2):
    chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)

#page_source 讀取網頁原始碼
soup = BeautifulSoup(chrome.page_source,"html.parser")

#商品名稱
for each_prod in soup.find_all('h5',class_="prod_name"):
    productName = each_prod.text
    print(productName)

#關閉網頁
chrome.close()
