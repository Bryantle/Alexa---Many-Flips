from flask import Flask, render_template
from flask_ask import Ask, question, session, statement
import logging
from random import randint

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@app.launch
def launcher():
    return question('start')

@app.intent("yesIntent")
def yes():
    return question('yes')

@app.intent('noIntent')
def no():
    return statement('no')

@app.intent("numberOfFlipsIntent", convert = {'number': int})
def no_flips(number):
    side = [randint(0,2) for i in range(number)]
    heads = len([for i in side if i == 0])
    tails = len([for i in side if i == 1])
    message = "From {} flips, I have {} heads and {} tails.".format(number,heads,tails)
    return statement(message)

@app.session_ended
def end():
    return statement('end')

if __name__ == "__main__":
    app.run(debug = True)
