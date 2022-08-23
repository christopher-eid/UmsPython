from src.infrastructure.ums_infrastructure_abstraction.firebase_jwt_token.abstract_firebase_auth_service \
    import AbstractFirebaseAuthService

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
import pyrebase
import json

'''token creation and verification and refresh token inspired from:
   creation of access and refresh token: using pyrebase : https://github.com/thisbejim/Pyrebase
   verification of access tokens : using firebase_admin: https://firebase.google.com/docs/auth/admin/verify-id-tokens#python
   DO NOT FORGET TO DO pip install pyrebase4   not pyrebase lahala bcz: https://stackoverflow.com/questions/57333606/unknown-syntax-error-on-calling-pyrebase-in-python'''

class FirebaseAuthService(AbstractFirebaseAuthService):

    def __init__(self, firebase_engine):
        self.verify_engine = firebase_engine.get_verification_engine()
        self.generate_engine = firebase_engine.get_token_generating_engine()

    def sign_in_access_and_refresh_token(self, received_email: str, received_password: str) -> list:
        user = self.generate_engine.sign_in_with_email_and_password(received_email, received_password)
        return [user["idToken"], user["refreshToken"]]

    def refresh_token(self, received_refresh_token) -> str:
        user = self.generate_engine.refresh(received_refresh_token)
        return user["idToken"] #fresh token returned

    def verify_access_token(self, received_token) -> str:
        decoded_token = auth.verify_id_token(received_token)
        uid = decoded_token['uid']
        return uid


