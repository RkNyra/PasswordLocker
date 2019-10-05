import unittest # Import the unittest module
from user import User # Import the User class
from credentials import Credentials # Import the Credentials class

class TestUser(unittest.TestCase):
  '''
  Test class that defines the test cases for the User class behavior.
  
  Args:
      unittest.TestCase: TestCase class that helps in creating cases.
  '''
  
  def setUp(self):
    '''
    Method to create a new instance of the User class before each test is run.
    '''
    
    self.new_user = User('Stl','pswd1234')
    
    # ======== FIRST (User Class) TEST - CORRECT INSTANTIATION ====
  def test__init__(self):
    '''
    Test if the creation of new User instances is properly done.
    '''
    self.assertEqual(self.new_user.username, 'Stl')
    self.assertEqual(self.new_user.password,'pswd1234')
    
    
    # ======= SECOND (User Class) TEST - SAVING NEW USER =======
  def test_save_new_user(self):
    '''
    Test if the user object is saved into the users list
    '''
    self.new_user.save_new_user() # saving the new user
    self.assertEqual(len(User.users),1)
    

class TestCredentials(unittest.TestCase):
  '''
  Test class that defines the test cases for the Credentials class behavior.
  
  Args:
    unittest.TestCase: TestCase class that helps in creating cases.
  '''

  def setUp(self):
    '''
    Method to create a new instance of the Credentials class before each test is run.
    '''
    self.new_credential = Credentials('twitter', 'SuperG', 'pwd333')
    
    # ======== FIRST (Credentials Class) TEST - CORRECT INSTANTIATION ====
  def test__init__(self):
    '''
    Test if the creation of new Credentials instances is properly done.
    '''
    self.assertEqual(self.new_credential.account, 'twitter')
    self.assertEqual(self.new_credential.acc_username, 'SuperG')
    self.assertEqual(self.new_credential.acc_password, 'pwd333')
  
    
    #======= SECOND (Credentials Class) TEST - SAVING NEW CREDENTIALS
  def test_save_new_credential(self):
    '''
    Test if the credential instance is saved into the credentials [] list.
    '''
    self.new_credential.save_new_credential() #saving the new credential instance/object
    self.assertEqual(len(Credentials.credentials),1)
    









    
if __name__ == '__main__':
  unittest.main()
