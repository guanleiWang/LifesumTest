import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, browser):
        self.browser = browser


class MainPage(BasePage):

    #signup elements
    getStartedLinkLocator = (By.LINK_TEXT, "Get Started")
    yearSelectLocator = (By.ID, "year")
    daySelectLocator = (By.ID, "date")
    monthSelectLocator = (By.ID, "month")
    heightDivLocator = (By.XPATH, '//div[@style="display: block;"]/div[1]/input[1]')
    weightDivLocator = (By.XPATH, '//div[@style="display: block;"]/div[2]/input[1]')
    nextButtonLocator = (By.XPATH, '//button[text()="Next"]')
    weightInputLocator = (By.NAME, "looseWeight")
    looseWeightInfoDivLocator = (By.CLASS_NAME, "loose-weight-info")
    selectedDivLocator = (By.XPATH, './/div[@style="display: block;"]')
    emailInputLocator = (By.ID, "signup_email")
    passwdInputLocator = (By.ID, "signup_password")
    agreeCheckboxLocator = (By.NAME, "agreeTos")
    submitInputLocator = (By.ID, "postSignup")

    #Login elements
    loginLinkLocator = (By.LINK_TEXT, "Log in")
    loginDivLocator = (By.XPATH, '//div[@id="login-modal"]')
    emailInputLocator = (By.XPATH, './/input[@id="id_username"]')
    passwdInputLocator = (By.XPATH, './/input[@id="id_password"]')
    loginButtonLocator = (By.XPATH, './/button[@id="loginToWebsite"]')

    #Logout elements
    headerDivLocator = (By.CLASS_NAME, "header")
    loginPLocator = (By.XPATH, './/p[@class="name"]')
    logoutLinkLocator = (By.XPATH, './/a[@id="logout"]')

    #Add food elements
    addMealDivLocator = (By.ID, "track_header_dropdown")
    dropdownIconLocator = (By.CLASS_NAME, "dropdown_icon_wrapper")
    searchInputLocator = (By.ID, "search_field")
    searchButtonLocator = (By.CLASS_NAME, "search_button")
    resultDivLocator = (By.ID, "mCSB_1")

    #Profile and weight tracker elements
    headerDivLocator = (By.CLASS_NAME, "header")
    weightDivLocator = (By.ID, "weight-graph")
    weightButtonLocator = (By.XPATH,'.//button[1]')
    weightInputLocator = (By.ID, "trackWeightValue")
    updateButtonLocator = (By.ID, "trackWeightSubmit")

    def clickGetStarted(self):
        getStartedLink = self.browser.find_element(*MainPage.getStartedLinkLocator)
        getStartedLink.click()

    def setUnitName(self, unitName):
        unit = self.browser.find_element(By.XPATH, '//li[@data-id="'+unitName+'"]')
        unit.click()

    def setUserGender(self, gender):
        #set user gender
        genderUnit = self.browser.find_element(By.XPATH, '//li[@data-id="'+gender+'"]')
        genderUnit.click()

    def setUserBirthday(self, birthday):
        #set user birthday
        year = str(birthday.year)
        yearSelect = Select(self.browser.find_element(*self.yearSelectLocator))
        yearSelect.select_by_visible_text(year)

        day = str(birthday.day)
        daySelect = Select(self.browser.find_element(*self.daySelectLocator))
        daySelect.select_by_visible_text(day)

        month_index = birthday.month - 1
        monthSelect = Select(self.browser.find_element(*self.monthSelectLocator))
        monthSelect.select_by_index(month_index)

    def setHeightWeight(self, height, weight):
        heightDiv = self.browser.find_element(*self.heightDivLocator)
        heightDiv.send_keys(height)

        weightDiv = self.browser.find_element(*self.weightDivLocator)
        weightDiv.send_keys(weight)

    def setActivityLevel(self, activityLevel):
        activityLi = self.browser.find_element_by_xpath('//li[@data-id="'+str(activityLevel)+'"]')
        activityLi.click()

    def signupNextStep(self):
        nextButton = self.browser.find_element(*self.nextButtonLocator)
        nextButton.click()

    def setWeightGoal(self, goalWeight, looseWeightPWeek):
        weightInput = self.browser.find_element(*self.weightInputLocator)
        weightInput.send_keys(goalWeight)

        looseWeightInfoDiv = self.browser.find_element(*self.looseWeightInfoDivLocator)
        selectedDiv = looseWeightInfoDiv.find_element(*self.selectedDivLocator)
        looseWeightPWeekLi = selectedDiv.find_element_by_xpath('.//li[@data-id=                             "' + str(looseWeightPWeek)+'"]')
        looseWeightPWeekLi.click()

        #signupNextStep(self)

    def setAccountInfor(self, emailAddress, password):
        emailInput = self.browser.find_element(*self.emailInputLocator)
        passwdInput = self.browser.find_element(*self.passwdInputLocator)
        emailInput.send_keys(emailAddress)
        passwdInput.send_keys(password)
        
        agreeCheckbox = self.browser.find_element(*self.agreeCheckboxLocator)
        agreeCheckbox.click()
    
    def signupSubmit():
        submitInput = self.browser.find_element(*self.submitInputLocator)
        submitInput.click()

    def clickLoginLink(self):
        loginLink = self.browser.find_element(*self.loginLinkLocator)
        loginLink.click()

    def setLoginInfor(self, emailAddress, password):
        loginDiv = self.browser.find_element(*self.loginDivLocator)
        emailInput = loginDiv.find_element(*self.emailInputLocator)
        passwdInput = loginDiv.find_element(*self.passwdInputLocator)

        emailInput.send_keys(emailAddress)
        passwdInput.send_keys(password)

    def clickLoginButton(self):
        loginDiv = self.browser.find_element(*self.loginDivLocator)
        loginButton = loginDiv.find_element(*self.loginButtonLocator)
        loginButton.click()

    def isUserLoggedin(self):
        headerDiv = self.browser.find_element(*self.headerDivLocator)
        loginP = headerDiv.find_element(*self.loginPLocator)
        if loginP.text == "Logged in":
            return True
        else:
            return False

    def clickLogoutButton(self):
        headerDiv = self.browser.find_element(*self.headerDivLocator)
        loginP = headerDiv.find_element(*self.loginPLocator)
        loginP.click()
        logoutLink = headerDiv.find_element(*self.logoutLinkLocator)
        logoutLink.click()

    def selectMealToAddFood(self, mealType):
        addMealDiv = self.browser.find_element(*self.addMealDivLocator)
        dropdownIcon = addMealDiv.find_element(*self.dropdownIconLocator)
        dropdownIcon.click()

        meal = {"breakfast":1, "lunch":2, "dinner":3, "snack":4, "exercise":5}
        i = str(meal[mealType])
        print i
        mealLi = addMealDiv.find_element_by_xpath('.//li[@data-mealtime="'+i+'"]')
        mealLi.click()

    def searchAndAddFood(self, foodKeyword):
        searchInput = self.browser.find_element(*self.searchInputLocator)
        searchInput.clear()
        searchInput.send_keys(foodKeyword)
        searchButton = self.browser.find_element(*self.searchButtonLocator)
        searchButton.click()

        resultDiv = self.browser.find_element(*self.resultDivLocator)
        time.sleep(5)
        firstLi = resultDiv.find_element_by_xpath('.//li[1]')
        addButton = firstLi.find_element_by_xpath('.//button[1]')
        addButton.click()

 
    def clickMeLink(self):
        headerDiv = self.browser.find_element(*self.headerDivLocator)
        meLink = headerDiv.find_element_by_xpath(".//li[2]")
        meLink.click()

    def updateWeight(self, weight):
        weightDiv = self.browser.find_element(*self.weightDivLocator)
        weightButton = weightDiv.find_element(*self.weightButtonLocator)
        weightButton.click()

        #wait and assert
        weightInput = self.browser.find_element(*self.weightInputLocator)
        weightInput.send_keys(weight)

        updateButton = self.browser.find_element(*self.updateButtonLocator)
        updateButton.click()
