import unittest # Import the unittest module
from user import User # Imiport the User class

class TestUser(unittest.TestCase):
  '''
  Test class that defines the test cases for the User class behavior.
  
  Args:
      unittest.Testcase: TestCase class that helps in creating cases.
  '''
  
  def setUp(self):
    '''
    Method to create a new instance of the User class before each test case to be declared.
    '''
    
    self.new_user = User('Stl','pswd1234')
    
    # ======== FIRST TEST - CORRECT INSTANTIATION ====
  def test__init__(self):
    '''
    Test if the creation of new User instances is properly done.
    '''
    self.assertEqual(self.new_user.username, 'Stl')
    self.assertEqual(self.new_user.password,'pswd1234')
    
    
    # ======= SECOND TEST - SAVING NEW USER =======
  def test_save_new_user(self):
    '''
    Test if the user object is saved into the users list
    '''
    self.new_user.save_new_user() # saving the new user
    self.assertEqual(len(User.users),1)
    
    
if __name__ == '__main__':
  unittest.main()