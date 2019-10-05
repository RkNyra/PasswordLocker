class Credentials:
  '''
  Class that generates new instances of credentials/account passwords.
  '''
  
  credentials = [] # Class variable - an empty credentials list
  
  def __init__ (self,account,acc_username,acc_password):
    self.account = account
    self.acc_username = acc_username
    self.acc_password = acc_password