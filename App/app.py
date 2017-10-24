from flask import Flask, render_template, request, json
import pymysql
import config
conn = pymysql.connect(
    db='example',
    user=config.username,
    passwd=config.password,
    host='localhost',
    autocommit=True) # important or add conn.commit() after query
c = conn.cursor()

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "Hello World! Welcome to my first Python Flask app!"
 
@app.route('/display') 
def display():
    return render_template('display.html')
    
@app.route('/postAnswer', methods=['POST'])
def postAnswer():
	question =  request.form['question'];
	text = request.form['text'];
	answer = request.form['answer'];
	response = {'status':'OK','question':question,'text':text,'answer':answer};
	c.execute("INSERT INTO questions (question, text, answer) VALUES ('%s', '%s', '%s');" %(question, text, answer)); 
	return json.dumps(response), 200, {'content-type': 'application/json'};

if __name__ == "__main__":
    app.run()



 
