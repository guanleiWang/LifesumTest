from datetime import time
import time
from datetime import date
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from lifesum_page import MainPage


def eu_signup(browser, emailAddress, password, gender="male", 
              birthday=date(1985,3,24), height=168, weight=60, 
              activityLevel=1.35, goalWeight=50, looseWPWeek=0.25):
    '''This handles the sign up process with eu-unit system'''
    try:
        homePage = MainPage(browser)
        homePage.click_get_started()
        #selenium wait doesn't work well with Chrom, use sleep here
        time.sleep(2)    

        #Select unit name
        unitName = "eu-system"
        homePage.set_unit_name(unitName)
        time.sleep(2)

        #Set user infor: gender, birthday, height, weight
        homePage.set_user_gender(gender)
        homePage.set_user_birthday(birthday)
        homePage.set_height_weight(height, weight)
        homePage.signup_next_step()
        time.sleep(2)
    
        #select activity level
        homePage.set_activity_level(activityLevel)
        homePage.signup_next_step()
        time.sleep(2) 

        #set weight goal and loose weight per week
        homePage.set_weight_goal(goalWeight, looseWPWeek)
        homePage.signup_next_step()
        time.sleep(2)

        #set email and password
        homePage.set_account_infor(emailAddress, password)
        if homePage.signup_submit():
            return 1
    except WebDriverException as e:
        print e
        return 1
      
    return 0

#TODO(guanlei): signup with us-system unit 
#def eu_signup(browser, emailAddress, password, gender="male",
#              birthday=date(1985,3,24), height=168, weight=60,
#              activityLevel=1.35, goalWeight=50, looseWPWeek=0.25):

def login(browser, emailAddress, password):
    loginPage = MainPage(browser)
    loginPage.click_login_link()
    time.sleep(2)

    loginPage.set_login_infor(emailAddress, password)
    login_result = loginPage.click_login_button()
    time.sleep(2)
    if login_result:
        return 1
    return 0

def add_food_to_meal(browser, mealType, foodKeyword):
    mealPage = MainPage(browser)
    mealPage.select_meal_to_add_food(mealType)
    result = mealPage.search_and_add_food(foodKeyword)
    if result:
       return 1
    return 0

def track_weight(browser, weight):
    weightPage = MainPage(browser)
    weightPage.click_me_link()
    time.sleep(2)
    update_weight_result = weightPage.update_weight(weight)
    if update_weight_result:
        return 1
    return 0

def logout(browser):
    try: 
        #Check the user is logined before logout
        logoutPage = MainPage(browser)
        if logoutPage.is_user_loggedin():
            logoutPage.click_logout_button()
        return 0
    except WebDriverException as e:
        #logging.error(e)
        print e
        return 1

