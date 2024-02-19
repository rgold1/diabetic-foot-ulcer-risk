from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    # Get the text input from the text box
    f_name = self.f_name.text
    l_name=self.l_name.text
    email=self.email.text
    result=anvil.server.call('main', f_name,f_name,l_name)
    if result=="Success":
      self.result.visible=True
      self.result.text="The result has been sent to you at "+email
      
    

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""

  def classify_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Get the file data from the FileLoader component
    f_name = self.f_name.text
    l_name=self.l_name.text
    email=self.email.text
    file_data = self.file_loader_2.file 
    if self.f_name.text=="":
      print("error")
    if file_data:
        # An image was sent
        print("Image sent")
        # Pass the file data to the 'main' function on the server side
        result=anvil.server.call('main', file_data,f_name,l_name,email)


        
     
    
  




