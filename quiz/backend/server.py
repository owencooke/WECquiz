from flask import Flask, request
import random
import openpyxl
  
# Init app
app = Flask(__name__)

'''
Select 10 random quiz questions from a Microsoft Excel file
provided by the teacher and pass to React as a JSON object.
'''
@app.route('/questions')
def init_quiz():
    # Init new quiz
    quiz = {
        "showProgressBar": "top",
        "pages": [{
            "elements": [{
                "name": "Your name?",
                "title": "Your name?",
                "type": "text",
                "isRequired": True
            }]
        }]
    }
    
    # Get questions file
    wb = openpyxl.load_workbook("questions.xlsx")
    ws = wb.active

    # Select 10 random question numbers
    num_q = 0
    for row in ws:
        if not all([c.value is None for c in row]):
            num_q += 1
    random_idxs = random.sample(range(1, num_q), 10)

    # Add each random MC question and possible answers
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i in random_idxs:
            choices = list(row[1:])
            random.shuffle(choices)
            # Add question to JSON for quiz init
            quiz["pages"].append({
                "elements": [{
                    "name": row[0],
                    "title": row[0],
                    "type": "radiogroup",
                    "choices": choices,
                    "isRequired": True
                }]
            })

    # #DEBUG: output init to json file for testing
    # # Serializing json
    # json_object = json.dumps(quiz, indent=2)
    # # Writing to sample.json
    # with open("sample.json", "w") as outfile:
    #     outfile.write(json_object)
            
    # generated quiz questions
    return quiz
  
'''
Return quiz results in form of JSON file. 
'''
@app.route('/complete', methods=['POST'])
def complete():
    answers = request.get_json()
    print(answers)
    return 'Done', 201
      
if __name__ == '__main__':
    app.run(debug=True)