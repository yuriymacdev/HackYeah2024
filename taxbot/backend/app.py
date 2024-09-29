from flask import Flask, render_template, request, jsonify, send_file, session
from statemachine import UserStateMachine
# import model_api
from io import BytesIO
import random, string


app = Flask(__name__)
app.secret_key = 'qwer23452welrkgj23l45tsdfgn23lk5t'

stateMachines = {}

def generateRandomWord(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


@app.route('/')
def index():
    stateMachineName = generateRandomWord(5)
    stateMachines[stateMachineName] = UserStateMachine()

    session['statemachine'] = stateMachineName
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def handle_api():
    if request.is_json:
        if stateMachines[session['statemachine']].dialogueEnded:
            response = {
                "serverMessage": "Dialog zakończony! Proszę odświeżyć stronę, jeśli chcesz utworzyć inny plik xml"
            }
            return jsonify(response), 200

        # Parse the JSON data
        data = request.get_json()
        userMessage = data["userMessage"]
        print(userMessage)

        botResponse = stateMachines[session['statemachine']].handleUserResponse(userMessage)

        # ollama_response = model_api.send_prompt(userMessage)
        # Handle the data (for example, just return it)
        # print(ollama_response)
        response = {
            "serverMessage": botResponse
        }
        return jsonify(response), 200
    else:
        # Handle cases where JSON is not provided
        return jsonify({"error": "Invalid JSON data"}), 400

# in the end the model should give the user a link in chat, in a form:
# <a href="/taxform.xml">Download generated taxform XML</a>

@app.route('/taxform.xml')
def get_xml():
    file_data = BytesIO()


    xmlstring = stateMachines[session['statemachine']].xmlText
    print(xmlstring)

    file_data.write(xmlstring.encode('utf-8'))
    file_data.seek(0)

    return send_file(file_data, as_attachment=True, download_name="taxform.xml", mimetype='text/xml')

    return r

