# cSpell:disable
from flask import Flask, render_template, request
from random import random
import numpy, cv2, os
from datetime import datetime
from zipfile import ZipFile

app = Flask(__name__)
name_list = []



@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        name = request.form.get('Name')
        return render_template("form.html", name=name)


@app.route("/list", methods=["GET"])
def list():
    if request.method == "GET":
        name_list.clear()
        return render_template("douglas_list.html")


@app.route("/add-name", methods=["POST"])
def add_name():
    if request.method == "POST":
        name = request.form.get('Name')
        name_list.append(name)
        return render_template("douglas_list.html", name_list=name_list)


