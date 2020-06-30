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
import os
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



ans=True
while ans:
    print ("""
    1.Anual Bills
    2.Monthly Bills
    3.Other Bills
    4.Exit/Quit
    """)
    ans=input(">>What option would you like to choose? ") 
    if ans=="1": 
      print("\n -Anual Bills- opened") 
    elif ans=="2":
      print("\n -Monthly Bills- opened") 
    elif ans=="3":
      print("-Other Bills-")
      print("""
      1.Transportation 
      2.Other
      """) 
      ans2=input(">>Which category would you like to access? ")
      if ans2=="1":
        print("""
        1.PlaneTickets
        2.FerryTickets
        3.TrainTickets
        4.VanTickets
        """)
        print("CATEGORY-TRANSPORTATION")
        ans3 = input("Which information would you like to access? ")
      if ans2=="2":
        print("""
        1.ChemicalCleaning
        2.OnlineLibrary
        3.CarRent
        4.ConcertTickets
        5.Handyman
        """)
        print("CATEGORY-OTHER")
        ans4 = input("Which information would you like to access? ")
    elif ans=="4":
      print("\n Goodbye")
      ans = None 
      break
    elif ans !="":
      print("\n Not Valid Choice Try again")  


class BillBase:
    def __init__(self,billID,billType,year,month,day,payvalue):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def getID(self):return self._ID

    def getType(self):return self._type

    def setID(self,newID):self._ID = newID
    
    def getPaydate(self):return self._paydate

    def getPayvalue(self):return self._payvalue

    def setPayvalue(self, newPayvalue):self._payvalue = newPayvalue


    def toString(self):
        return str(self._ID)+","+str(self._type)+"\n"
    @classmethod
    def fromline(cls,line):
        tokens = line.split(",")
        return cls(tokens[0],tokens[1])


class PlaneTickets:
    def __init__(BillBase):
          self._ID = billID
          self._type = billType
          self._paydate =(year,month,day)
          self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class FerryTickets:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class TrainTickets:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class Handyman:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class ConcertTickets:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class OnlineLibrary:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class VanTickets:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class ChemicalCleaning:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class CarRent:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))


answer=input("Create new bill press(1), existing bill press(2):")
if answer == "1":
    BillBase(input("Enter the ID: "), input("Name of the bill: "),input("Enter the year of the payment: "),input("Enter the month of the payment: "),input("Enter the day of the payment: "), input("Enter the payment vaule: "))
elif answer == "2":
    print("test")
else:
    print("ERROR - This answer is not valid")

    def toString(self):
        return str(self._ID)+","+str(self._type)+"\n"
    @classmethod
    def fromline(cls,line):
        tokens = line.split(",")
        return cls(tokens[0],tokens[1])

ans=True
while ans:
    print ("""
    1.Anual Bills
    2.Monthly Bills
    3.Other Bills
    4.Exit/Quit
    """)
    ans=input(">>What option would you like to choose? ")
    if ans=="1":
      print("\n -Anual Bills- opened")
      print("""
        1.
        2.
        """)

      ans2=input(">>Which category would you like to access? ")
      if ans2=="1":
        print("""
        1.
        2.
        3.
        4.
        5.
        """)
        print("CATEGORY-")
        ans3 = input("Which information would you like to access? ")
      if ans2=="2":
        print("""
        1.
        2.
        3.
        4.
        5.
        """)
        print("CATEGORY-")
        ans4 = input("Which information would you like to access? ")
    elif ans=="2":
      print("\n -Monthly Bills- opened")
      print("""
        1.House related Bills
        2.Other
        """)

      ans2=input(">>Which category would you like to access? ")
      if ans2=="1":
        print("""
        1.Cable
        2.House insurance
        3.Light Bills
        4.Water Bills
        5.Electricity
        6.Rent
        7.Mortgage
        """)
        print("CATEGORY-House related bills")
        ans3 = input("Which information would you like to access? ")
      if ans2=="2":
        print("""
        1.Different memberships
        2.Vehical insurance
        3.Cellphone bills
        4.Internet bills
        5.Medical bills
        6.Bank fees
        7.Loans
        """)
        print("CATEGORY-OTHER")
        ans4 = input("Which information would you like to access? ")

    elif ans=="3":
      print("-Other Bills-")
      print("""
      1.Transportation
      2.Other
      """)
      ans2=input(">>Which category would you like to access? ")
      if ans2=="1":
        print("""
        1.PlaneTickets
        2.FerryTickets
        3.TrainTickets
        4.VanTickets
        """)
        print("CATEGORY-TRANSPORTATION")
        ans3 = input("Which information would you like to access? ")
      if ans2=="2":
        print("""
        1.ChemicalCleaning
        2.OnlineLibrary
        3.CarRent
        4.ConcertTickets
        5.Handyman
        """)
        print("CATEGORY-OTHER")
        ans4 = input("Which information would you like to access? ")
    elif ans=="4":
      print("\n Goodbye")
      ans = None
      break
    elif ans !="":
      print("\n Not Valid Choice Try again")




