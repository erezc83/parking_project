# parking_project

**Prerequisites:**
1. python 3.7
  1.1. To download and install Python, visit the official website of Python: https://www.python.org/downloads/ and choose the version.
  1.2. How to install Python on windows, you can use the website https://www.guru99.com/how-to-install-python.html

2. mysql workbrench 8.0.23
  2.1. To download and install mySQL, visit the official website of mySQL: https://dev.mysql.com/downloads/installer/
  2.2. How to install mySQL on windows, you can use: https://www.youtube.com/watch?v=WDEyt2VHpj4


**Please follow the next steps:**
1. Download all the files to the same locution (same folder).

2. Execute pip -r requirement.txt

3. Data Base and table creation:
  3.1. Open 'mySQL' server, press on "+" (add new Database).
  3.2. Insert all DB details to create new DN (there is an explanation in prerequisites 2.2).
  3.3. Press "OK" button (to finish).
  3.4. Double click on DB sql that you created now.
  3.5. On query tab execute the following script on 'mySQL' server:
       CREATE TABLE `parking` (
        `id` int(10) NOT NULL AUTO_INCREMENT,
        `vehicle_number` varchar(50) COLLATE utf8_bin NOT NULL,
        `vehicle_type` varchar(50) COLLATE utf8_bin NOT NULL,
        `allowed` BOOLEAN NOT NULL,  
        `timestemp` int(10) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
        AUTO_INCREMENT=1;
  3.6. Press "run" (the table will be created).

4. execute main.py file.
   Where there are two ways to execute the program.
  4.1. Using cmd: go to the main.py locution and execute python main.py.
  4.2. Execute main.py by using any python supporting. 
       for example: PyCharm.
       
5. Checking the DB:
  5.1 Open new query.
  5.2 Execute following:
      select * 
      from parking;
      
6. **program limitations:**
  6.1 the orc api is מתקשה some time with Hebrew letters.
  6.2 in order to overcome it the program is relates to the Hebrew letters “מ” as the English letter as "n”.


