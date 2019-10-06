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
def save_account(credential):
  '''
  Function to save new pswdlckr user account
  '''
  credential.save_account()

#===== delete an existing password locker user account =====
def del_account(credential):
  '''
  Function to delete a credential user account
  '''
  credential.delete_account()