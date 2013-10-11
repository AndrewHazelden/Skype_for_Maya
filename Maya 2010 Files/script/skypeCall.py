"""
SkypeCall V1.0 Build 3 - Oct 11, 2013
Call a Skype Contact from the Maya Shelf
Script by Andrew Hazelden
------------------------------------------------
Available SkypeCall shelf icon names:
skypeMiniCall.png
skypeCall.png
skypeCallTest.png
skypeNewContact.png


Script Usage Example:
import skypeCall
reload(skypeCall)
skypeCall.openSkypeCall('echo123')

"""

def openSkypeCall( contact ):
  """ Run the Skype call function """
  import webbrowser
  #contact = 'echo123'
  
  # Skype Support Chat Contact
  url = 'skype:' + contact + '?call'
  
  # Open URL in Skype
  print('Skype Calling: ' + contact);
  webbrowser.open_new(url)

