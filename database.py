import sqlite3

import tui

"""
This module is responsible for setting up and querying the database.
"""

"""
Task 22 - 26: Write suitable functions to query the database as follows:

Setup database
Retrieve the names of all (unique) countries in alphabetical order
Retrieve the number of confirmed cases, deaths and recoveries for a specified observation / serial number.
Retrieve information for the top 5 countries for confirmed cases
Retrieve information for the top 5 countries for death for specific observation dates


The function for setting up the database should do the following:
- Take a list of records as a parameter
- Use the list passed as a parameter value to create and populate a suitable database. You are required to design a
suitable (small) database.
- It is recommended that you complete this function last and start by creating your database using a tool such as
SQL DB Browser. This would allow you to complete the other database functions first.  You can then complete this
function to generate the database via code.

Each function for querying the database should follow the pattern below:
- Take no parameters
- Query the database appropriately. You may use the module 'tui' to retrieve any additional information 
required from the user to complete the querying.
- Return a list of records as retrieved from the database

"""


# 22 setting up database
def set_database(records):
    name_db = input("Please enter database name:")
    db = sqlite3.connect(f"{name_db}.db")
    cursor = db.cursor()
    sql = """
    BEGIN TRANSACTION;
    CREATE TABLE IF NOT EXISTS "observations" (
	   "id"	INTEGER NOT NULL UNIQUE,
	   "obs_date"	TEXT NOT NULL,
	   "last_update"	TEXT NOT NULL,
	   "confirmed"	INTEGER NOT NULL,
	   "death"	    INTEGER NOT NULL,
	   "recovered"	INTEGER NOT NULL,
	   PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "locations" (
                "id"   INTEGER NOT NULL UNIQUE,
                "state" TEXT NOT NULL,
                "country" TEXT NOT NULL,
                "obs_id"  INTEGER NOT NULL,
                FOREIGN KEY("obs_id") REFERENCES "observations"("id"),
                PRIMARY KEY("id" AUTOINCREMENT)
    );
    COMMIT;
    """
    cursor.executescript(sql)

    for record in records:
        sql = "INSERT INTO observations" \
              "(obs_date,last_update,confirmed,death,recovered)" \
              "VALUES (?, ?, ?, ?, ?)"
        values = [record[1], record[4], record[5], record[6], record[7]]
        cursor.execute(sql, values)
        sql1 = "INSERT INTO locations (state, country, obs_id) VALUES(?, ?, ?)"
        values = [record[2], record[3], record[0]]
        cursor.execute(sql1, values)
    db.commit()
    db.close()


# 23 To retrieve names of all unique countries in alphabetical order
def ret_c_names():
    db = sqlite3.connect("default.db")
    cursor = db.cursor()
    sql = "SELECT DISTINCT country FROM locations ORDER BY country ASC"  # country FROM observations GROUP BY country"
    cursor.execute(sql)
    records = cursor.fetchall()
    return records


# 24 Retrieve the number of confirmed cases, deaths and recoveries for a specified observation / serial number.
def retrieve_all():
    s_num = tui.serial_number()
    db = sqlite3.connect("default.db")
    cursor = db.cursor()
    sql = f"SELECT confirmed,death,recovered FROM observations WHERE id ={s_num}"
    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()
    return records


# 25 To retrieve info for the first 5 countries for confirmed cases
def retrieve_top5():
    db = sqlite3.connect("default.db")
    cursor = db.cursor()
    sql = "SELECT  country,sum(confirmed) FROM observations " \
          "INNER JOIN locations ON observations.id = locations.obs_id " \
          "GROUP by country ORDER by sum(confirmed) DESC LIMIT 5"
    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()
    return records


# 26 Retrieve information for the top 5 countries for death for specific observation dates
def retrieve_top5_det():
    dates = tui.observation_dates()
    db = sqlite3.connect("default.db")
    cursor = db.cursor()
    for date in dates:
        sql = "SELECT * FROM observations " \
              "INNER JOIN locations ON observations.id = locations.obs_id " \
              "WHERE obs_date=? GROUP by country ORDER BY sum(death) DESC LIMIT 5"
        values = [date]
        cursor.execute(sql, values)
        records = cursor.fetchall()
        db.close()
        return records


# additional function to retrieve information for animation in visual module
def retrieve_country_info_an():
    reg = "Mainland China"
    db = sqlite3.connect("default.db")
    cursor = db.cursor()
    sql = "SELECT obs_date,country,confirmed,death,recovered FROM observations " \
          "INNER JOIN locations ON observations.id=locations.obs_id " \
          "WHERE country=? GROUP by obs_date"
    values = [reg]
    cursor.execute(sql, values)
    records = cursor.fetchall()
    db.close()
    return records
