import sqlite3
import openpyxl

def jsonToSQL(json):
    connection = sqlite3.connect("answers.db")
    cursor = connection.cursor()

    noNameJSON = json

    #Get kids name from the first key and value from the JSON file.
    name = json["Your name?"]

    #Create the table and insert questions/answers
    cursor.execute("CREATE TABLE " + str(name) + " (Questions text, Answers text)")

    del noNameJSON["Your name?"]
    
    for key, val in noNameJSON.items():
        temp = [key,val]
        cursor.executemany("INSERT INTO " + str(name) + " VALUES(?,?)", (temp,))
        connection.commit()
    
    cursor.execute("SELECT * FROM " + str(name))
    allRows = cursor.fetchall()
    for row in allRows:
        print(row)

def csvToSQL(csvFilePath):
    results = []
    # Get questions file
    wb = openpyxl.load_workbook("questions.xlsx")
    ws = wb.active
    for row in ws.iter_rows(values_only=True):
        results.append(row)

    connection = sqlite3.connect("answers.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE Correct (CorrectQ text, CorrectA text)")

    temp = []

    for i in range(len(results)):
        if i==0:
            continue
        temp = []
        temp.append(results[i][0])
        temp.append(results[i][1])    
        cursor.executemany("INSERT INTO Correct VALUES(?,?)", (temp,))

    cursor.execute("SELECT * FROM Correct")
    allRows = cursor.fetchall()
    for row in allRows:
        print(row)

#NOTE: unfinished
# def compareAnswers(name):
#     connection = sqlite3.connect("answers.db")
#     cursor = connection.cursor()

#     cursor.execute("SELECT * FROM Correct")
#     allCorrect = cursor.fetchall()
#     for row in allCorrect:
#         print(row)

#     cursor.execute("SELECT * FROM " + str(name))
#     allStudentAnswers = cursor.fetchall()
#     for row in allStudentAnswers:
#         print(row)
