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
  
  @classmethod
  def check_user_exists(cls,username):
    '''
    Method to check whether or not a user account exists in the users list.
    
    Args:
      username: username to search whether or not a user account exists.
    Returns:
      Boolean: True or false depending on whether or not a user account exists.
    '''
    for user in cls.users:
      if user.username == username:
        return True
    
    return False