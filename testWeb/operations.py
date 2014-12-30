import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lifesum_page import MainPage



def signup(browser, emailAddress, password, unitName="eu-system", gender="male", birthday=date(1985,3,24), height=168, weight=60, activityLevel=1.35, goalWeight=50, looseWPWeek=0.25):
    homePage = MainPage(browser)
    homePage.clickGetStarted()
    time.sleep(2)
    
    #Select unit name
    homePage.setUnitName(unitName)
    time.sleep(2)

    #Set user infor: gender, birthday, height, weight
    homePage.setUserGender(gender)
    homePage.setUserBirthday(birthday)
    homePage.setHeightWeight(height, weight)
    homePage.signupNextStep()
    time.sleep(2)
    #select activity level
    homePage.setActivityLevel(activityLevel)
    homePage.signupNextStep()
    time.sleep(2)

    #set weight goal and loose weight per week
    homePage.setWeightGoal(goalWeight, looseWPWeek)
    homePage.signupNextStep()
    time.sleep(2)

    #set email and password
    homePage.setAccountInfor(emailAddress, password)
#    homePage.signupSubmit()


def login(browser, emailAddress, password):
    loginPage = MainPage(browser)
    loginPage.clickLoginLink()
    time.sleep(1)

    loginPage.setLoginInfor(emailAddress, password)
    loginPage.clickLoginButton()
    time.sleep(2)

def addFoodToMeal(browser, mealType, foodKeyword):
    mealPage = MainPage(browser)
    mealPage.selectMealToAddFood(mealType)
    mealPage.searchAndAddFood(foodKeyword)
    time.sleep(5)
   # try:
   #     print "call addFoodToMeal"
        #Select "Add xxx" according to the meal type: breakfast, lunch...
   #     addMealDiv = WebDriverWait(browser, 10).until(
   #     EC.presence_of_element_located((By.ID, "track_header_dropdown"))
   #     )
   #     print "find addMealDiv"
   
    #finally:
     #   return -1

def trackWeight(browser, weight):
    weightPage = MainPage(browser)
    weightPage.clickMeLink()
    weightPage.updateWeight(weight)

def logout(browser):
    #Check the user is logined before logout
    logoutPage = MainPage(browser)
    if logoutPage.isUserLoggedin():
        logoutPage.clickLogoutButton()
 
