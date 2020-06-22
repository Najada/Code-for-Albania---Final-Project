#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     03/06/2020
# Copyright:   (c) User 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from database import Database
from bills import BillBase
from reports import ReportBase
from database import BaseObject
from os import system , name





class User(BaseObject):
    def __init__(self,username,password,usertype):
        self.__username = username
        self.__password = password
        self.setUserType(usertype)

    def setUserType(self,utype="user"):
        if(utype=="admin"):
            self._usertype = "admin"
        else :self._usertype = "user"


    def toString(self):
        return str(self.__username)+","+str(self.__password)+","+ str(self._usertype)

    @classmethod
    def fromLine(cls,line):
        tokens = line.split(",")
        if(len(tokens)==3):
            return cls(tokens[0],tokens[1],tokens[2])
        else : return cls("guest","guest","guest")

    def check(self,password):
        return self.__password==password





def option1(user:User,db:Database):
    choice = input(">")
    if(choice ==1):
        suboption1()
    elif(choice==2):
        suboption2()
    else :
        return
    return



def suboption1():
    print("you chosed suboption 1")
    pass

def suboption2():
    print("you chosed suboption 2")
    pass

def option2():
    pass

def option3():
    pass


def clearscreen(self):
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Activity:
    def __init__(self,db,currentuser:User):
        self.__currentuser = currentuser
        self.__db = db
    def start(self):
        # wellcome the user
        # present the option
        print("1 for option 1")
        print("2 for option 2")
        opt = input(">")
        if opt==1:
            option1(self.__currentuser,self.__db)
        elif opt==2:
            option2()
        elif opt == 3:
            option3()
        else :
            print("goodbye")
            return True


        # take any option chosen by thew user


        pass



def main():
    # initialize the database
    db = Database(dbname="db",dbpath=".")
    # create the tabkes
    db.createtableifnotexists("users",User,User.fromLine)
    db.createtableifnotexists("bills",BillBase,BillBase.fromline)

    while True:
        # get user info
        users = db.getObjectsFrom("users")
        print("all users read")
        if(len(users)==0):
            # enter add new admin wizard
            print("logging in as admin ")
            curruser = User("admin","admin","admin")
            Activity(db,curruser).start()
        else:
            # inform the user that to enter he needs to enter an passsword.
            # enter username
            # enter password
            # check user validity
            #db.getObjectsFrom("users",x=x.check(username))
            curruser = User("me","me","me")
            Activity(db,curruser).start()
        print("do you want to login : [y]")
        if input(">")!="y":
            break



if __name__ == '__main__':
    main()
