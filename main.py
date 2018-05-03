import cgi
import textwrap
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import datastore


# [GLOBAL VARIABLE INITILISATION]
user = users.get_current_user()
user_email = user.email()
user_id_number = user.user_id()
# [END GLOBAL VARIABLE INITILISATION]

# [GOOGLE DATASTORE 'KIND' INITILISATION]
class Account(ndb.Model):
    user_email = ndb.GenericProperty()
    user_id_number = ndb.GenericProperty()

class Event(ndb.Model):
    user_email = ndb.GenericProperty()
    user_id_number = ndb.GenericProperty()
    eventName = ndb.StringProperty()
    eventDate = ndb.StringProperty()
    eventLocation = ndb.StringProperty()
    eventDetails = ndb.TextProperty()

class Note(ndb.Model):
    user_email = ndb.GenericProperty()
    user_id_number = ndb.GenericProperty()
    noteName = ndb.StringProperty()
    noteContent = ndb.TextProperty()

class ToDo(ndb.Model):
    user_id_number = ndb.GenericProperty()
    todo_string = ndb.GenericProperty()

# [END GOOGLE DATASTORE 'KIND' INITILISATION]

# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]

# [START index]
@app.route('/')
def index():
    user = users.get_current_user()
    user_email = user.email()
    user_id_number = user.user_id()
    return render_template('index.html', user_email = user_email, user_id_number = user_id_number)
# [END index]

# [START home]
@app.route('/home')
def home():
    user = users.get_current_user()
    user_email = user.email()
    user_id_number = user.user_id()
    logout_url = users.create_logout_url('')
    Events = Event.query().filter(Event.user_id_number == user_id_number)
    Notes = Note.query().filter(Note.user_id_number == user_id_number)
    ToDos = ToDo.query().filter(ToDo.user_id_number == user_id_number)


    return render_template('home.html', Events = Events, Notes = Notes, ToDos = ToDos, user_email = user_email, user_id_number = user_id_number, logout_url = logout_url)
# [END home]

# [START login submitted]
@app.route('/login', methods=['POST'])
def login():
    user_email = request.form['user_email']
    user_id_number = request.form['user_id_number']

    form = Account(user_email = user_email, user_id_number = user_id_number)
    form.put()
# [END login submitted]

    # [START login render_template]
    return render_template(
    'login.html',
    user_email=user_email,
    user_id_number=user_id_number)
    # [END login render_template]

# [START event submitted]
@app.route('/submitted_form', methods=['POST'])
def submitted_form():
    user_email = request.form['user_email']
    user_id_number = request.form['user_id_number']
    eventName = request.form['eventName']
    eventDate = request.form['eventDate']
    eventLocation = request.form['eventLocation']
    eventDetails = request.form['eventDetails']

    form = Event(user_email = user_email, user_id_number = user_id_number, eventName = eventName, eventDate = eventDate, eventLocation = eventLocation, eventDetails = eventDetails)
    form.put()
# [END event submitted]

    # [START event render_template]
    return render_template(
        'submitted_form.html',
        user_email=user_email,
        user_id_number=user_id_number,
        eventName=eventName,
        eventDate=eventDate,
        eventLocation=eventLocation,
        eventDetails=eventDetails)
    # [END render_template]

# [START note submitted]
@app.route('/submitted_note', methods=['POST'])
def submitted_note():
    user_email = request.form['user_email']
    user_id_number = request.form['user_id_number']
    noteName = request.form['noteName']
    noteContent = request.form['noteContent']

    form = Note(user_email = user_email, user_id_number = user_id_number, noteName = noteName, noteContent = noteContent)
    form.put()
    # [END note submitted]

    # [START note render_template]
    return render_template(
        'submitted_note.html',
        user_email=user_email,
        user_id_number=user_id_number,
        noteName=noteName,
        noteContent=noteContent)
    # [END note render_template]

@app.route('/submiited_todo', methods=['POST'])
def submitted_todo():
    user_id_number = request.form['user_id_number']
    todo_string = request.form['todo_string']

    form = ToDo(user_id_number = user_id_number, todo_string = todo_string)
    form.put()

    return render_template(
    'submitted_todo.html',
    user_id_number=user_id_number,
    todo_string=todo_string
    )

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
