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