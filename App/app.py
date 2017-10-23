from flask import Flask, render_template, request, json
import pymysql
conn = pymysql.connect(
    db='example',
    user='root',
    passwd='***REMOVED***',
    host='localhost',
    autocommit=True) # important or add conn.commit() after query
c = conn.cursor()

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "Welcome to Python Flask!"
 
@app.route('/signUp') 
def signUp():
    return render_template('signUp.html')
    
@app.route('/signUpUser', methods=['POST'])
def signUpUser():
	user =  request.form['username'];
	password = request.form['password'];
	response = {'status':'OK','user':user,'pass':password};
	c.execute("INSERT INTO users (user, password) VALUES ('%s', '%s');" %(user, password)); 
	return json.dumps(response), 200, {'content-type': 'application/json'};

if __name__ == "__main__":
    app.run()



 
