#!/usr/bin/env python3

import os
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from flask_api import FlaskAPI
from config.env import app_env

#from ..app.utils.slackhelper import SlackHelper
from .utils.slackhelper import SlackHelper
from flask import request, jsonify
from re import match
from app.actions import Actions


allowed_commands = [
    'new-tip'
    'show-tip'
    'help'
]

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')


#    @app.route("/", methods=["GET"])
#    def home():
#       """ Render sample text for the home route"""
#       #rendering test
#        return 'Hello Randal, I am your Security Awareness application'

    @app.route("/randall", methods=['POST'])
    def randall(): 
        command_text = request.data.get('text')
        command_text = command_text.split(' ')
        slack_uid = request.data.get('user_id')
        slackhelper = SlackHelper()
        slack_user_info = slackhelper.user_info(slack_uid)
        actions =Actions(slackhelper, slack_user_info) 

    return app
