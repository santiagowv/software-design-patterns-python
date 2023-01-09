from __future__ import annotations
from random import randint
from abc import ABC, abstractmethod

def send_email(email:str, subject:str, body:str) -> None:
    print(f"Email sent to:{email}")
    print(f"Subject:{subject}")
    print("----------------")
    print(body)
    print("----------------")

class EventHandler(ABC):
    @abstractmethod
    def attach(self, user:User) -> None:
        pass
    
    @abstractmethod
    def detach(self, user:User) -> None:
        pass

class AccountMgmtHanlder(EventHandler):
    observers = []
        
    def attach(self, user:User) -> None:
        print("Account added to management handler.")
        self.observers.append(user)
        self.user_registered(user)

    def detach(self, user:User) -> None:
        self.observers.remove(user)
        print("You'll no longer receive our emails")

    def user_registered(self, user:User) -> None:
        if user in self.observers:
            send_email(email = user.email, subject = f"Welcome {user.name}", 
                       body = "It's a pleasure to have you in our team!")

    def reset_password(self, user:User) -> None:
        if user in self.observers:
            send_email(email = user.email, subject = "Reset password",
                       body = "Please go to the following link to setup your new password.")

    def change_username(self, user:User) -> None:
        if user in self.observers:
            send_email(email = user.email, subject = "Change your username",
            body = "Please go to the following link to change your username")

class User:
    def __init__(self, id:str, name:str, email:str, job_title:str):
        self.id = id
        self.name = name
        self.email = email
        self.job_title = job_title

class CrmApplication:
    users = []

    def generate_id(self):
        return randint(10000, 20000)

    def __init__(self, app_name:str):
        self.id = self.generate_id()
        self.app_name = app_name
        self.account_handler = AccountMgmtHanlder()
    
    def create_user(self, name:str, email:str, job_title:str) -> None:
        print("Adding new user to the database")
        new_user = User(self.generate_id(), name = name, email = email, job_title = job_title)
        self.users.append(new_user)
        self.account_handler.attach(new_user)

    def delete_from_email_list(self, email:str) -> None:
        user = self.find_user(email)
        self.account_handler.detach(user)

    def find_user(self, email:str) -> User:
        for user in self.users:
            if user.email == email:
                return user
        print(f"User with email: {email} not found")

    def password_forgotten(self, email:str) -> None:
        user = self.find_user(email)
        self.account_handler.reset_password(user)

    def change_username(self, email:str) -> None:
        user = self.find_user(email)
        self.account_handler.change_username(user)

if __name__ == "__main__":
    company = CrmApplication("campbi.com")

    company.create_user("santiago", "santiagowilchesv@gmail.com", "data analyst")
    company.password_forgotten("santiagowilchesv@gmail.com")
    company.delete_from_email_list("santiagowilchesv@gmail.com")
    company.change_username("santiagowilchesv@gmail.com")

    company.create_user("andres", "andresgarcia@gmail.com", "director")
    company.change_username("andresgarcia@gmail.com")
