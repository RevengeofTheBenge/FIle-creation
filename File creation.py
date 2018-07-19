import time
import os
import hashlib

iflogin = False

filename = ""

def md5hash(s):
     hash_object = hashlib.md5(s.encode())
     return hash_object.hexdigest()

def spaces():
     for i in range(1,99):
          print(" ")

def percentage(s):
     for i in range(1, 99):
          print(s +"... " + str(i) + "%")

def login():
     global iflogin
     global filename
     spaces()
     usr = input("Please enter a username: ")
     pas = input("Please enter a password: ")
     filename = usr + pas  
     filename = md5hash(filename) + ".txt"
     percenntage("Login in")
     iflogin = True
     
def accountcreator():
     spaces()
     input("You are about to create an account. Press <ENTER> to continue.")
     print("")
     usr = input("Please enter a username: ")
     pas = input("Please enter a password: ")
     filename = usr + pas  
     filename = md5hash(filename) + ".txt"
     print("")
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
     input("Welcome back, friend... Press <ENTER> to continue.")
     print("")
     usr1 = input("Please enter your username: ")
     pas1 = input("Please enter your password: ")
     print("")
     opener = md5hash(usr1 + pas1) + ".txt"
     f=open(opener,"r")
     percentage('Opening')
     print("Account opened.")
     time.sleep(1)
     spaces()
     print("Current bank balance: ")
     print('       £' + f.read())
     print("")
     f.close()
     input('Press <ENTER> to exit.')
     spaces()

def accountcloser():
     spaces()
     input("I see you want to delete your account. Very well. Press <ENTER> to continue.")
     print("")
     usr1 = input("Please enter your username: ")
     pas1 = input("Please enter your password: ")
     print("")
     opener = md5hash(usr1 + pas1) + ".txt"
     os.remove(opener)
     percentage('Deleting')
     print("Account deleted.")
     time.sleep(1)
     spaces()

def depositer():
     spaces()
     input('I see you want to deposit some money. Press <ENTER> to continue. ')
     print("")
     usr = input("Please enter your username: ")
     pas = input("Please enter your password: ")
     print("")
     filename = md5hash(usr + pas) + '.txt'
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
     spaces()
     input('I see you want to withdraw some money. Press <ENTER> to continue. ')
     print("")
     usr = input("Please enter your username: ")
     pas = input("Please enter your password: ")
     print("")
     filename = md5hash(usr + pas) + '.txt'
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
     print("Choose 1 of the following options:")
     print("")
     if login == True:
          print("Logged in.")
     print("")
     print("      [1] - Open an account.")
     print("      [2] - Check your bank balance.")
     print("      [3] - Close an account.")
     print("      [4] - Make a deposit.")
     print("      [5] - Make a withdrawal.")
     if login == False:
          print("      [6] - Login to your account.")
          login()
     elif login == True:
          print("      [6] - Logout of your account.")
          global iflogin
          iflogin = False
     print("      [7] - Exit the bank.")
     print("")
     choice = input("Choice: ")
     if choice == "1":
          accountcreator()
     elif choice == "2":
          accountopener()
     elif choice == "3":
          accountcloser()
     elif choice == '4':
          depositer()
     elif choice == '5':
          remover()
     elif choice == "6":
          return 1

     
def start():
     print("Welcome to your local bank, where your security is our priority!")
     time.sleep(2)
     spaces()
     while True:
          if select() == 1:
               break
                    
start()
