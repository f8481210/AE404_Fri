from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#自動化瀏覽器 > 打開Chrome()
chrome = webdriver.Chrome()
#打開網頁
chrome.get("https://www.google.com.tw/")

time.sleep(0.5)

inputBar = chrome.find_element_by_class_name("gLFyf.gsfi")

inputBar.send_keys("猿創力")
time.sleep(0.5)

#利用Keys直接針對inputbar按下鍵盤Enter
inputBar.send_keys(Keys.ENTER)

time.sleep(0.5)

chrome.find_element_by_partial_link_text("兒童青少年程式").click()

time.sleep(0.5)

chrome.maximize_window()

time.sleep(0.5)
chrome.save_screenshot('猿創力.png')
time.sleep(0.5)
chrome.close()
