from flask import Flask, request,render_template
import sqlite3
def create_connection():
    Conn=sqlite3.Connection('re')

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
  
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__=='__main__':
    app.run(debug =True)
   
