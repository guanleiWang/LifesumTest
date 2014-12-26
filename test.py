import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome("/usr/local/chromedriver/ChromeDriver")
browser.get("http://lifesum.com/")
time.sleep(5)
#assert title of the page

#get started function
getStarted = browser.find_element_by_link_text("Get Started")
getStarted.click()
time.sleep(2)
unitName = "eu-system"
xpath = "//li[@data-id=\""+unitName+"\"]"
unit = browser.find_element_by_xpath(xpath)
unit.click()
time.sleep(2)

#Page 2: select sex
gender = "male"

genderUnit = browser.find_element_by_xpath('//li[@data-id="'+gender+'"]')
genderUnit.click()

#check genderUnit.class = selected

#set birthday
year = "1992"
date = "2"
month = "January"

yearSelect = Select(browser.find_element_by_id("year"))
yearSelect.select_by_visible_text(year)

dateSelect = Select(browser.find_element_by_id("date"))
dateSelect.select_by_visible_text(date)

monthSelect = Select(browser.find_element_by_id("month"))
monthSelect.select_by_visible_text(month)

#set height and weight
height = 168
weight = 55
#UserInforDivOne = browser.find_element_by_class("signup-form-section user-info")[0]
heightDiv = browser.find_element_by_xpath('//div[@style="display: block;"]/div[1]/input[1]')
heightDiv.send_keys(height)

weightDiv = browser.find_element_by_xpath('//div[@style="display: block;"]/div[2]/input[1]')
weightDiv.send_keys(weight)

nextButton = browser.find_element_by_xpath('//button[text()="Next"]')
nextButton.click()
time.sleep(2)

#Page 3:
activityLevel = 1.35
activityLi = browser.find_element_by_xpath('//li[@data-id="'+str(activityLevel)+'"]')
activityLi.click()
time.sleep(2)

#Page 4:
goalWeight = 45
weightInput = browser.find_element_by_name("looseWeight")
weightInput.send_keys(goalWeight)

looseWeightPWeek = "0.75"
looseWeightInfoDiv = browser.find_element_by_class_name("loose-weight-info")
#print looseWeightInfoDiv.find_element_by_xpath('.//h4').text
selectedDiv = looseWeightInfoDiv.find_element_by_xpath('.//div[@style="display: block;"]')
looseWeightPWeekLi = selectedDiv.find_element_by_xpath('.//li[@data-id="' + looseWeightPWeek+'"]')
looseWeightPWeekLi.click()

nextButton = browser.find_element_by_xpath('//button[text()="Next"]')
nextButton.click()
time.sleep(2)

#Page 5:
emailAddress = "1234hello123456@gmail.com"
password = "Test0102"
emailInput = browser.find_element_by_id("signup_email")
passwdInput = browser.find_element_by_id("signup_password")
emailInput.send_keys(emailAddress)
passwdInput.send_keys(password)

agreeCheckbox = browser.find_element_by_name("agreeTos")
agreeCheckbox.click()

submitInput = browser.find_element_by_id("postSignup")
submitInput.click()
time.sleep(5)

#browser.quit()
