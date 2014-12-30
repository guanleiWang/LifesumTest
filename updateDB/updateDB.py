#!/usr/bin/python

import MySQLdb as mdb
import sys, getopt
import string
import random
import names
from datetime import date, datetime,timedelta

def randomDate(start, end):
    delta = end - start
    int_delta = (delta.days *24*60*60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds = random_second)

def updateTable(host, user, passwd, database):
    con = mdb.connect(host,user,passwd,database)

    with con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) from tbluser")
        result = str(cur.fetchone())
        originalRowCount = int(result[1:-3])
        print "Table tbluser has "+ str(originalRowCount)+ " records."    

        i = 0
        while i < 1000:
            #Generate random values:
            #Generate random firstname and lastname from names module: varchar(50)
            firstname = names.get_first_name()
            if len(firstname) > 50:
                firstname = firstname[0:49]
            firstnameStr = '"' + firstname + '"'

            lastname = names.get_last_name()
            if len(lastname) > 50:
                lastname = lastname[0:49]
            lastnameStr = '"' + lastname + '"'

            #Generate random unique username(a string containing letters and digits,lenght is 25 chars): varchar(25)
            username = ''.join(random.choice(string.ascii_letters + string.digits)\
                       for _ in range(25))
            usernameStr = '"' + username + '"'
    
            #Generate random password(a string containing letters and digits,with a random length of 8 to 12):varchar(128)
            size = random.randint(8,12)
            password = ''.join(random.choice(string.ascii_letters + string.digits)\
                       for _ in range(size))
            passwordStr = '"' + password + '"'

            #Generate person height: random value between 50 to 250cm maybe: double 
            height = random.uniform(50,250)
    
            #Generate random birthdate: date between 1915-1-1 and 2000-12-31 (according to lifesum signup page)
            startDate = date(1915,1,1)
            endDate = date(2000,12,31)
            birthDate = randomDate(startDate, endDate)
            birthDateStr = '"' + datetime.strftime(birthDate,'%Y-%m-%d') + '"'

            #Calculate age from birthDate
            today = date.today()
            age = today.year - birthDate.year - ((today.month, today.day) \
                  < (birthDate.month, birthDate.day))

            #Generate random last sync time: datetime between 2008-1-1 0:0:0 to now
            startTime = datetime.strptime('1/1/2008 0:0:0', '%m/%d/%Y %H:%M:%S')
            now = datetime.strftime(datetime.now(),'%m/%d/%Y %H:%M:%S')
            endTime = datetime.strptime(now, '%m/%d/%Y %H:%M:%S')
            lastsync = randomDate(startTime, endTime)
            lastsyncStr = '"'+datetime.strftime(lastsync, '%Y-%m-%d %H:%M:%S')+'"'

            #Generate random device from enum
            device = random.choice(('android','online','apple'))
            deviceStr = '"' + device + '"'

            #insert records to db
            cur.execute("INSERT INTO tbluser(firstname, lastname, username, height,\
                    age, password, lastsync, device, birthdate) VALUES(%s,%s,\
                    %s,%.2f,%i,%s,%s,%s,%s)" %(firstnameStr,lastnameStr,\
                    usernameStr, height,age,passwordStr,lastsyncStr,\
                    deviceStr,birthDateStr))
            i += 1

        cur.execute("SELECT COUNT(*) from tbluser")
        result = str(cur.fetchone())
        currentRowCount = int(result[1:-3])
        print "Table tbluser has "+str(currentRowCount)+ " records now."

        if currentRowCount - originalRowCount == 1000:
            print "Insert 1000 random records successed!"
        else:
            print "Insert 1000 random records failed! Please check!"

def printTimeCost(start, end):
    timeDelta = end - start
    timeCost = (timeDelta.days *24*60*60) + timeDelta.seconds

    print ("The operation cost " + str(timeCost) + " seconds")

def main(argv):
    server = ''
    user = ''
    passwd = ''
    db = ''
  
    try:
        opts,args = getopt.getopt(argv, "hs:u:p:d:")
    except getopt.GetoptError:
        print 'Invalid option. Please use this follow:'
        print 'updateDB.py -s <DB server>, -u <user>, -p <password>, -d <database>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'updateDB.py -s <DB server>, -u <user>, -p <password>,-d <database>'
            sys.exit()
        elif opt == '-s':
            server = arg
        elif opt == '-u':
            user = arg
        elif opt == '-p':
            passwd = arg
        elif opt == '-d':
            db = arg

    start1 = datetime.now()

    updateTable(server, user, passwd, db)
    
    end1 = datetime.now()
    printTimeCost(start1, end1)

if __name__ == "__main__":
    main(sys.argv[1:])
