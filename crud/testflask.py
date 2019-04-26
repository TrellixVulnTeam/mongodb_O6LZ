from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mydatabase'
app.config['MONGO_URI'] = '<URI MONGODB>'

mongo = PyMongo(app)

@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({'name' : 'Anthony'})
    return 'Added User:'

if __name__ == '__main__':
    app.run(debug=True)

''' from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola Mundo!"

if __name__ == "__main__":
    app.run() '''