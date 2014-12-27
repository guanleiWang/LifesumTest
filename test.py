import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from functions import login, addFixedFood
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("/usr/local/chromedriver/ChromeDriver")
browser.maximize_window()
browser.get("http://lifesum.com/")

#Wait until the "Get started" link is available
#signup

login(browser, "wangguanlei.buaa@gmail.com", "Wgl09026")

result = addFixedFood(browser, "lunch")
print "added meal!"



browser.quit()
