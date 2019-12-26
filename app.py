from flask import Flask, url_for, redirect, render_template, request
import requests
import os

application = Flask(__name__)
application.config.from_pyfile( os.path.join(os.getcwd(), 'config-staging.py'))

@application.route("/")
def index():
    return  render_template("index.html")

@application.route("/contact/")
def contact():
    return render_template("construction.html")

@application.route("/courses/")
def courses():
    url = application.config["HOST"]
    url += "get_all_classes?api_key="
    url += application.config["SECRET_KEY"]
    url += "&archived=false"
    r = requests.get(url)
    course_list = []
    for course in r.json():
        if course["catalog_category"] == "Continuing Education For EMS Professionals":
            course_list.append(course)

    return render_template("courses.html", courses= course_list, host = 'http://edu.c3emstraining.com/visitor_catalog_class/show/')

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
    
    application.run()
 