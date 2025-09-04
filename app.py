from flask import Flask,render_template, request
from flask_restful import Api, Resource, reqparse
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
api = Api(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Tinku@143'
app.config['MYSQL_DATABASE_DB'] = 'h2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def user_list():
    cur = mysql.connect().cursor()
    cur.execute("SELECT * FROM coach")
    users = cur.fetchall()
    cur.close()
    return render_template('user_list.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)