def send_slack_message(email: str, user: str, message: str) -> None:
    print(f"Hi {user} your email is {email}")
    print("Here's your slack message")
    print(message)
    print("------")