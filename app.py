from flask import Flask, url_for, redirect, render_template, request
application = Flask(__name__)


@application.route("/")
def index():
    return  render_template("index.html")

if(__name__ == '__main__'):
    
    application.run(debug= True, host='0.0.0.0')
 