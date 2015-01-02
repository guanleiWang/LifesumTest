1. Description 
   These scripts are to test lifesum website functionalities like: login, sign up, add food, track weight. Python(2.7.6) and selenium(2.44) are used for implementation. The target web browser is Chrome.

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

3. Design pattern: Page Object Model and Python modular programming
   lifesum_test.py - the main script to launch the test cases and report test result.It calls functions from operations.py.
   operations.py   - a library for common functions like: login, sign up...
   lifesum_page.py - the only place knowing the structure of the lifesum web page, it provides basic functionalities to operations.py.

4. Test cases: 
   Totally there are 3 test cases in lifesum_test.py currently.
Case 1 - test_signup_logout_case1
    To test the new user sign up process, and then logout after sign up.
Case 2 - test_login_add_food_logout_case1:
    To test existing user login, add food to  breakfast and lunch, then logout.
Case 3 - test_login_track_weight_logout_case1:
    To test existing user login, update weight with weight tracker, then logout.

5. How to run:
   #python lifesum_test.py
   It will execute 3 test cases and report test result like:
"
test_login_add_food_logout_case1 (__main__.LifesumTest) ... ok
test_login_track_weight_logout_case1 (__main__.LifesumTest) ... ok
test_signup_logout_case1 (__main__.LifesumTest) ... ok

----------------------------------------------------------------------
Ran 3 tests in 159.399s

OK
"

####################
   NOTE: Test case - test_signup_logout_case1, which is used to test the new user sign up process, a new email address is needed every time it was run. So after the first run,if you want to continue running, please remove the user from backend database or modify line 17 of lifesum_test.py to provide a new email address. Or error message may received because of user already existed.

   NOTE: I added a video file examples.ogv recorded by ubuntu recordMyDesktop to show the running of the test cases. If you can't play it on ubuntu, please run #sudo apt-get install gtk-recordmydesktop to install the software.
####################

6. What can be done in the future
1). Implement more detailed and visual logs and reports
2). Organize test cases with Suite
3). Add more test cases
4). Implement data driven testing model
5). Write a script to automate the env setup
 
7. Framework selection:
Besides the commercial web automation testing tools like heliumhq, ranorex, QTP and so on, selenium, sikuli and watir are the three most popular open-source web automation testing framework. Selenium is a one of the efficient open-source automated testing tool which provide a nice testing framework for testing wide variety of web application. Sikuli is one tool that uses images to generate test cases and automate testing for the application under consideratioin. Watir is a set of open source Ruby libraries released under BSD license to test the various web based applications. I choose selenium finally because of its advantages like:
1). Similar to sikuli, selenium provides an IDE, a firefox add-on can do simple record-and-playback of interactioins with the browser.
2). Selenium also provides Selenium WebDriver, a collection of language specific bindings to drive a browser. It can create robust, browser-based regression automation scripts. I use this feature to write the test cases.
3). Selenium supports many operating systems and browsers. It supports Windows, Linux and Apple OS X. It supports browsers like firefox, Chrome, IE, Safari and Opera. So it can test different browser support for lifesume.com.
4). Selenium supports many programming languages and testing frameworks. It supports Java and JUnit & TestNG frameworks; It supports Python and unittest, py.test & robot frameworks; It also support C#, Perl, Ruby and other languagues and frameworks. So its easy to pick up a familiar programming language and testing framework, and integrate the automation scripts into CI environment.
5). Selenium also provides an advanced feature called Grid. It can scale and distribute scripts across many environments. So if the automation testing cost much time to run, we can empower this feature to distribute the testing to improve efficiency.
6). Selenium is the choice for most companies currently, the support documentation and materials are substantial.

8. Reference:
1). Selenium: www.seleniumhq.org
2). Sikuli: www.sikuli.org
3). Watir: watir.com

