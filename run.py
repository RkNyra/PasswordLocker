#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_pswdlckr_account(username,password):
  '''
  Function to create a new password locker account
  '''
  new_user = User(username,password)
  return new_user