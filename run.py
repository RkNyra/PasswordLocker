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

#==== verify existing user ==============
def verify_user(username, password):
  '''
  Function that verifies the existence of the user before login in.
  '''
  check_existing_account = User.check_user_exists(username)
  return check_existing_account

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
  
#===== delete an obsolete credential =======
def delete_obsolete_credential(credential):
  '''
  Function to delete an obsolete credential
  '''
  Credentials.delete_obsolete_credential(credential)
  
#======= finding a saved credential =======
def find_credential(account):
  '''
  Function that finds a credential by its account name and returns the credential
  '''
  return Credentials.find_by_account_name(account)

#======= checking for existing credential =======
def check_existing_credential(account):
  '''
  Function that checks, by account name, whether a credential exists and return a Boolean.
  '''
  return Credentials.credential_exists(account)

#======= view/display all credentials =======
def display_credentials():
  '''
  Function that returns/displays all saved credentials.
  '''
  return Credentials.view_credentials()

# #======= generating a password =======
# def auto_gen_password():
#   '''
#   Functions that enables the auto-generation of passwords
#   '''
#   return Credentials.generate_password(self, size=7, character=string.ascii_lowercase+string.digits+string.punctuation)


#======= copying a credential password ======
def copy_credential_password(account):
  '''
  Function that copies the password of a selected credential.
  '''
  return Credentials.copy_password(account)


