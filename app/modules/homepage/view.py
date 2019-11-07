from flask import render_template

class View():

    def __init__(self):
        print('View created')

    def render(self):
        return render_template('homepage.html')
