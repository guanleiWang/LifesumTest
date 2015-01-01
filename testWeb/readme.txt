1. Description: These scripts are used to test lifesum website functionalities like: login, sign up, add food, track weight. They are implemented with Python(2.7.6), selenium(2.44) and unittest. I ran these test with Chrome browser.

2. Environment setup(for ubuntu 14.04 desktop edition):
1). Install python pip, run:
    sudo apt-get install python-pip

2). Install selenium, run:
    sudo pip install selenium

3). Install Google Chrome, run:
    sudo apt-get install google-chrome-stable

4). Install Chrome driver for selenium:
    a. Go to chromedriver.storage.googleapis.com/index.html
    b. Select sub folder: 2.13
    c. Download chromedriver_linux64.zip
    D. Unzip the package into folder: /usr/local/chromedriver/, run:
       unzip chromedriver_linux64.zip -d /usr/local/chromedriver

3. Files description:
   lifesum_test.py is the main script to launch the test cases and report test result.
   operations.py is a library for common functions like: login, sign up...
   lifesum_page.py is the only place knowing the structure of the lifesum web page.
   These was designed according to the Page Object Model used in selenium.

4. How to run:
   #python lifesum_test.py
   It will execute 3 test cases within unittest framework and report test result like:
"
test_login_add_food_logout_case1 (__main__.LifesumTest) ... ok
test_login_track_weight_logout_case1 (__main__.LifesumTest) ... ok
test_signup_logout_case1 (__main__.LifesumTest) ... ok

----------------------------------------------------------------------
Ran 3 tests in 159.399s

OK
"

5. Please note:
   For test case: test_signup_logout_case1, which is used to test the new user sign up process, a new email address is needed every time it was run. So after the first run,if you want to continue running, please remove the user from backend database or modify line 17 of lifesum_test.py to provide a new email address. Or error message may received because of user already existed.

Thanks!