#======= MAIN() -  calling the defined functions =======
#=======================================================
def main():
  print(' ')
  print('Hi there!')
  print(' ')
  print('WELCOME TO PASSWORD LOCKER')
  print(' ')
  print('*'*60)
  print(' ')
  while True:
    print('Do you have a Password Locker account? Select: (yes or no)')
    print(' ')
    status = input()
  
    if status == 'yes':
      print(' ')
      print('Log In to Your Account')
      print('='*60)
      print(' ')
      username = input('Enter your username: ').strip()
      password = input('Enter your password: ').strip()
    
      user_exists = verify_user(username,password)
      if user_exists == True:
        print(' ')
        print('*'*60)
        print(f'Welcome {username}! Please select an option to proceed')
        print('='*60)
        print(' ')
        
        # while True:
        #   print('-'*60)
        #   print('''Use these short codes:
        #       cc - create new credential
        #       dc - display credential
        #       fc - find a credential
        #       del - delete credential
        #       copy - copy account password
        #       x - exit the credential display mode''')
        #   short_code = input('Type your choice: ').lower().strip()
          
        #   if short_code == 'cc':
        #     while True:
        #       print(' ')
        #       print('Create a new account credentials by: ')
        #       print('-'*70)
        #       account = input('Enter the account name (e.g Linked In): ').strip()
        #       acc_username = input('Enter your preferred username: ').strip
        #       print('''Select one:
        #             1. create your own passowrd
        #             OR
        #             2. have one generated for you ''')
        #       selection = input(int())
        #       if selection == 1:
        #         acc_password = input('Enter your preferred password: ').strip
        #       elif selection == 2:
        #         acc_password = Credentials.generate_password
        #       else:
        #         print('Invalid. Please select a valic selection')
        #       save_new_credential(create_credential(
        #           account, acc_username, acc_password))
        #       print(' ')
        #       print(
        #           f'New account & credentials created for: {account}, using username - {acc_username} and password - {password}.')
        #       break
        #   elif short_code == 'dc':
        #     print(' ')
        #     if display_credentials():
        #       print('Your saved account credentials include: ')
        #       print('-'*70)
        #       print(display_credentials())
        #     else:
        #       print('You don\'t seem to have any saved credentials yet.')
        #   elif short_code == 'fc':
        #     search_account = input(
        #         'Enter the account_name you wish to find/search-for: ')
        #     if check_existing_credential(account):
        #       search_account = find_credential(account)
        #       print(
        #           f'{search_account.account}, {search_account.acc_username}, {search_account.acc_password}')
        #     else:
        #       print('That account/account-credential does not exist')
        #       print(' ')
        #       print('-'*70)
        #       print(find_credential(account))
        #   elif short_code == 'del':
        #     print('Delete a credential you no longer need: ')
        #     print(' ')
        #     print('-'*70)
        #     chosen_for_delete = input('Select account to delete: ')
        #     print(display_credentials())
        #     print(delete_obsolete_credential(chosen_for_delete))
        #   elif short_code == 'copy':
        #     print(' ')
        #     chosen_for_copy = input(
        #         'Enter the account name for the credential password to copy: ')
        #     copy_credential_password(chosen_for_copy)
        #     print('')
        #   elif short_code == 'x':
        #     print('Thanks for your time! :) Goodbye...')
        #     break
        #   else:
        #     print('I didn\'t quite catch that, please use the given short codes.')
        #   break
      
      else:
        print(' ')
        print('='*60)
        print('This Password-Locker account does not exist.')
        print(' ')
        print('Please proceed to create an account...')
        print(' ')
        print('='*60)
        print(' ')
        print('Register:')
        print('-'*60)
        register = input('Enter your preferred username: ')
        
        if register in User.users:
          print('Account already exists! Log in instead')
          print('Log in')
          print('-'*60)
          username = input('Enter your username: ').strip()

        else:
          password = input('Enter your password: ').strip()
          save_new_user(create_pswdlckr_account(username, password))

          print('\nAccount Created! Proceed to Log In.\n')
          print('Log in')
          print('-'*60)
          username = input('Enter your username: ').strip()
          password = input('Enter your password: ').strip()
        
        while True:
          print('-'*60)
          print('Hey there,', username,'!')
          print(' ')
          print('''Let's explore these Password Locker Options: - Select from: 
              1 - Create new credential
              2 - Display credential
              3 - Find a credential
              4 - Delete credential
              5 - Copy account password
              x - Exit the credential display mode''')
          short_code = input('Enter your choice: ')
          
          if short_code == '1':
            while True:
              print(' ')
              print('Create a new account credentials: ')
              print('-'*60)
              account = input('Enter the account name (e.g Gmail): ').strip()
              acc_username = input('Enter your preferred username: ').strip()
              
              print(' ')
              print('For password, select either a or b:')
              print(' ')
              print('   a - Custom-make: Write your own password')
              print('   b - Auto-generate: Get auto-generated password')
              print(' ')
              
              selection = input('Select a or b: ')
              acc_password = selection
              if selection == 'a':
                acc_password = input('Type your custom password: ')
                
              elif selection == 'b':
                acc_password = Credentials.generate_password(acc_password)
              else:
                print('Please select a valid option')
                
              save_new_credential(create_credential(account, acc_username, acc_password))
              print(acc_username)
              print(' ')
              print(f'''Credential created,
                  Account: {account}
                  Acc_Username: {acc_username}
                  Acc_Password: {acc_password}''')
              print(' ')
              # continue
              
              print('Do you want to create another credential? Select: yes or no')
              add_another_option = input('Select yes or no: ')
              
              if add_another_option == 'yes':
                continue
              elif add_another_option == 'no':
                break
              else:
                print('Select a valid option')
              
          elif short_code == '2':
              
                print('Your saved account credentials include: ')
                print('-'*60)
                while True:
                  print(display_credentials())
                  break
                else:
                  print('You don\'t seem to have any saved credentials yet.')
                  break
          elif short_code == '3':
            search_account = input('Enter the account_name you wish to find/search-for: ')
            if check_existing_credential(account):
              search_account = find_credential(account)
              print(
                  f'{search_account.account}, {search_account.acc_username}, {search_account.acc_password}')
            else:
              print('That account/account-credential does not exist')
              print(' ')
              print('-'*60)
              print(find_credential(account))
          elif short_code == '4':
            while True:
              print('Delete a credential you no longer need: ')
              print(' ')
              print('-'*60)
              chosen_for_delete = input('Select account to delete: ')
              print(display_credentials())
              print(delete_obsolete_credential(chosen_for_delete))
              break
          elif short_code == '5':
            print(' ')
            chosen_for_copy = input(
                'Enter the account name for the credential password to copy: ')
            copy_credential_password(chosen_for_copy)
            print('')
          elif short_code == 'x':
            print('Thanks for your time! :) Goodbye...')
            break
          else:
            print('I didn\'t quite catch that, please use the given short codes.')
          break
          
          
    elif user_exists !=True or status == 'no':
      register = input('Register: Enter your preferred username: ')
      if register in User.users:
        print('Account already exists! Log in instead')
        print('Log in')
        print('-'*60)
        username = input('Enter your username: ').strip()
        
      else:
        password = input('Enter your password: ').strip()
        save_new_user(create_pswdlckr_account(username, password))
        
        print('\n Account Created! Proceed to Log In.\n')
        username = input('Enter your username: ').strip()
        password = input('Enter your password: ').strip()
    else:
      print('Invalid Selection: Please type in a valid selection: (Either yes or no).')
    
if __name__ == '__main__':
  
    main()
