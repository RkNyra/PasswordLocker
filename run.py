#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

#==== create user account ======
def create_pswdlckr_account(username,password):
  '''
  Function to create a new password locker account
  '''
  new_user = User(username,password)
  return new_user

#===== save the newly created account ====
def save_new_user(user):
  '''
  Function to save new pswdlckr user account
  '''
  User.save_new_user(user)

#====== create a credential =====
def create_credential(account,acc_username,acc_password):
  '''
  Function to create a new credential
  '''
  new_credential = Credentials(account,acc_username,acc_password)
  return new_credential

#===== save the newly created credential =======
def save_new_credential(credential):
  '''
  Function to save credential
  '''
  Credentials.save_new_credential(credential)