from flask import Flask, render_template, request, url_for, session, redirect
import json
import pymongo
from pymongo import MongoClient
import bcrypt
from bson import json_util


app=Flask(__name__)

cluster = MongoClient("mongodb+srv://root:root@test-6janc.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["bday"]
collection = db["responses"]


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/thank", methods=["GET"])
def thank():
    return render_template('thank.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
            collection.insert({'name' : request.form['name'],'meet' : request.form['meet'],'like' : request.form['like'],'memory' : request.form['memory'],'message' : request.form['message'] })
            return redirect(url_for('thank'))
    return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = "mysecretkey"
    app.run()

