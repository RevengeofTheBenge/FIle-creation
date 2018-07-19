import time
import os
import hashlib

iflogin = False

filename = ""

usr = ""

def md5hash(s):
     hash_object = hashlib.md5(s.encode())
     return hash_object.hexdigest()

def spaces():
     for i in range(1,99):
          print(" ")

def percentage(s):
     for i in range(1, 101):
          print(s +"... " + str(i) + "%")

def login():
     global usr
     global iflogin
     global filename
     print("")
     usr = input("Please enter a username: ")
     pas = input("Please enter a password: ")
     filename = usr + pas  
     filename = md5hash(filename) + ".txt"
     percentage("Logging in")
     print("Logged in.")
     iflogin = True
     
def accountcreator():
     global iflogin
     global filename
     spaces()
     input("You are about to create an account. Press <ENTER> to continue.")
     if iflogin == False:
          login()
          time.sleep(1.5)
          spaces()
     balance = input("Would you like to deposit money into your account?(y/n): ")
     if balance == 'y':
          print("")
          balance = input("How much would you like to deposit? ")
          f = open(filename,"w+")
          f.write(balance)
          f.close()
          percentage('Creating')
          print("Account created.")
          time.sleep(1)
          spaces()
     else:
          f = open(filename,"w+")
          f.write('0')
          f.close()
          percentage('Creating')
          print("Account created.")
          time.sleep(1)
          spaces()

def accountopener():
     spaces()
     global filename
     global iflogin
     input("Welcome back, friend... Press <ENTER> to continue.")
     if iflogin == False:
          login()
          print("")
          input("Press <ENTER> to continue.")
     print("")
     f=open(filename,"r")
     percentage('Opening')
     print("Account opened.")
     time.sleep(1)
     spaces()
     print("Current bank balance: £" + f.read())
     print("")
     f.close()
     input('Press <ENTER> to exit.')
     spaces()

def accountcloser():
     spaces()
     global iflogin
     global filename
     global usr
     input("I see you want to delete your account. Very well. Press <ENTER> to continue.")
     if iflogin == False:
          login()
          print("")
          input("Press <ENTER> to continue.")
     print("")
     os.remove(filename)
     percentage('Deleting')
     print("Account deleted.")
     filename = ""
     usr = ""
     iflogin = False
     time.sleep(1)
     spaces()

def depositer():
     global iflogin
     global filename
     spaces()
     input('I see you want to deposit some money. Press <ENTER> to continue. ')
     if iflogin == False:
          login()
          print("")
          input("Press <ENTER> to continue.")
          spaces()
     print("")
     f = open(filename, 'r+')
     balance = int(f.read())
     f.truncate(0)
     add = int(input("How much would you like to deposit? "))
     imput = str(balance + add)
     f = open(filename,"w+")
     f.write(imput)
     f.close()
     percentage('Adding')
     print('£' + str(add) + ' added to your account.')
     time.sleep(1.5)
     spaces()

def remover():
     global iflogin
     global filename
     spaces()
     input('I see you want to withdraw some money. Press <ENTER> to continue. ')
     if iflogin == False:
          login()
          print("")
          time.sleep(1)
          input("Press <ENTER> to continue.")
          spaces()
     print("")
     f = open(filename, 'r+')
     balance = int(f.read())
     f.truncate(0)
     remove = int(input("How much would you like to remove? "))
     imput = str(balance - remove)
     f = open(filename,"w+")
     f.write(imput)
     f.close()
     percentage('Withdrawing')
     print('£' + str(remove) + ' removed from your account.')
     time.sleep(1.5)
     spaces()

def select():
     global usr
     global iflogin
     print("Choose 1 of the following options:")
     print("")
     if iflogin == False:
          print("Logged out.")
     elif iflogin == True:
          print("Logged in to account: " + usr)
     print("")
     print("      [1] - Open an account.")
     if iflogin == False:
          print("      [2] - Login to your account.")
     elif iflogin == True:
          print("      [2] - Logout of your account.")
     print("      [3] - Check your bank balance.")
     print("      [4] - Make a deposit.")
     print("      [5] - Make a withdrawal.")
     print("      [6] - Close an account.")
     print("      [7] - Exit the bank.")
     print("")
     choice = input("Choice: ")
     if choice == "1":
          accountcreator()
     elif choice == "3":
          accountopener()
     elif choice == "6":
          accountcloser()
     elif choice == '4':
          depositer()
     elif choice == '5':
          remover()
     elif choice == '2' and iflogin == False:
          login()
          time.sleep(1.5)
          spaces()
     elif choice == '2' and iflogin == True:
          percentage("Logging out")
          print("Logged out.")
          time.sleep(1.5)
          iflogin = False
          spaces()
     elif choice == "7":
          return 1
     else:
          spaces()

     
def start():
     print("Welcome to your local bank, where your security is our priority!")
     time.sleep(2)
     spaces()
     while True:
          if select() == 1:
               break
                    
start()
