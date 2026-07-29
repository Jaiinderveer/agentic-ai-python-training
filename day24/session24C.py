import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

cred = credentials.Certificate("day24/service-account-key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def create_task(task):
    result = db.collection('tasks').add(task)
    # print('Task Created', result)
    print('Task Created', result[1].id) # gets document id as well

def get_all_tasks():
    # docs = db.collection('tasks').stream()
    docs = db.collection('tasks').where('status','==','pending').stream()
    for task in docs:
        print(task.id)
        print(task.to_dict())
        print('~~~~~~~~~~~~~~')

def delete_task(id):
    db.collection('tasks').document(id).delete()
    print('Task Deleted...')

def update_task(id):
    task = {
        'title': 'Email james',
        'description': 'Email james and ask him status on bus ticketing solution',
        'status': 'completed',
        'priority': 'medium',
        'created_at': datetime.datetime.now()
    }
    db.collection('tasks').document(id).update(task)
    print('Task Updated...')


task = {
    'title': 'Email james',
    'description': 'Email james and ask him status on bus ticketing solution',
    'status': 'pending',
    'created_at': datetime.datetime.now()
}

# create_task(task)
get_all_tasks()
# delete_task('AdEzKNYdNDRyHJsfhyfh') # pass task id
# update_task('PeFLUKdqHCRr717iULRo')