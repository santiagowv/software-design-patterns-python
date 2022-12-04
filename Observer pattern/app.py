from lib.user import create_user, password_forgotten
from api.email_listener import setup_email_event_handlers

setup_email_event_handlers()

create_user("Santiago", "santiagowilches@gmail.com", "Data engineer")
password_forgotten("santiagowilches@gmail.com")