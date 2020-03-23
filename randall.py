#!/usr/bin/env python3

import os
from flask import Flask, request, make_response, render_template

from config import get_env
from app import create_app


app = create_app(get_env('APP_ENV'))


#app= Flask(__name__)
#@app.route("/", methods=["GET"])

#def home():
#    """ Route to extend the home/default text """
    #rendering text
#    return 'Randal, Randal. Are you leaving without saying goodbye? '

if __name__ == '__main__':
    app.run()

    

