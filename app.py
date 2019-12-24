from flask import Flask, url_for, redirect, render_template, request
application = Flask(__name__)


@application.route("/")
def index():
    return  render_template("index.html")

@application.route("/contact/")
def contact():
    return render_template("construction.html")

@application.route("/courses/")
def courses():
    return render_template("construction.html")

@application.route("/clients/")
def clients():
    return render_template("quotes.html")

@application.errorhandler(500)
def internal_error(error):
    m = "An internal error was encounted. Sorry the website might be down, check again later to see if the website is back up"
    return render_template("error.html", code = 500, message= m)

@application.errorhandler(404)
def not_found(error):
    m = "The page you requested was not found."
    return render_template("error.html", code = 404, message = m)

if(__name__ == '__main__'):
    
    application.run(debug= True)
 