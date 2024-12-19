import hashlib
import time

#Simple Token Generator
tokens={}

def generate_token(user_id):
    token=hashlib.sha256(f"{user_id}{time.time()}".encode()).hexdigest()
    tokens[token]=user_id
    return token

def verify_token(token):
    return tokens.get(token)