import time
from flask import Flask, render_template
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app =Flask ( __name__ )
def currenttime():
    return time.asctime (time.localtime ( time.time()))

currenttime = currenttime()
@app.route('/')
@app.route ( "/menu" )
def menu():
     return render_template ('home.html', currtime=currenttime)
@app.route ( "/main" )
def main():
    return render_template ('main.html', currtime=currenttime)
@app.route ( "/intro" )
def intro_tutorial():
    return render_template ('intro.html', currtime=currenttime)
@app.route('/logged_in')
def logged():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Welcome!!"
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return logged()


if __name__ == "__main__":
    app.run ( port=8080 )
