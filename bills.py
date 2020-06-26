import os
# here all classes that represent bills are defined


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

    def setPayvalue(self,newPayvalue):self._payvalue = newPayvalue

    # todo other getters and setters
    # ...
    # ...

    def toString(self):
        return str(self._ID)+","+str(self._type)+"\n"
    @classmethod
    def fromline(cls,line):
        tokens = line.split(",")
        return cls(tokens[0],tokens[1])


class WaterBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class LightBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class ElectricBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class CableBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class RentBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class House_InsuranceBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class MortgageBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class Bank_FeesBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class InternetBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class MedicalBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class CellphoneBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class Vehicle_InsuranceBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class Different_MembershipBill:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

class Loans:
    def __init__(BillBase):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue))

answer=input("To create a new bill press 1, to find an exisitng bill press 2!!")

if answer== 1:
    BillBase(input("Enter the ID"), input("How to u want to name this bill"),input(" Enter the year of the payment"),input(" Enter the month of the payment"),input(" Enter the day of the payment"), input("Enter the payment vaule"))
elif answer ==2:


else:
    print("This is not a valid answer")


