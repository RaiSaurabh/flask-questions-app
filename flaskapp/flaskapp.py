# This is the Peak front-end.

from flask import Flask, render_template, flash, redirect, request

from flaskapp.forms import QuestionForm

import requests
import os
#Openapi
import openai

application = Flask(__name__)
application.secret_key = os.environ['FLASK_SECRET']

openai.api_key  = os.environ['API_SECRET']

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

@application.route('/healthz')
def healthz():
    """
    Check the health of this peakweb instance. OCP will hit this endpoint to verify the readiness
    of the peakweb pod.
    """
    return 'OK'

@application.route('/')
def index():
    return render_template('chatbot.html')

@application.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)
    return response

@application.route('/new_question/', methods=('GET', 'POST'))
def new_question():
    form = QuestionForm()
    if form.validate_on_submit():
        flash("Successfully submitted question \"%s\"" % (form.summary.data))
        return redirect('/new_question/')

    return render_template('newquestion.html', form=form)
