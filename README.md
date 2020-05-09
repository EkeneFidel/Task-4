# Python Task 4: Getting Started with Banking System with FileSystem

The code contains the following functions
⋅⋅*start() - This function starts the program by prompting the user to Login or close the app.

⋅⋅*login() - This function takes the username and password from **staff.txt** and saves them in a list respectively. It then prompts the user for its username and password, then compares to the username in the list above and the password in the same index. One the username and password match, the user session is recorded in the **session.txt** file.

⋅⋅*displayOptions() - This function displays the main menu and prompts the user to create account, check account or login.

⋅⋅*createAccount() - This function prompts user for account details and add user data to the end of the **customer.txt** file.

⋅⋅*checkAccount() - This function prompts user for his/her account number and uses it to check for user details in the **customer.txt** file and displays user account details.

⋅⋅*logout() - This function deletes the **sesssion.txt** file and starts the program again. 
