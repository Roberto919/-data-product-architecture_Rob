from flask import Flask, url_for

app = Flask(__name__)

@app.route('/user/<string:username>')
def show_user_profile(username):
    return "Hello user {}".format(username)
