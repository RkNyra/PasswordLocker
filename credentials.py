import string
import random

class Credentials:
  '''
  Class that generates new instances of credentials/account passwords.
  '''
  
  credentials = [] # Class variable - an empty credentials list
  
  def __init__ (self,account,acc_username,acc_password):
    self.account = account
    self.acc_username = acc_username
    self.acc_password = acc_password
    
  #============ save_new_credentials ===========
  
  def save_new_credential(self):
    '''
    Method that saves each new instance of credentials in the credentials [] list.
    '''
    Credentials.credentials.append(self)
    
  def generate_password(self, size=10, char=string.ascii_lowercase+string.digits):
    '''
    Method to generate a 10 character password.
    '''
    generate_password = ''.join(random.choice(char) for _ in range(size))
    return generate_password
    