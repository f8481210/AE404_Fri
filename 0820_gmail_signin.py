from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome = webdriver.Chrome()
chrome.get("https://www.google.com.tw/")
chrome.find_element_by_link_text("Gmail").click()
time.sleep(1)
chrome.find_element_by_link_text("Sign in").click()

inputBar = chrome.find_element_by_class_name("whsOnd.zHQkBf")
inputBar.send_keys("codingape@gmail.com")
inputBar.send_keys(Keys.ENTER)



