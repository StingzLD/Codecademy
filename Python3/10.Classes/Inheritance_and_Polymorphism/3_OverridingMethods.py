class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username

  # Only allow editing of the message if the user is the sender.  
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text
  
class Admin(User):
  # Override the User's method to allow it edit the message, even if it is not the owner.
  def edit_message(self, message, new_text):
    message.text = new_text