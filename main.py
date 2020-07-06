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
from bills import WaterBill
from bills import LightBill
from bills import ElectricBill
from bills import CableBill
from bills import RentBill
from bills import House_InsuranceBill
from bills import MortgageBill
from bills import Bank_FeesBill
from bills import InternetBill
from bills import MedicalBill
from bills import CellphoneBill
from bills import Vehicle_InsuranceBill
from bills import Different_MembershipBill
from bills import Loans
from bills import KolaudimiBill
from bills import Car_InsuranceBill
from bills import Car_ServiceBill
from bills import School_TaxBill
from bills import BooksBill
from bills import FoodBill
from bills import School_TransportBill
from bills import CoursesBill

db=Database(dbname="Bills")

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


def Creating_NewBill(an):
        ID=input("Enter the id of the bill")
        year=input("Enter the year")
        month=input("Enter the month")
        day=input("Enter the day")
        price=input("Enter the price of the bill")

        bill=an(ID,an,year,month,day,price)
        db.createtableifnotexists("MonthlyBills",an,an.fromline)
        db.appendObjectsInto("MonthlyBills",[bill])
        ans3="0"
        ans4="0"
        print(bill.toString())

if __name__ == '__main__':
    main()

def AnualBills():
    print("\n -Anual Bills- opened")
    print("""
    1. Car related bills
    2. School related bills
    3. Other
    """)
    ans2=input(">>Which category would you like to access? ")

    if ans2=="1":
        print("""
        1. Kolaudimi
        2. Car insurance
        3. Car service
        """)
        print("CATEGORY-")
        ans3 = input("Which information would you like to access? ")

        while ans3 =="1":
            an = KolaudimiBill
            Creating_NewBill(an)

        while ans3 =="2":
            an = Car_InsuranceBill
            Creating_NewBill(an)

        while ans3 =="3":
            an = Car_ServiceBill
            Creating_NewBill(an)


    if ans2=="2":
        print("""
        1. School tax
        2. Books
        3. Food
        4. School Transport
        5. Courses
        """)
        print("CATEGORY-")
        ans4 = input("Which information would you like to access? ")

        while ans4 =="1":
            an = School_TaxBill
            Creating_NewBill(an)

        while ans4 =="2":
            an = BooksBill
            Creating_NewBill(an)

        while ans4 =="3":
            an = FoodBill
            Creating_NewBill(an)

        while ans4 =="4":
            an = School_TransportBill
            Creating_NewBill(an)

        while ans4 =="5":
            an=CoursesBill
            Creating_NewBill(an)

def MonthlyBills():
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
        while ans3 =="1":
            an=CableBill
            Creating_NewBill(an)
        while ans3 =="2":
            an=House_InsuranceBill
            Creating_NewBill(an)
        while ans3 =="3":
            an=LightBill
            Creating_NewBill(an)
        while ans3 =="4":
            an=WaterBill
            Creating_NewBill(an)
        while ans3 =="5":
            an=ElectricBill
            Creating_NewBill(an)
        while ans3 =="6":
            an=RentBill
            Creating_NewBill(an)
        while ans3 =="7":
            an=MonthlyBills
            Creating_NewBill(an)
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
        while ans4 =="1":
            an=Different_MembershipBill
            Creating_NewBill(an)
        while ans4 =="2":
            an=Vehicle_InsuranceBill
            Creating_NewBill(an)
        while ans4 =="3":
            an=CellphoneBill
            Creating_NewBill(an)
        while ans4 =="4":
            an=InternetBill
            Creating_NewBill(an)
        while ans4 =="5":
            an=MedicalBill
            Creating_NewBill(an)
        while ans4 =="6":
            an=Bank_FeesBill
            Creating_NewBill(an)
        while ans4 =="7":
            an=Loans
            Creating_NewBill(an)



def OtherBills():
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
        while ans3 =="1":
            an=PlaneTickets
            Creating_NewBill(an)
        while ans3 =="2":
            an=FerryTickets
            Creating_NewBill(an)
        while ans3 =="3":
            an=TrainTickets
            Creating_NewBill(an)
        while ans3 =="4":
            an=VanTickets
            Creating_NewBill(an)

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
        while ans4 =="1":
            an=ChemicalCleaning
            Creating_NewBill(an)
        while ans4 =="2":
            an=OnlineLibrary
            Creating_NewBill(an)
        while ans4 =="3":
            an=CarRent
            Creating_NewBill(an)
        while ans4 =="4":
            an=ConcertTickets
            Creating_NewBill(an)
        while ans4 =="5":
            an=Handyman
            Creating_NewBill(an)


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
        AnualBills()

    elif ans=="2":
        MonthlyBills()

    elif ans=="3":
      OtherBills()
    elif ans=="4":
      print("\n Goodbye")
      ans = None
      break
    elif ans !="":
      print("\n Not Valid Choice Try again")