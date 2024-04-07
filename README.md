# Login-and-Sign-up-pages
My first Project was with HTML and CSS on the front-end side and Python and Flask on the back-end side which all connected to a Mysql database. This project has different code files such as app.py, Login.html, and Signup. HTML, forgotpassword.html, and welcome.html which are all html files styled by style.css files and used from simple codes on javascript for some features. 

## app.py
this file contains Python codes and Flask codes for the back-end side and is connected front-end to the MySQL database, you can change database information:
``` python
db_config = {
    'host': 'your hostname',
    'user': 'your host user name',
    'password': 'your host password',
    'database': 'your database name '
}
```
you need also create 4 columns in your database as below:
First_name, Lastname, Email, and Password. after doing these works you should first run the app.py with Python IDLE

in this file, there are specific sections for each HTML file that are routed specifically

## Signup page
This is the first recommended file that you should open with a browser and use from it to sign up.

## Login page
Now you can open this file enter your information and log in to the website simply.


## Forgot password
if you forget your password you can use this file to generate a new random password.

## welcome
this is a simple welcoming page after a successful login to the site.

## style.css 
this is a complete style file for 4 HTML files, in the CSS file, related parts to each HTML file are specified.

## app.js
this is a javascript simple file for Login and signup pages. On the Login page showing and hiding password function used from this file. on the Signup page password and password confirm use from this file to match the password and its confirm parts.


