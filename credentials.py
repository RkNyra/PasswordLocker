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