import random
from playsound import playsound
import threading
import sys

queryArr = []
answerArr = []

def populateQueryArr(queryArr):
    #SQL SELECT
    queryArr.append("Get all the columns from the Customers table")
    queryArr.append("Select the City column from the Customers table")
    queryArr.append("Select all the different values from the Country column in the Customers table")

    #SQL WHERE
    queryArr.append("Select all records in the Customers table where the City column has the value 'Berlin'")
    queryArr.append("Select all records in the Customers table where the CustomerID column has the value 32")

    #SQL ORDER BY
    queryArr.append("Select all records from the Customers table, sort the result alphabetically by the column City")
    queryArr.append("Select all records from the Customers table, sort the result reversed alphabetically by the column City")
    queryArr.append("Select all records from the Customers table, sort the result alphabetically, first by the column Country, then, by the column City")

    #SQL AND
    queryArr.append("Select all records in the Customers table where the City column has the value 'Berlin' and the PostalCode column has the value '12209'")

    #SQL OR
    queryArr.append("Select all records in the Customers table where the City column has the value 'Berlin' OR 'London'")

    #SQL NOT
    queryArr.append("Use the NOT keyword to select all records in the Customers table where City is NOT 'Berlin'")

    #SQL INSERT - We are skipping this

    #SQL NULL
    queryArr.append("Select all records from the Customers where the PostalCode column is empty")
    queryArr.append("Select all records from the Customers where the PostalCode column is NOT empty")

    #SQL UPDATE
    queryArr.append("Update the City column of all records in the Customers table")
    queryArr.append("In the Customers table, Set the value of the City columns to 'Oslo', but only the ones where the Country column has the value 'Norway'")
    queryArr.append("In the Customers table, set all cities to 'Oslo' and all countries to 'Norway' where the CustomerID = 32")

    #SQL DELETE
    queryArr.append("Delete all the records from the Customers table where the Country value is 'Norway'")
    queryArr.append("Delete all the records from the Customers table")

    #SQL Functions - Products table
    queryArr.append("Use the MIN function to select the record with the smallest value of the Price column in the Products table")
    queryArr.append("Use an SQL function to select the record with the highest value of the Price column in the Products table")
    queryArr.append("Use the correct function to return the number of records that have the Price value set to 18 in the Products table")
    queryArr.append("Use an SQL function to calculate the average Price of all products in the Products table")
    queryArr.append("Use an SQL function to calculate the sum of all the Price column values in the Products table")

    #SQL LIKE
    queryArr.append("Select all records in the Customers table where the value of the City column starts with the letter 'a'")
    queryArr.append("Select all records in the Customers table where the value of the City column ends with the letter 'a'")
    queryArr.append("Select all records in the Customers table where the value of the City column contains the letter 'a'")
    queryArr.append("Select all records in the Customers table where the value of the City column starts with letter 'a' and ends with the letter 'b'")
    queryArr.append("Select all records in the Customers table where the value of the City column does NOT start with the letter 'a'")

    #SQL Wildcards
    queryArr.append("Select all records in the Customers table where the second letter of the City is an 'a'")
    queryArr.append("Select all records in the Customers table where the first letter of the City is an 'a' or a 'c' or an 's'")
    queryArr.append("Select all records in the Customers table where the first letter of the City starts with anything from an 'a' to an 'f'")
    queryArr.append("Select all records in the Customers table where the first letter of the City is NOT an 'a' or a 'c' or an 'f'")

    #SQL IN
    queryArr.append("Use the IN operator to select all the records in the Customers table where Country is either 'Norway' or 'France'")
    queryArr.append("Use the IN operator to select all the records in the Customers table where Country is NOT 'Norway' and NOT 'France'")

    #SQL BETWEEEN - Products table
    queryArr.append("Use the BETWEEN operator to select all the records in the Products table where the value of the Price column is between 10 and 20")
    queryArr.append("Use the BETWEEN operator to select all the records in the Products table where the value of the Price column is NOT between 10 and 20")
    queryArr.append("Use the BETWEEN operator to select all the records in the Products table where the value of the ProductName column is alphabetically between 'Geitost' and 'Pavlova'")

    #SQL ALIAS - We are skipping this
    #SQL JOIN - We are skipping this

    #SQL GROUP BY
    queryArr.append("From the Customers table, list the number of customers in each country")
    queryArr.append("From the Customers table, list the number of customers in each country, ordered by the country with the most customers first")

    #SQL Database
    queryArr.append("Write the correct SQL statement to create a new database called testDB")
    queryArr.append("Write the correct SQL statement to delete a database named testDB")
    # queryArr.append("Write the correct SQL statement to create a new table called Persons") --> Skip this
    queryArr.append("Write the correct SQL statement to delete a table called Persons")
    queryArr.append("Use the TRUNCATE statement to delete all data inside the table Persons")
    queryArr.append("Add a column of type DATE called Birthday in the Persons table")
    queryArr.append("Delete the column Birthday from the Persons table")

