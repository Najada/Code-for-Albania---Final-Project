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




