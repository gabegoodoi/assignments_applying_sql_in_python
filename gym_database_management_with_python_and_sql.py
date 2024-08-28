'''
Submission Guidelines:

        Submit a Python script (.py file) containing all the functions for the tasks.
        Include comments in your code to explain your logic and SQL queries.
        Ensure your script handles errors gracefully and provides meaningful output.

Objective: 

        The aim of this assignment is to reinforce your understanding of Python's interaction with SQL databases, focusing on CRUD (Create, Read, Update, Delete) operations in the context of a gym's membership and workout session management system. You will work with two tables: 'Members' and 'WorkoutSessions'.

Problem Statement: 

        You are tasked with developing a Python application to manage a gym's database. The database consists of 'Members' and 'WorkoutSessions' tables. Your role is to implement various functions to add, retrieve, update, and delete records in these tables, ensuring data integrity and efficient data handling.

Task 1: Add a Member

        Write a Python function to add a new member to the 'Members' table in the gym's database.

            # Example code structure
            def add_member(id, name, age):
                # SQL query to add a new member
                # Error handling for duplicate IDs or other constraints

        Expected Outcome: 
        
            A Python function that successfully adds a new member to the 'Members' table in the gym's database. The function should handle errors gracefully, such as duplicate member IDs or violations of other constraints.
'''
import mysql.connector
from mysql.connector import Error

# this function will run in all of the others in order to forge a proper connection to the correct database. It requires 4 major details about the connection (1) the name of the database (2) the name of the user (3) the name of the password (4) the name of the host.

def connect_database():
    db_name = input("Input database name: ")
    user = input("Input User name: ")
    password = input("Input Password: ")
    host = input("Input Host: ")
    
    # once that info is collected we'll try to use the connect() method from the mysql.connector module to connect to open a connection with a MySQL server (and the database of interest within that server)
    try:
        connection = mysql.connector.connect(
               database = db_name,
               user = user,
               password = password,
               host = host
               )

        print("Connected to MySQL database successfully.")
        # if it works we return the connection to use the connection in the other functions
        return connection
    
    # if the above doesn't work we're returning an error message.
    except Error as e:
        print(f"Error: {e}")
        return None

# here's the function that will add a new member to the database, I diverged from the example because id is autoincremented already, which is cleaner and safer for a primary key.
def add_member(name, age, id=None):
        connection = connect_database() # first we establish the database connection
        if connection is not None: # if the database connection works we'll try the following
                try:
                        # this try block activates a cursor connected to the connected database  which is what is used to later execute the query.
                        cursor = connection.cursor()
                        
                        # SQL query to add a new member
                        query = "INSERT INTO Members (name, age) VALUES (%s, %s)"
                        
                        # this next bit runs the query statement with the name and age in place of the  formatted placeholders %s and %s.
                        cursor.execute(query, (name, age))
                        # then it commits the executed query to the actual server.
                        connection.commit()
                        # then I let the user know it was a success
                        print(f"Member {name} added successfully")
                        
                # if the above doesn't work we're returning an error message.
                except Exception as e:
                      print(f"Error: {e}")
                
                # we make sure to close the cursor and the connection no matter what
                finally:
                      cursor.close()
                      connection.close()       

#IMPORTANT: if you want to run the actual function first you'll need to uncomment the following three lines

# name = input("New Member's name: ")
# age = int(input("New member's age: "))
# add_member(name, age)
'''
Task 2: Add a Workout Session

        Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.

            # Example code structure
            def add_workout_session(member_id, date, duration_minutes, calories_burned):
                # SQL query to add a new workout session
                # Error handling for invalid member ID or other constraints

        Expected Outcome: 
            
            A Python function that adds a new workout session to the 'WorkoutSessions' table in the gym's database for a specific member. The function should handle errors gracefully, such as invalid member IDs or violations of other constraints.
'''

def add_workout_session(member_id, session_date, session_time, activity):
        connection = connect_database() # first we establish the database connection
        if connection is not None: # if the database connection works we'll try the following
                try:
                        # this try block activates a cursor connected to the connected database  which is what is used to later execute the query.
                        cursor = connection.cursor()
                        
                        # SQL query to add a new member
                        query = "INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s)"
                        
                        # this next bit runs the query statement with the name and age in place of the  formatted placeholders.
                        cursor.execute(query, (member_id, session_date, session_time, activity))
                        # then it commits the executed query to the actual server.
                        connection.commit()
                        # then I let the user know it was a success
                        print(f"Workout session added successfully")
                        
                # if the above doesn't work we're returning an error message.
                except Exception as e:
                      print(f"Error: {e}")
                
                # we make sure to close the cursor and the connection no matter what
                finally:
                      cursor.close()
                      connection.close()       

#IMPORTANT: if you want to run the actual function first you'll need to uncomment the following 5 lines

# member_id = input("Member's ID: ")
# session_date = input("Date (format YYYY-MM-DD): ")
# session_time = input("Start time: ")
# activity = input("Activity: ")
# add_workout_session(member_id, session_date, session_time, activity)

'''
Task 3: Updating Member Information

        Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update.

            # Example code structure
            def update_member_age(member_id, new_age):
                # SQL query to update age
                # Check if member exists
                # Error handling

        Expected Outcome: 
        
            A Python function that updates the age of a member and handles cases where the member does not exist.
'''

def update_member_age(member_id, new_age):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()

            query = "UPDATE Members SET age = %s WHERE id = %s"

            cursor.execute(query, (new_age, member_id))
            connection.commit()
            print("Member age updated successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()

#IMPORTANT: if you want to run the actual function first you'll need to uncomment the following 3 lines

# member_id = input("Member's ID: ")
# new_age = input("Updated age: ")
# update_member_age(member_id, new_age)

'''
Task 4: Delete a Workout Session

        Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID does not exist.

            # Example code structure
            def delete_workout_session(session_id):
                # SQL query to delete a session
                # Error handling for non-existent session ID

        Expected Outcome: 
            
            A Python function that can delete a workout session using its session ID, with proper error handling for invalid IDs.
'''

def delete_workout_session(session_id):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()

            # SQL Query
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"

            #executing the query
            cursor.execute(query, (session_id, ))
            connection.commit()
            print("Workout Session removed successfully.")
        
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()

#IMPORTANT: if you want to run the actual function first you'll need to uncomment the following 2 lines

# session_id  = input("Workout Session ID to remove: ")
# delete_workout_session(session_id)