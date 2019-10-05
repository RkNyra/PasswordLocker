class User:
  '''
  Class that creates and stores user's username and password for the Password Locker account.
  '''
  users = [] #Create an empty (Password Locker) users list
  
  def __init__(self,username,password):
    '''
    __init__method to define properties for each user instance/object.
    '''
    self.username = username
    self.password = password
    
  def save_new_user(self):
    '''
    save_new_user method to save User objects into users list
    '''
    User.users.append(self)