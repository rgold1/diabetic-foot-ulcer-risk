from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.



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
  




