# captchaTing.py

from datetime import datetime
import webbrowser
from flask import Flask, render_template, request
import _thread
import logging

tokens = []

def stamp():
    timestamp = str("["+datetime.utcnow().strftime("%H:%M:%S")+"]")
    return timestamp

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', methods=['GET', 'POST'])
@app.route('/solve', methods=['GET', 'POST'])

def solve():
    sitekey = "6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz" # SITEKEY GOES HERE FAM
    if request.method == "POST":
            token = request.form.get('g-recaptcha-response', '')
            tokens.append(token)
            count = len(tokens)
            print("{} stored token | {} total stored".format(stamp(), count))
    return render_template('index.html', sitekey=sitekey)

def harvestTokens():
    _thread.start_new_thread(app.run, ())
    webbrowser.open("http://supremenewyork.com:5000/solve") # WEB ADDRESS FOR SOLVING CAPTCHA GOES HERE FAM
    return

def main():
	print("captcha ting we out here")
	print("this shit was made by the real chef, cos he the real chef\n\n")
	harvestTokens()
	input("")

if __name__ == '__main__':
	main()
