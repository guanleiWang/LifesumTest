#!/usr/bin/python

from selenium import webdriver
import unittest
from operations import eu_signup, login, logout, add_food_to_meal, track_weight

class LifesumTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/usr/local/chromedriver/ChromeDriver")
        self.browser.maximize_window()
        self.browser.get("http://lifesum.com/")

    def tearDown(self):
        self.browser.quit()

    def test_signup_logout_case1(self):
        result_signup = eu_signup(self.browser, "wally1109test09861@gmail.com",
                        "wgl010209")
        if result_signup:
            self.fail("Can't sign up successfully!")
 
        result_logout = logout(self.browser)

        if result_logout:
            self.fail("Can't logout after sign up!")

        pass

    def test_login_add_food_logout_case1(self):
        login_result = login(self.browser, "wangguanlei.buaa@gmail.com",
                       "Wgl09026")
        if login_result:
            self.fail("Unable to login!")

        add_breakfast_result = add_food_to_meal(self.browser, "breakfast", "bread")
        if add_breakfast_result:
            self.fail("Add breakfast failed!")

        add_lunch_result = add_food_to_meal(self.browser, "lunch", "fish")
        if add_lunch_result:
            self.fail("Add lunch failed!")

        result_logout = logout(self.browser)

        if result_logout:
            self.fail("Can't logout after add breakfast and lunch!")

        pass

    def test_login_track_weight_logout_case1(self):
        login_result = login(self.browser, "wangguanlei.buaa@gmail.com",
                       "Wgl09026")
        if login_result:
            self.fail("Unable to login!")

        update_weight_result = track_weight(self.browser, 53)
        if update_weight_result:
            self.fail("Track weight failed!") 

        result_logout = logout(self.browser)
        if result_logout:
            self.fail("Can't logout after update weight!")

        pass

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LifesumTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
