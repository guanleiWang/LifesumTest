import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#Click "get started" and select unit name 
def selectUnitName(browser, unitName):
    unitName = "eu-system"
    xpath = "//li[@data-id=\""+unitName+"\"]"
    unit = browser.find_element_by_xpath(xpath)
    unit.click()
    time.sleep(2)

def setUserInfor(browser, gender, birthday, height, weight):
    genderUnit = browser.find_element_by_xpath('//li[@data-id="'+gender+'"]')
    genderUnit.click()

    year = "1992"
    date = "2"
    month = "January"

    yearSelect = Select(browser.find_element_by_id("year"))
    yearSelect.select_by_visible_text(year)

    dateSelect = Select(browser.find_element_by_id("date"))
    dateSelect.select_by_visible_text(date)

    monthSelect = Select(browser.find_element_by_id("month"))
    monthSelect.select_by_visible_text(month)

    heightDiv = browser.find_element_by_xpath('//div[@style="display: block;"]/div[1]/input[1]')
    heightDiv.send_keys(height)

    weightDiv = browser.find_element_by_xpath('//div[@style="display: block;"]/div[2]/input[1]')
    weightDiv.send_keys(weight)

    nextButton = browser.find_element_by_xpath('//button[text()="Next"]')
    nextButton.click()
    time.sleep(2)

def selectActivityLevel(activityLevel):
    activityLi = browser.find_element_by_xpath('//li[@data-id="'+str(activityLevel)+'"]')
    activityLi.click()
    time.sleep(2)

def setGoalWeight(goalWeight, looseWeightPWeek):	
    weightInput = browser.find_element_by_name("looseWeight")
    weightInput.send_keys(goalWeight)

    looseWeightInfoDiv = browser.find_element_by_class_name("loose-weight-info")
#print looseWeightInfoDiv.find_element_by_xpath('.//h4').text
    selectedDiv = looseWeightInfoDiv.find_element_by_xpath('.//div[@style="display: block;"]')
    looseWeightPWeekLi = selectedDiv.find_element_by_xpath('.//li[@data-id="' + looseWeightPWeek+'"]')
    looseWeightPWeekLi.click()

    nextButton = browser.find_element_by_xpath('//button[text()="Next"]')
    nextButton.click()
    time.sleep(2)

def setAccountInfor(emailAddress, password):
    emailInput = browser.find_element_by_id("signup_email")
    passwdInput = browser.find_element_by_id("signup_password")
    emailInput.send_keys(emailAddress)
    passwdInput.send_keys(password)

    agreeCheckbox = browser.find_element_by_name("agreeTos")
    agreeCheckbox.click()

    submitInput = browser.find_element_by_id("postSignup")
    submitInput.click()
    time.sleep(5)

def signup(browser, emailAddress, emailPassword, unitName="eu-system", gender="male", birthday="2002-03-24", height=168, weight=60, activityLevel=1.35, goalWeight=50, looseWPWeek=0.25):
    getStarted = browser.find_element_by_link_text("Get Started")
    getStarted.click()
    time.sleep(2)

    selectUnitName()
    setUserInfor()
    selectActivityLevel()
    setGoalWeight()
    setAccountINfor()

def login(browser, emailAddress, password):


def addFixedFood(browser, type):

def trackWeight(browser, weight):

def logout(browser):
