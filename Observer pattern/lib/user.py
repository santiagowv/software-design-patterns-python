from random import randint
from api.event import post_event
users = []

class User:
    def __init__(self, id, name, email, job_title):
        self.id = id
        self.name = name
        self.email = email
        self.job_title = job_title

def generate_id():
    return randint(10000, 20000)

def find_user(email: str):
    for user in users:
        if user.email == email:
            return user
    print(f"User with {email} not found")

def create_user(name:str, email:str, job_title:str):
    print("Adding new user to the database")
    new_user = User(generate_id(), name = name, email = email, job_title = job_title)
    users.append(new_user)
    post_event("user_registered", new_user)

def password_forgotten(email: str):
    user = find_user(email)
    post_event("password_forgotten", user)