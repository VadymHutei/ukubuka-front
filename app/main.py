from flask import Flask, render_template
from modules.homepage.ctrl import Homepage

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    inst = Homepage()
    return inst.getPage()
