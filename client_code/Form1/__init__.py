from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    email_address = "rinagoldberg13@gmail.com"
    anvil.server.call('send_email', email_address)


  def button_1_click(self, **event_args):
    # Get the text input from the text box
    text_input = self.name.text
    result = anvil.server.call('name', text_input)
    if result:
        self.result.visible = True 
        self.result.text = result.capitalize()

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call('classify_image', file)
    if result:
      self.img_r.visible=True
      self.img_r.text=result
    print(result)

  def classify_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Get the file data from the FileLoader component
    
    file_data = self.file_loader_2.file
    
    if file_data:
        # An image was sent
        print("Image sent")
        # Pass the file data to the 'main' function on the server side
        result = anvil.server.call('main', file_data)
        
        if result:
            self.img_r.visible = True
            self.img_r.source = result  # Assuming 'result' contains the URL of the image
        print(result)
    else:
        # No image was sent
        print("No image sent")
   
  from email_sender import send_email

email_sender.send_email(to='rinagoldberg13@gmail.com', subject='Hello', body='This is a test email!')


    
    
  




