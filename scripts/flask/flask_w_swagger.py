from flask import Flask, request
from flask_restplus import Api, Resource
app = Flask(__name__)
api = Api(app)

users = {'lmillan': {'role': 'admin',
                     'privileges': 'all'},
         'jramos': {'role': 'user',
                    'privileges': 'readonly'}}

@api.route("/user/<string:username>")
class UserProfile(Resource):

    # método get
    def get(self, username):
        return users[username]

    # método put
    def put(self, username):
        users[username] = request.form['user_data']
        return users[username]

if __name__ == '__main__':
    app.run()