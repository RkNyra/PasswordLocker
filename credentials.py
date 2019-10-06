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
    
    
  #========= generate new password =============
    
  def generate_password(self, size=7, character=string.ascii_lowercase+string.digits+string.punctuation):
    '''
    Method to generate a 7 character password.
    '''
    generate_password = ''.join(random.choice(character) for _ in range(size))
    return generate_password
  
  
  
  #=============== viewing accounts & creds created ===========
  
  @classmethod
  def view_credentials(cls):
    '''
    Method to view/display all the created and saved account credentials.
    '''
    for credential in cls.credentials:
     return credential 
   
  #============== find creds by account name ==============
  
  @classmethod
  def find_by_account_name(cls, account):
    '''
    Method that takes in the account name and returns the credential that matches that account name
    
    Args: 
      account: account name to search for
    Returns:
      credential that matches that account
    '''
    
    for credential in cls.credentials:
      if credential.account == account:
        return credential
  
  
  #============== deleting obsolete credentials ===========
  
  def delete_obsolete_credential(self):
    '''
    Method to delete an obsolete credential/delete a credential account that is no longer needed in the application.
    '''
    
    Credentials.credentials.remove(self)
    
