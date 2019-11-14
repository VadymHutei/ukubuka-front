import sys
sys.path.append('core')
# from pathlib import Path
from flask import render_template
from core import AbstractView
import config

class ShopView(AbstractView):

    def __init__(self):
        pass

    def render(self):
        return ''
