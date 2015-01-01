from datetime import time
from datetime import date
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

class BasePage(object):
    'This is the base class for all lifesum web pages.'
    def __init__(self, browser):
        self.browser = browser


class MainPage(BasePage):
    'This class represents the lifesum web pages. This is the only place knows the structure of the web pages, how to handle the elements.'

    '''Attributes'''
    #signup elements
    GET_STARTED_LINK_LOC = (By.LINK_TEXT, "Get Started")
    YEAR_SELECT_LOC = (By.ID, "year")
    DAY_SELECT_LOC = (By.ID, "date")
    MONTH_SELECT_LOC = (By.ID, "month")
    HEIGHT_DIV_LOC = (By.XPATH, '//div[@style="display: block;"]/div[1]/input[1]')
    WEIGHT_DIV_LOC = (By.XPATH, '//div[@style="display: block;"]/div[2]/input[1]')
    NEXT_BUTTON_LOC = (By.XPATH, '//button[text()="Next"]')
    WEIGHT_INPUT_LOC = (By.NAME, "looseWeight")
    LOOSE_WEIGHT_INFO_DIV_LOC = (By.CLASS_NAME, "loose-weight-info")
    SELECTED_DIV_LOC = (By.XPATH, './/div[@style="display: block;"]')
    EMAIL_INPUT_LOC = (By.ID, "signup_email")
    PASSWD_INPUT_LOC = (By.ID, "signup_password")
    AGREE_CHECKBOX_LOC = (By.NAME, "agreeTos")
    SUBMIT_INPUT_LOC = (By.ID, "postSignup")

    #Login elements
    LOGIN_LINK_LOC = (By.LINK_TEXT, "Log in")
    LOGIN_DIV_LOC = (By.XPATH, '//div[@id="login-modal"]')
    EMAIL_INPUT_LOC2 = (By.XPATH, './/input[@id="id_username"]')
    PASSWD_INPUT_LOC2 = (By.XPATH, './/input[@id="id_password"]')
    LOGIN_BUTTON_LOC = (By.XPATH, './/button[@id="loginToWebsite"]')

    #Logout elements
    HEADER_DIV_LOC = (By.CLASS_NAME, "header")
    LOGIN_P_LOC = (By.XPATH, './/p[@class="name"]')
    LOGOUT_LINK_LOC = (By.XPATH, './/a[@id="logout"]')

    #Add food elements
    ADD_MEAL_DIV_LOC = (By.ID, "track_header_dropdown")
    DROPDOWN_ICON_LOC = (By.CLASS_NAME, "dropdown_icon_wrapper")
    SEARCH_INPUT_LOC = (By.ID, "search_field")
    SEARCH_BUTTON_LOC = (By.CLASS_NAME, "search_button")
    RESULT_DIV_LOC = (By.ID, "mCSB_1")

    #Profile and weight tracker elements
    HEADER_DIV_LOC = (By.CLASS_NAME, "header")
    WEIGHT_DIV_LOC2 = (By.ID, "weight-graph")
    WEIGHT_BUTTON_LOC = (By.XPATH,'.//button[1]')
    WEIGHT_INPUT_LOC2 = (By.ID, "trackWeightValue")
    UPDATE_BUTTON_LOC = (By.ID, "trackWeightSubmit")

    def click_get_started(self):
        '''click the "GetStarted" link to sign up'''
        get_started_link = WebDriverWait(self.browser, 10).until(
                         EC.element_to_be_clickable(
                         self.GET_STARTED_LINK_LOC)
                         )
        get_started_link.click()

    def set_unit_name(self, unitName):
        '''select the unit system for measurement'''
        unit = WebDriverWait(self.browser, 10).until(
               EC.presence_of_element_located((By.XPATH, 
               '//li[@data-id="'+unitName+'"]'))
               )
        unit.click()

    def set_user_gender(self, gender):
        '''set user gender'''
        gender_unit = WebDriverWait(self.browser, 10).until(
                     EC.presence_of_element_located((By.XPATH, 
                     '//li[@data-id="'+gender+'"]'))
                     )
        gender_unit = WebDriverWait(self.browser, 10).until(
                     EC.element_to_be_clickable((By.XPATH,
                     '//li[@data-id="'+gender+'"]'))
                     )
        gender_unit.click()

    def set_user_birthday(self, birthday):
        '''set user birthday'''
        year = str(birthday.year)
        year_select = Select(self.browser.find_element(*self.YEAR_SELECT_LOC))
        year_select.select_by_visible_text(year)

        day = str(birthday.day)
        day_select = Select(self.browser.find_element(*self.DAY_SELECT_LOC))
        day_select.select_by_visible_text(day)

        month_index = birthday.month - 1
        month_select = Select(self.browser.find_element(
                      *self.MONTH_SELECT_LOC))
        month_select.select_by_index(month_index)

    def set_height_weight(self, height, weight):
        '''set user height and weight'''
        height_div = self.browser.find_element(*self.HEIGHT_DIV_LOC)
        height_div.send_keys(height)

        weight_div = self.browser.find_element(*self.WEIGHT_DIV_LOC)
        weight_div.send_keys(weight)

    def set_activity_level(self, activityLevel):
        '''set user activity level'''
        activity_li = WebDriverWait(self.browser, 10).until(
                     EC.presence_of_element_located((By.XPATH,'//li[@data-id="'+
                     str(activityLevel)+'"]'))
                     )
        activity_li.click()

    def signup_next_step(self):
        next_button = self.browser.find_element(*self.NEXT_BUTTON_LOC)
        next_button.click()

    def set_weight_goal(self, goalWeight, looseWeightPWeek):
        '''set the goal weight user want'''
        weight_input = WebDriverWait(self.browser, 10).until(
                      EC.presence_of_element_located(self.WEIGHT_INPUT_LOC)
                      )
        weight_input.send_keys(goalWeight)

        loose_weight_info_div = self.browser.find_element(
                             *self.LOOSE_WEIGHT_INFO_DIV_LOC)
        selected_div = loose_weight_info_div.find_element(*self.SELECTED_DIV_LOC)
        loose_weight_week_li = selected_div.find_element_by_xpath(
                             './/li[@data-id="' + str(looseWeightPWeek)+'"]')
        loose_weight_week_li.click()

    def set_account_infor(self, emailAddress, password):
        '''set user email and password for the new account'''
        email_input = self.browser.find_element(*self.EMAIL_INPUT_LOC)
        passwd_input = self.browser.find_element(*self.PASSWD_INPUT_LOC)
        email_input.send_keys(emailAddress)
        passwd_input.send_keys(password)
        
        agree_checkbox = self.browser.find_element(*self.AGREE_CHECKBOX_LOC)
        agree_checkbox.click()
    
    def is_user_loggedin(self):
        '''check whether user is logged in'''
        try:
            header_div = self.browser.find_element(*self.HEADER_DIV_LOC)
            login_p = header_div.find_element(*self.LOGIN_P_LOC)
            if login_p.text == "Logged in":
                return True
            else:
                return False
        except NoSuchElementException as e:
            return False
        except ElementNotVisibleException as e1:
            return False

    def signup_submit(self):
        '''The last step for signup. Need to check signup is succeed or hit some issue        '''
        submit_input = self.browser.find_element(*self.SUBMIT_INPUT_LOC)
        submit_input.click()
        time.sleep(10)

        if self.is_user_loggedin():
            return 0
        else:
            signup_modal = self.browser.find_element_by_id("signup-modal")
            modal_body = signup_modal.find_element_by_xpath(\
                     './/div[@class="modal-body"]')
            user_exist_error_div = modal_body.find_element_by_xpath('.//div[1]')
            if user_exist_error_div.get_attribute("style") == "display: block;":
               print user_exist_error_div.text
               return 1
            return 0

    def click_login_link(self):
        login_link = self.browser.find_element(*self.LOGIN_LINK_LOC)
        login_link.click()

    def set_login_infor(self, emailAddress, password):
        '''Input login information'''
        login_div = self.browser.find_element(*self.LOGIN_DIV_LOC)
        email_input = login_div.find_element(*self.EMAIL_INPUT_LOC2)
        passwd_input = login_div.find_element(*self.PASSWD_INPUT_LOC2)

        email_input.send_keys(emailAddress)
        passwd_input.send_keys(password)

    def click_login_button(self):
        '''last step for login: need to check login succeed or hit issue'''
        login_div = self.browser.find_element(*self.LOGIN_DIV_LOC)
        login_button = login_div.find_element(*self.LOGIN_BUTTON_LOC)
        login_button.click()
   
        modal_content = login_div.find_element_by_class_name("modal-content")
        error_message_div = modal_content.find_element_by_xpath('.//div[2]')
        if error_message_div.get_attribute("style") == "display: block;":
            print "Invalid Email or Password!"
            return 1
        return 0
        

    def click_logout_button(self):
        '''logout'''
        header_div = self.browser.find_element(*self.HEADER_DIV_LOC)
        login_p = header_div.find_element(*self.LOGIN_P_LOC)
        login_p.click()
        time.sleep(1)
        logout_link = header_div.find_element(*self.LOGOUT_LINK_LOC)
        logout_link.click()

    def select_meal_to_add_food(self, mealType):
        '''Select the meal type to add food: breakfast, lunch, dinner...'''
        add_meal_div = self.browser.find_element(*self.ADD_MEAL_DIV_LOC)
        dropdown_icon = add_meal_div.find_element(*self.DROPDOWN_ICON_LOC)
        dropdown_icon.click()
        time.sleep(1)

        meal = {"breakfast":1, "lunch":2, "dinner":3, "snack":4, "exercise":5}
        i = str(meal[mealType])
        meal_li = add_meal_div.find_element_by_xpath('.//li[@data-mealtime="'
                 +i+'"]')
        meal_li.click()
        time.sleep(2)

    def search_and_add_food(self, foodKeyword):
        '''Search the keyword, then add the first returned food into the meal.'''
        try:
            search_input = self.browser.find_element(*self.SEARCH_INPUT_LOC)
            search_input.clear()
            search_input.send_keys(foodKeyword)
            search_button = self.browser.find_element(*self.SEARCH_BUTTON_LOC)
            search_button.click()
            time.sleep(3)

            result_div = self.browser.find_element(*self.RESULT_DIV_LOC)
            first_li = result_div.find_element_by_xpath('.//li[1]')
            add_button = first_li.find_element_by_xpath('.//button[1]')
            add_button.click()
            time.sleep(10)
  
            return 0
        except WebDriverException as e:
            return 1   
 
    def click_me_link(self):
        header_div = self.browser.find_element(*self.HEADER_DIV_LOC)
        me_link = header_div.find_element_by_xpath(".//li[2]")
        me_link.click()

    def update_weight(self, weight):
        '''update user weight using weight tracker'''
        try:
            weight_div = self.browser.find_element(*self.WEIGHT_DIV_LOC2)
            weight_button = weight_div.find_element(*self.WEIGHT_BUTTON_LOC)
            weight_button.click()
            time.sleep(2)

            #wait and assert
            weight_input = self.browser.find_element(*self.WEIGHT_INPUT_LOC2)
            weight_input.send_keys(weight)

            update_button = self.browser.find_element(*self.UPDATE_BUTTON_LOC)
            update_button.click()
            time.sleep(2)

            return 0
        except WebDriverException as e:
            return 1   
