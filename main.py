import datetime
from random import randint
import os

def start():
   resp = int(input("Choose one of the following \n 1. Staff Login \n 2. Close App\n"))
   if resp == 1:
      login()
   if resp == 2:
      exit()


def login():
   usern = []
   passw = []


   # Retrieve username and password from text file into a list
   with open("staff.txt") as f:
      for res in f:
         usern.append(res.split(' ')[0].lower())
         passw.append(res.split(' ')[1].lower())
   f.close()


   # Prompt user for username and password and check username.
   # If username is contained in previous list, check if password inputed is same
   #       same as password in the list on the same index as username
   while True:
      username = input("What is your Username?").lower()
      password = input("What is your Password?").lower()
      if username in usern:
         print("\n")
         
      if password in passw and password == passw[usern.index(username)]:
         print("\nUser has been identified, Welcome", username)
         sess_file = open("session.txt", "w")
         sess_file.write("user " + username + " session at "+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
         sess_file.close()

         displayOptions()

         break
      else:
         print("Username and Password incorrect!")


def displayOptions():
   print("\n----------------------------------------")
   print("Choose one of the following \n1. Create new Bank Account \n2. Check Account details \n3. Logout \n ")
   resp = int(input())
   if resp == 1:
      createAccount()
   if resp == 2:
      checkAccount()
   if resp == 3:
      logout()


def createAccount():
   acct_name = input("Enter your account name: ")
   opening_balance = input("Enter your opening balance? ")
   acct_type = input("Savings or Current? ")
   acct_email = input("Enter your account email: ")

   acct_num = randint(10**9,(10**10)-1)


   with open("customer.txt", "a+") as f:
      #move and read cursor to the start of the file
      f.seek(0)
      #If file is not empty, append '\n'
      data = f.read(100)
      if len(data) > 0:
         f.write('\n')
      f.write(("{} {} {} {} {} ").format(acct_name,acct_num,opening_balance,acct_type,acct_email))
      f.close()

   print(("Account Number:{} ").format(acct_num))
   displayOptions()


def checkAccount():
   print("Enter Account Number: ")
   acctNum = input()
   line_number = 0
   result = []
   # Retrieve user account details from
   #  customer.txt using account number
   with open("customer.txt", "r") as f:
      # Read all lines in the file one by one
      for line in f:
         # For each line, check if line contains the string
         line_number += 1
         if acctNum in line:
            result.append((line_number, line.rstrip()))
            final_details = line.split()
            print()
            data = ["Account Name: ", "Account Number: ", "Opening Balance: $ ", "Account Type: ", "Email: "]
            counter = 0
            for i in data:
               print((i + "{}\n").format(final_details[counter]))
               counter += 1
   f.close()

   displayOptions()
   

def logout():     
   os.remove("session.txt")
   start()


start()