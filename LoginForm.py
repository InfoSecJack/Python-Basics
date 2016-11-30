import hashlib
import uuid
import tkinter

class Variables(object):

    def ___init__():
        try:
            file = open('passwords.txt', 'r')
            file.close()
        except:
            file = open('passwords.txt', 'w')
            file.close()

class Menu:


    
    def __init__(self):
        menuoptions = ["Login", "Create New User"]
        
        def printmenu():
            listnum = 0
            number = 1
            for x in range(len(menuoptions)):
                       prnumber = str(number)
                       print (prnumber + ") " + menuoptions[listnum])
                       listnum += 1
                       number += 1
            listnum = 0
            number = 1
            
        def choicemenu():
            listnum = 0
            number = 1
            
            for x in range(len(menuoptions)):
                prnumber = str(number)            
                if choice in prnumber:
                    print ("You picked " + prnumber)
                    break
                else:
                    number + 1
                    
        
        listnum = 0
        menuoptions = ["Login", "Create New User"]
        printmenu()     
        choice = input("Pick an option: ")
        choicemenu()

        
class Users:
    

    def __init__(self, username):
        Variables()
        self.username = username
        
    def writepass(self):
        global passwords
        f = open('passwords.txt', 'a+')
        f.write(self.username + ':' + self.password + "\n")
        f.seek(0, 0)
        passwords = f.readlines()
        f.close()
        
    def password(self, password):
        self.password = password
        password = password.encode()
        beforeHash = hashlib.sha512(password)
        self.password = beforeHash.hexdigest()
        self.writepass()

        

if __name__ == "__main__":
    Variables()
    Menu()

jack = Users("Jack")
name = str(input("What is your name?: "))
vars()[name] = Users(name)
password = input("What is your password?: ")
vars()[name].password(password)
