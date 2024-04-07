from flask import Flask, render_template, request, redirect
import mysql.connector
import os
import random
import string
from werkzeug.security import generate_password_hash

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'erfan',
    'password': '13791379',
    'database': 'erfan'
}

def connect_to_db():
    try:
        connection = mysql.connector.connect(**db_config)
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))
        return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Email = request.form['Email']
        Password = request.form['Password']
        
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            sql_query = "SELECT * FROM users WHERE Email = %s AND Password = %s"
            cursor.execute(sql_query, (Email, Password))
            user = cursor.fetchone()
            
            if user:
                return redirect('/welcome')
            else:
                return "Invalid email or password. Please try again."
            
            cursor.close()
            connection.close()
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['First_name']
        last_name = request.form['Last_name']
        email = request.form['Email']
        password = request.form['Password']
        
        
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            sql_query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_query, (first_name, last_name, email, password))
            connection.commit()
            
            cursor.close()
            connection.close()
            
            return redirect('/login')
        
    return "Failed to sign up. Please try again later."

@app.route('/recover_password', methods=['POST'])
def recover_password():
    if request.method == 'POST':
        Email = request.form['Email']
        
        
        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        
        
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            sql_query = "UPDATE users SET Password = %s WHERE Email = %s"
            cursor.execute(sql_query, (new_password, Email))
            connection.commit()
            
            
            cursor.close()
            connection.close()
            
            return f"Password reset successfully. New password: {new_password}"
        
    return "Failed to recover password. Please try again later."


@app.route('/welcome')
def welcome():
    return render_template('/welcome.html')


if __name__ == '__main__':
    app.run(debug=True)
