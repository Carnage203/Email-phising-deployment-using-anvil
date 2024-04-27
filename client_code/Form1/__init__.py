from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def Check_click(self, **event_args):
    """This method is called when the button is clicked"""
    Mail=anvil.server.call('Check',
                        self.Link.text)
    if Mail=="true":
      self.Mail.visible=True
      self.Mail.text="Not Safe"
    else:
      self.Mail.visible=True
      self.Mail.text="Safe"
