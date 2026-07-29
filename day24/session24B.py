"""
    Firestore -> Product by Google, available as a databse in firebase stack
    it saves data in hierarchy

    collection/document/collection/document....

    /users/
        john
            {}
            /orders/
            o1{}
            o2{}
            o3{}
            /address
            /transactions
                upi/
                    {}
                    {}
                    {}
                card/
                netbanking/
        jim
            {}
            /orders
            o1{}
            o2{}
        jennie
            {}

"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("service-account-key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
print('Firestore: DB Connection Created...')