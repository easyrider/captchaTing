# captchaTing.py


from functions import storeTokens

from datetime import datetime
import webbrowser
from flask import Flask, render_template, request
import _thread
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', methods=['GET', 'POST'])
@app.route('/solve', methods=['GET', 'POST'])

tokens = {}

def solve():
    sitekey = "6Ld80SYTAAAAABkkLnWCwycH-8K9axi95wjeG7lb" # SITEKEY GOES HERE FAM
    if request.method == "POST":
            token = request.form.get('g-recaptcha-response', '')
            tokens.append(token)
            print("stored token using {}".format(sitekey))
    return render_template('index.html', sitekey=sitekey)

def harvestTokens():
    _thread.start_new_thread(app.run, ())
    webbrowser.open("http://supremenewyork:5000/solve") # WEB ADDRESS FOR SOLVING CAPTCHA GOES HERE FAM
    return

def main():
	print("captcha ting we out here")
	print("this shit was made by the real chef, cos he the real chef\n\n")
	harvestTokens()

if __name__ == '__main__':
	main()