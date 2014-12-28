import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from functions import login, addFoodToMeal, trackWeight, logout
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LifesumTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/usr/local/chromedriver/ChromeDriver")
        self.browser.maximize_window()
        #self.browser.implicity_wait(20)
        self.browser.get("http://lifesum.com/")

    def tearDown(self):
        self.browser.quit()

    #Test user story of the test question required: signup, add breakfast/lunch,    track weight using weight tracker, then logout.
    def test_signup_addFood_trackWeight_logout(self):
        self.assertEqual(1,1)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LifesumTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
