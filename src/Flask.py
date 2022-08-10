from flask import Flask,render_template,request
from flask_cors import CORS
# Initializing flask app
app = Flask(__name__)
CORS(app)
  
  
# Route for seeing a data
@app.route('/index.html')
def serve():
    return render_template('index.html')
@app.route('/result',methods = ['POST'])
def Postserve():
    form_data = request.form
    return render_template('index.html',form_data = form_data)
   

if __name__ == '__main__':
    app.run(debug=True)
