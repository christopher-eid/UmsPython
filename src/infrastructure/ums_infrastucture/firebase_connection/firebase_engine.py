import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
import pyrebase
import json
import os
from pathlib import Path
#make sure to download pyrebase4 not pyrebase : pip install pyrebase4
#download pyrebase 4 bcz: https://stackoverflow.com/questions/57333606/unknown-syntax-error-on-calling-pyrebase-in-python


class FirebaseEngine:

    def get_token_generating_engine(self):#pyrebase is used to create token and refresh tokens
        with open("./pyrebase_env.json") as json_file:
            cred1 = json.load(json_file)

        firebase1 = pyrebase.initialize_app(cred1)
        auth1 = firebase1.auth()
        return auth1

    def get_verification_engine(self): #i used firebase_admin to verify the idtokens

        #.src/infrastructure/ums_infrastructure/firebase_connection/google_env.json
        #file_location = os.path.join(os.getcwd(), 'src', 'infrastructure', 'ums_infrastructure', 'firebase_connection', 'google_env.json')
        cred = credentials.Certificate("./google_env.json")
        firebase = firebase_admin.initialize_app(cred)
        return firebase
