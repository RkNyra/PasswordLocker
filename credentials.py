import string
import random
import pyperclip

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
    
  def generate_password(self, size=7, character=string.ascii_lowercase+string.digits):
    '''
    Method to generate a 7 character alphanumeric password.
    '''
    generated_password = ''.join(random.choice(character) for _ in range(size))
    return generated_password
  
  
  
  #============ viewing accounts & creds created ===========
  
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
    
  #======== check whether credential exists ==========
  
  @classmethod
  def credential_exists(cls, account):
    '''
    Method to check whether a credential exist in the credentials list.
    
    Args:
      account: account name to search whether a credential exists.
    Returns:
      Boolean: True or false depending on whether or not a credetial exists.
    '''
    
    for credential in cls.credentials:
      if credential.account == account:
        return True
    
    return False
  
  
  #======= copy password =============
  
  @classmethod
  def copy_password(cls,account):
      '''
      Method to copy password
      '''
      credential = Credentials('Skype','Stl','pwd333')
      credential.save_new_credential()
      found_credential = Credentials.find_by_account_name('Skype')
      pyperclip.copy(found_credential.acc_password)
    
