from lib.email import send_email
from api.event import subscribe

def handle_user_registered_event(user):
    send_email(user.email, user.name, "Welcome to our company is a pleasure to have you in our team!")

def handle_user_password_forgotten(user):
    send_email(user.email, user.name, "Please user this link to recover your password")

def setup_email_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("password_forgotten", handle_user_password_forgotten)
