#!/usr/bin/python

import MySQLdb as mdb
import sys
import string
import random
import names
from datetime import date, datetime

con = mdb.connect('localhost', 'guanlei', 'Wgl09026', 'lifesum')

with con:
    cur = con.cursor()
    
    i = 0
    while i < 4:
        #Generate random values:
        #Generate firstname and lastname: varchar(50)
        firstname = names.get_first_name()
        if len(firstname) > 50:
            firstname = firstname[0:49]

        lastname = names.get_last_name()
        if len(lastname) > 50:
            lastname = lastname[0:49]

        username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(25))
    
        #password is a random string with a random length of 8 to 128
        size = random.randint(8,128)
        password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))

        #I guess the height is between 0.3 to 2.5m 
        height = random.uniform(0.3, 2.5)
    
        #Generate random age: smallint(6)
        age = random.randint(14,100)
        device = random.choice(('android','online','apple'))

        #Generate random birthdate: date
        year = random.choice(range(1915,2001))
        month = random.choice(range(1,13))
        day = random.choice(range(1,32))
        birthDate = date(year, month, day)

        #Generate last sync time: datetime
        lastsync = datetime.now()

        #insert records to db
        cur.execute("INSERT INTO tbluser(firstname, lastname, username, height, age, password, lastsync, device, birthdate) VALUES(%s,%s,%s,%f,%d,%s,%s,%s,%s)", (firstname,lastname,username,height,age,password,lastsync,device,birthDate))
        i += 1
