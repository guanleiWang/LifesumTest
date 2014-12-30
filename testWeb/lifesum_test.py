import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest
from operations import signup, login, logout, addFoodToMeal, trackWeight

class LifesumTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/usr/local/chromedriver/ChromeDriver")
        self.browser.maximize_window()
        #self.browser.implicity_wait(20)
        self.browser.get("http://lifesum.com/")

    def tearDown(self):
        self.browser.quit()

    def test_signup_logout_case1(self):
        signup(self.browser, "testquestions123456@gmail.com","wgl010209")
        logout()

    def test_login_add_food_logout_case1(self):
        login(self.browser, "wangguanlei.buaa@gmail.com","Wgl09026")
        addFoodToMeal(self.browser, "breakfast", "bread")
        addFoodToMeal(self.browser, "lunch", "fish")
        logout(self.browser)

    def test_login_track_weight_logout_case1(self):
        login(self.browser, "wangguanlei.buaa@gmail.com","Wgl09026")
        trackWeight(self.browser, 53)
        logout(self.browser)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LifesumTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
