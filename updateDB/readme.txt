1. Description: This script is used to insert 1000 random records to MySQL database table tbluser

2. Setup and Configuration:
1). Setup database, table and user
   For ubuntu (I use ubuntu 14.04 desktop edition), run:
       sudo apt-get install mysql-server
       sudo apt-get install python-mysqldb
   Create database and table(tbluser)
   Create a user and grant privilege to database and table

2). Install additional libraries
   sudo pip install names
   #names is a python module to generate random names

3. How to run:
For example:
python updateDB.py -s localhost -u guanlei -p Wgl09026 -d lifesum
Output:
Table tbluser has 7019 records.
Table tbluser has 8019 records now.
Insert 1000 random records successed!
The operation cost 10 seconds


   
