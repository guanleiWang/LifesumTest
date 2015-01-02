#!/usr/bin/python

import MySQLdb as mdb
import sys, getopt
import string
import random
import names
from datetime import date, datetime,timedelta

def random_date(start, end):
    #Generate a random date between start and end
    delta = end - start
    int_delta = (delta.days *24*60*60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds = random_second)

def update_table(host, user, passwd, database):
    #Get a connection to MySQL db
    con = mdb.connect(host,user,passwd,database)

    with con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) from tbluser")
        result = str(cur.fetchone())
        original_row_count = int(result[1:-3])
        print "Table tbluser has "+ str(original_row_count)+ " records."    

        i = 0
        while i < 1000:
            #Generate random values:
            #Generate random firstname and lastname from names module: varchar(50)
            firstname = names.get_first_name()
            if len(firstname) > 50:
                firstname = firstname[0:49]
            firstname_str = '"' + firstname + '"'

            lastname = names.get_last_name()
            if len(lastname) > 50:
                lastname = lastname[0:49]
            lastname_str = '"' + lastname + '"'

            #Generate random unique username(a string containing letters and digits,lenght is 25 chars): varchar(25)
            username = ''.join(random.choice(string.ascii_letters + string.digits)\
                       for _ in range(25))
            username_str = '"' + username + '"'
    
            #Generate random password(a string containing letters and digits,with a random length of 8 to 12):varchar(128)
            size = random.randint(8,12)
            password = ''.join(random.choice(string.ascii_letters + string.digits)\
                       for _ in range(size))
            password_str = '"' + password + '"'

            #Generate person height: random value between 50 to 250cm maybe: double 
            height = random.uniform(50,250)
    
            #Generate random birthdate: date between 1915-1-1 and 2000-12-31 (according to lifesum signup page)
            start_date = date(1915,1,1)
            end_date = date(2000,12,31)
            birth_date = random_date(start_date, end_date)
            birth_date_str = '"' + datetime.strftime(birth_date,'%Y-%m-%d') + '"'

            #Calculate age from birthDate
            today = date.today()
            age = today.year - birth_date.year - ((today.month, today.day) \
                  < (birth_date.month, birth_date.day))

            #Generate random last sync time: datetime between 2008-1-1 0:0:0 to now
            start_time = datetime.strptime('1/1/2008 0:0:0', '%m/%d/%Y %H:%M:%S')
            now = datetime.strftime(datetime.now(),'%m/%d/%Y %H:%M:%S')
            end_time = datetime.strptime(now, '%m/%d/%Y %H:%M:%S')
            lastsync = random_date(start_time, end_time)
            lastsync_str = '"'+datetime.strftime(lastsync, '%Y-%m-%d %H:%M:%S')+'"'

            #Generate random device from enum
            device = random.choice(('android','online','apple'))
            device_str = '"' + device + '"'

            #insert records to db
            cur.execute("INSERT INTO tbluser(firstname, lastname, username, height,\
                    age, password, lastsync, device, birthdate) VALUES(%s,%s,\
                    %s,%.2f,%i,%s,%s,%s,%s)" %(firstname_str,lastname_str,\
                    username_str, height,age,password_str,lastsync_str,\
                    device_str,birth_date_str))
            i += 1

        cur.execute("SELECT COUNT(*) from tbluser")
        result = str(cur.fetchone())
        current_row_count = int(result[1:-3])
        print "Table tbluser has "+str(current_row_count)+ " records now."

        if current_row_count - original_row_count == 1000:
            print "Insert 1000 random records successed!"
        else:
            print "Insert 1000 random records failed! Please check!"

def printTimeCost(start, end):
    #Print the time cost for insert 1000 records
    time_delta = end - start
    time_cost = (time_delta.days *24*60*60) + time_delta.seconds

    print ("The operation cost " + str(time_cost) + " seconds")

def main(argv):
    #Below is the command line parameters
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
    #call update_table to insert 1000 recodes
    update_table(server, user, passwd, db)
    
    end1 = datetime.now()
    #print the time cost
    printTimeCost(start1, end1)

if __name__ == "__main__":
    main(sys.argv[1:])
