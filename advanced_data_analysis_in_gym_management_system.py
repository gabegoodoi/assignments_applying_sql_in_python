
'''
Objective: 
    
    The goal of this assignment is to advance your SQL querying skills within Python, focusing on specific SQL functions and clauses like BETWEEN. You will be working with the same gym database as in the previous assignment, comprising the Members and WorkoutSessions tables.

Problem Statement: 
    
    As a part of the gym's management team, you need to conduct an in-depth analysis of the membership data. Your task is to develop Python functions that execute advanced SQL queries for distinct department identification, employee count in each department, and age-based employee filtering.

Task 1: SQL BETWEEN Usage

    Problem Statement: 
    
        Retrieve the details of members whose ages fall between 25 and 30.

    Expected Outcome: 
        
        A list of members (including their names, ages, etc) who are between the ages of 25 and 30.

        Example Code Structure:

            def get_members_in_age_range(start_age, end_age):
                # SQL query using BETWEEN
                # Execute and fetch results
'''

import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = input("Input database name: ")
    user = input("Input User name: ")
    password = input("Input Password: ")
    host = input("Input Host: ")
    
    try:
        connection = mysql.connector.connect(
               database = db_name,
               user = user,
               password = password,
               host = host
               )

        print("Connected to MySQL database successfully.")
        return connection
    
    except Error as e:
        print(f"Error: {e}")
        return None
    
def get_members_in_age_range(start_age, end_age):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            
            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s;"

            cursor.execute(query, (start_age, end_age))
            
            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            connection.close()

start_age = input("Enter minimum age for range: ")
end_age = input("Enter maximum age for range: ")
get_members_in_age_range(start_age, end_age)