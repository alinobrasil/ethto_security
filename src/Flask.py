from flask import Flask
from flask_cors import CORS
# Initializing flask app
app = Flask(__name__)
CORS(app)
  
  
# Route for seeing a data
@app.route('/')
def serve():
    send_from_directory('.', 'App.js')
@app.route('/result',methods = ['POST'])
def Postserve():
    return {
        'Name':"geek", 
        "Age":"22",
        "Date":"", 
        "programming":"python"
        }

if __name__ == '__main__':
    app.run(debug=True)
