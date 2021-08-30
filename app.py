import os
import requests
import urllib.parse
import re

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import *

# Config flask application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Setting var
        result = " "
        sentence = request.form.get("input")

        # Setting conditions & Display result
        if not sentence:
            result = "Fill this form"

        if "generate" in request.form:
            result = generate_password(sentence)

        return render_template("index.html", result=result)

    else:
        return render_template("index.html")