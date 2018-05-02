# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cgi
import textwrap
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import datastore

user = users.get_current_user()
user_email = user.email()
user_id_number = user.user_id()

class Account(ndb.Model):
    user_email = ndb.GenericProperty()
    user_id_number = ndb.GenericProperty()

class EventForm(ndb.Model):
    user_email = ndb.GenericProperty()
    user_id_number = ndb.GenericProperty()
    eventName = ndb.StringProperty()
    eventDate = ndb.StringProperty()
    eventLocation = ndb.StringProperty()
    eventDetails = ndb.TextProperty()

class NoteForm(ndb.Model):
    user_email = ndb.GenericProperty()
    user_id_number = ndb.GenericProperty()
    noteName = ndb.StringProperty()
    noteContent = ndb.TextProperty()

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
    eventForms = EventForm.query()
    noteForms = NoteForm.query()
    return render_template('index.html', eventForms = eventForms, noteForms = noteForms, user_email = user_email, user_id_number = user_id_number)
# [END index]

# [START form]
@app.route('/form')
def form():
    return render_template('form.html')
# [END form]

# [START note]
@app.route('/note')
def note():
    return render_template('note.html')
# [END note]

@app.route('/login', methods=['POST'])
def login():
    user_email = request.form['user_email']
    user_id_number = request.form['user_id_number']

    form = Account(user_email = user_email, user_id_number = user_id_number)
    form.put()

    return render_template(
    'login.html',
    user_email=user_email,
    user_id_number=user_id_number)

# [START submitted]
@app.route('/submitted_form', methods=['POST'])
def submitted_form():
    user_email = request.form['user_email']
    user_id_number = request.form['user_id_number']
    eventName = request.form['eventName']
    eventDate = request.form['eventDate']
    eventLocation = request.form['eventLocation']
    eventDetails = request.form['eventDetails']

    form = EventForm(user_email = user_email, user_id_number = user_id_number, eventName = eventName, eventDate = eventDate, eventLocation = eventLocation, eventDetails = eventDetails)
    form.put()
    # [END submitted]

    # [START render_template]
    return render_template(
        'submitted_form.html',
        user_email=user_email,
        user_id_number=user_id_number,
        eventName=eventName,
        eventDate=eventDate,
        eventLocation=eventLocation,
        eventDetails=eventDetails)
    # [END render_template]

# [START submitted]
@app.route('/submitted_note', methods=['POST'])
def submitted_note():
    user_email = request.form['user_email']
    user_id_number = request.form['user_id_number']
    noteName = request.form['noteName']
    noteContent = request.form['noteContent']

    form = NoteForm(user_email = user_email, user_id_number = user_id_number, noteName = noteName, noteContent = noteContent)
    form.put()
    # [END submitted]

    # [START render_template]
    return render_template(
        'submitted_note.html',
        user_email=user_email,
        user_id_number=user_id_number,
        noteName=noteName,
        noteContent=noteContent)
    # [END render_template]

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
