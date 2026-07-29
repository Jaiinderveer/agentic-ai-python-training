from flask import Flask, request, jsonify, render_template
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

cred = credentials.Certificate("day24/service-account-key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# create a directory in the root of project folder -> templates

# create flask app
app = Flask('MyApp')

@app.route('/') # applications root
def home(): 
   return render_template('register-user.html')

@app.route('/save-user', methods=['POST'])
def save_user_in_db():

    user = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': request.form['password'], # use sha to secure password
        'created_at': datetime.datetime.now()
    }

    # Save data in Firestore/MongoDB
    db.collection('users').add(user) # save user in firestore (registration operation)

    return render_template('home.html', name=user['name'])


if __name__ == '__main__':
    app.run(debug=True)


# Complete other CRUD Operations
# create HTML templates to save, update, list and delete with flask :)