def populateAnswerArr(answerArr):
    #SQL SELECT
    answerArr.append("SELECT * FROM Customers;")
    answerArr.append("SELECT City FROM Customers;")
    answerArr.append("SELECT DISTINCT Country FROM Customers;")

    #SQL WHERE
    answerArr.append("SELECT * FROM Customers WHERE City = 'Berlin';")
    answerArr.append("SELECT * FROM Customers WHERE CustomerID = 32;")

    #SQL ORDER BY
    answerArr.append("SELECT * FROM Customers ORDER BY City;")
    answerArr.append("SELECT * FROM Customers ORDER BY City DESC;")
    answerArr.append("SELECT * FROM Customers ORDER BY Country, City;")

    #SQL AND
    answerArr.append("SELECT * FROM Customers WHERE City = 'Berlin' AND PostalCode = '12209';")

    #SQL OR
    answerArr.append("SELECT * FROM Customers WHERE City = 'Berlin' OR City = 'London';")

    #SQL NOT
    answerArr.append("SELECT * FROM Customers WHERE NOT City = 'Berlin';")

    #SQL INSERT - We are skipping this

    #SQL NULL
    answerArr.append("SELECT * FROM Customers WHERE PostalCode IS NULL;")
    answerArr.append("SELECT * FROM Customers WHERE PostalCode IS NOT NULL;")

    #SQL UPDATE
    answerArr.append("UDPATE Customers SET City = 'Oslo';")
    answerArr.append("UPDATE Customers SET City = 'Oslo' WHERE Country = 'Norway';")
    answerArr.append("UPDATE Customers SET City = 'Oslo', Country = 'Norway' WHERE CustomerID = 32;")

    #SQL DELETE
    answerArr.append("DELETE FROM Customers WHERE Country = 'Norway';")
    answerArr.append("DELETE FROM Customers;")

    #SQL Functions - Products table
    answerArr.append("SELECT MIN(Price) FROM Products;")
    answerArr.append("SELECT MAX(Price) FROM Products;")
    answerArr.append("SELECT COUNT(*) FROM Products WHERE Price = 18;")
    answerArr.append("SELECT AVG(Price) FROM Products;")
    answerArr.append("SELECT SUM(Price) FROM Products;")

    #SQL LIKE
    answerArr.append("SELECT * FROM Customers WHERE City LIKE 'a%';")
    answerArr.append("SELECT * FROM Customers WHERE City LIKE '%a';")
    answerArr.append("SELECT * FROM Customers WHERE City LIKE '%a%';")
    answerArr.append("SELECT * FROM Customers WHERE City LIKE 'a%b';")
    answerArr.append("SELECT * FROM Customers WHERE City NOT LIKE 'a%';")

    #SQL Wildcards
    answerArr.append("SELECT * FROM Customers WHERE City LIKE '_a%';")
    answerArr.append("SELECT * FROM Customers WHERE City LIKE '[acs]%';")
    answerArr.append("SELECT * FROM Customers WHERE City LIKE '[a-f]%';")
    answerArr.append("SELECT * FROM Customers WHERE City LIKE '[!acf]%';")

    #SQL IN
    answerArr.append("SELECT * FROM Customers WHERE Country IN ('Norway', 'France');")
    answerArr.append("SELECT * FROM Customers WHERE Country NOT IN ('Norway', 'France');")

    #SQL BETWEEEN - Products table
    answerArr.append("SELECT * FROM Products WHERE Price BETWEEN 10 AND 20;")
    answerArr.append("SELECT * FROM Products WHERE Price NOT BETWEEN 10 AND 20;")
    answerArr.append("SELECT * FROM Products WHERE ProductName BETWEEN 'Geitost' AND 'Pavlova';")

    #SQL ALIAS - We are skipping this
    #SQL JOIN - We are skipping this

    #SQL GROUP BY
    answerArr.append("SELECT COUNT(CustomerID), Country, FROM Customers, GROUP BY Country;")
    answerArr.append("SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country ORDER BY COUNT(CustomerID) DESC;")

    #SQL Database
    answerArr.append("CREATE DATABASE TestDB;")
    answerArr.append("DROP DATABASE testDB;")
    # answerArr.append("Write the correct SQL statement to create a new table called Persons") --> Skip this
    answerArr.append("DROP TABLE Persons;")
    answerArr.append("TRUNCATE TABLE Persons;")
    answerArr.append("ALTER TABLE Persons ADD Birthday DATE;")
    answerArr.append("ALTER TABLE Persons DROP COLUMN Birthday;")

def askRestart():
    while True:
        play_again = input("Would you like to practice again? (y/n): ").lower().strip()
        if play_again == 'y':
            random.shuffle(questions_and_answers)  # Optionally reshuffle the questions
            return True
        elif play_again == 'n':
            return False
        else:
            print(RED + "Please enter 'y' for yes or 'n' for no." + RESET)
            print("\n")

def play_sound_async(file):
    playsound(file)

def start_sound_thread(file):
    if not hasattr(start_sound_thread, "thread") or not start_sound_thread.thread.is_alive():
        start_sound_thread.thread = threading.Thread(target=play_sound_async, args=(file,))
        start_sound_thread.thread.start()

populateQueryArr(queryArr)
populateAnswerArr(answerArr)

# Ensure the correspondence between questions and answers
questions_and_answers = list(zip(queryArr, answerArr))
# random.shuffle(questions_and_answers)

RED = "\033[91m"
GREEN = "\033[92m"
LIGHT_BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"  # Reset color to default

restart = True
while restart:
    print("\n")
    for query, correct_answer in questions_and_answers:
        user_answer = False

        while not user_answer:
            print(LIGHT_BLUE + query + RESET)
            answer = input("Enter query: ")

            if answer == correct_answer:
                user_answer = True
                print(GREEN + "Correct!" + RESET)

            elif answer.lower() == "skip":
                user_answer = True
                print(YELLOW + "Skipping question..." + RESET)

            elif answer.lower() == "quit":
                sys.exit()

            else:
                print(RED + "Incorrect. Try again!" + RESET)
                start_sound_thread('oof.wav')

            print("\n")
        
    restart = askRestart()