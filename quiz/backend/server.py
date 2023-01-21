# Import flask and datetime module for showing date and time
from flask import Flask, request
import datetime
import json
import random
import openpyxl
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)

# Initialize random questions
@app.route('/data')
def get_time():
    # Get questions file
    wb = openpyxl.load_workbook("questions.xlsx")
    ws = wb.active

    for row in ws.iter_rows(values_only=True):
        invalid_links.append(row[0])

    # Pick 10 random questions
    random_idxs = random.sample(range(0, len(questions)+1), 10)
    for i in rand:
        print(i)
    
    # Closing file
    f.close()
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }
  
@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo_data = request.get_json()
    print(todo_data)
    return 'Done', 201
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)