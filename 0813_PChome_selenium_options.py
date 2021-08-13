from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

#讓瀏覽器執行在背景執行（不讓我們肉眼看得見）
chrome_options = Options() #添加啟動選項
chrome_options.add_argument('--headless') #"--headless" 不顯示視窗
chrome_options.add_argument('--disable-gpu')
chrome = webdriver.Chrome(options=chrome_options)

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

chrome.save_screenshot("google.png")
#商品名稱
for each_prod in soup.find_all('h5',class_="prod_name"):
    productName = each_prod.text
    print(productName)
