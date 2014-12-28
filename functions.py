import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    loginLink = browser.find_element_by_link_text("Log in")
    loginLink.click()
    time.sleep(1)

    loginDiv = browser.find_element_by_xpath('//div[@id="login-modal"]')
    emailInput = loginDiv.find_element_by_xpath('.//input[@id="id_username"]')
    passwdInput = loginDiv.find_element_by_xpath('.//input[@id="id_password"]')
   
    emailInput.send_keys(emailAddress)
    passwdInput.send_keys(password)

    loginButton = loginDiv.find_element_by_xpath('.//button[@id="loginToWebsite"]')
    loginButton.click()
    time.sleep(2)

def addFoodToMeal(browser, mealType, foodKeyword):
   # try:
        print "call addFoodToMeal"
        #Select "Add xxx" according to the meal type: breakfast, lunch...
        addMealDiv = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "track_header_dropdown"))
        )
        print "find addMealDiv"
    
        dropdownIcon = addMealDiv.find_element_by_class_name("dropdown_icon_wrapper")
        dropdownIcon.click()

        meal = {"breakfast":1, "lunch":2, "dinner":3, "snack":4, "exercise":5}
        i = meal[mealType]
        mealLi = addMealDiv.find_element_by_xpath('.//li[2]')
        mealLi.click()
        print "select lunch"

        #Search for food "bread"
        searchInput = browser.find_element_by_id("search_field")
        searchInput.send_keys(foodKeyword)
        searchButton = browser.find_element_by_class_name("search_button")
        searchButton.click()
        print "search for keyword"        

        #Add the first returned result food into meal
        resultDiv = browser.find_element_by_id("mCSB_1")
        time.sleep(10)
        firstLi = resultDiv.find_element_by_xpath('.//li[1]')
        addButton = firstLi.find_element_by_xpath('.//button[1]')
        addButton.click()
        print "add food"
        time.sleep(20)
        #Add food to meal

        return 0
    #finally:
     #   return -1

def trackWeight(browser, weight):
    time.sleep(10)
    #print browser.page_source
    headerDiv = browser.find_element_by_class_name("header")
    meLink = headerDiv.find_element_by_xpath(".//li[2]")
    meLink.click()
    time.sleep(5)
    
    weightDiv = browser.find_element_by_id("weight-graph")
    weightButton = weightDiv.find_element_by_xpath('.//button[1]')
    weightButton.click()
    time.sleep(5)
  
    #wait and assert
    weightInput = browser.find_element_by_id("trackWeightValue")
    weightInput.send_keys(weight)

    updateButton = browser.find_element_by_id("trackWeightSubmit")
    updateButton.click()


def logout(browser):
    #Check the user is logined before logout
    headerDiv = browser.find_element_by_class_name("header")
    loginP = headerDiv.find_element_by_xpath('.//p[@class="name"]')
    if loginP.text == "Logged in":
        loginP.click()
        logoutLink = headerDiv.find_element_by_xpath('.//a[@id="logout"]')
        logoutLink.click()
