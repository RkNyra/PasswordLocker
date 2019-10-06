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
  
  def tearDown(self):
    '''
    Method that cleans up after each test case has run
    '''
    
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
  
  def tearDown(self):
      '''
    Method that cleans up after each test case has run
    '''
  
  
    # ======== FIRST (Credentials Class) TEST - CORRECT INSTANTIATION ====
  def test__init__(self):
    '''
    Test if the creation of new Credentials instances is properly done.
    '''
    self.assertEqual(self.new_credential.account, 'twitter')
    self.assertEqual(self.new_credential.acc_username, 'SuperG')
    self.assertEqual(self.new_credential.acc_password, 'pwd333')
  
    
    # ======= SECOND (Credentials Class) TEST - SAVING NEW CREDENTIALS
  def test_save_new_credential(self):
    '''
    Test if the credential instance is saved into the credentials [] list.
    '''
    self.new_credential.save_new_credential() #saving the new credential instance/object
    self.assertEqual(len(Credentials.credentials),2)
    
    
# to consider - test for auto/comp-generated password
#             - test for custom/user-typed/chosen password
#             - test for finding acc creds by accountName.



#======= TEST - VIEWING SAVED ACC. CREDENTIALS =======
  def test_view_credentials(self):
    '''
    Test whether one can view all the account credentials that they have created/saved.
    '''
    self.new_credential.save_new_credential()
    account_2 = Credentials('facebook', 'StlSuperG', 'pswd1234')
    account_2.save_new_credential()
    self.assertEqual(len(Credentials.credentials),4)




#=========== TEST - DELETING OBSOLETE CREDENTIAL(S) ===========  
  def test_delete_obsolete_credential(self):
    '''
    method to test whether one can delete account credentials that are obsolete.
    '''
    self.new_credential.save_new_credential()
    test_credential = Credentials('twitter','Chyle','chyle3377')
    test_credential.save_new_credential()
    self.new_credential.delete_obsolete_credential()
    self.assertEqual(len(Credentials.credentials),1)
  
print(Credentials.credentials)







    
if __name__ == '__main__':
  unittest.main()
