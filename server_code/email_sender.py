import anvil.email
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def send_email(address):
    anvil.email.send(
      from_name="Anvil Forum",
      to=address,
      subject="Have you used the Anvil Forum?",
      html='The Anvil <a href="https://anvil.works/forum">Forum</a> is friendly and informative.',
      text="The Anvil Forum (https://anvil.works/forum) is friendly and informative.",
    )