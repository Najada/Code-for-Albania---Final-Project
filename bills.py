import os
# here all classes that represent bills are defined


class BillBase:
    def __init__(self,billID,billType,year,month,day,payvalue,user):
        self._ID = billID
        self._type = billType
        self._paydate =(year,month,day)
        self._payvalue = payvalue

    def getID(self):return self._ID

    def getType(self):return self._type

    def setID(self,newID):self._ID = newID

    def getPaydate(self):return self._paydate

    def getUser(self):return self._username

    def getPayvalue(self):return self._payvalue

    def setPayvalue(self,newPayvalue):self._payvalue = newPayvalue

    # todo other getters and setters
    # ...
    # ...

    def toString(self):
        return str(self._ID)+","+str(self._type)+"\n"+str(self._paydate)+","+str(self._payvalue)+","+str(self._username)
    @classmethod
    def fromline(cls,line):
        tokens = line.split(",")
        return cls(tokens[0],tokens[1])


class WaterBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class LightBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class ElectricBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class CableBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class RentBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class House_InsuranceBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class MortgageBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class Bank_FeesBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class InternetBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class MedicalBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class CellphoneBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class Vehicle_InsuranceBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class Different_MembershipBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class Loans(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))
class KolaudimiBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class Car_InsuranceBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class Car_ServiceBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class School_TaxBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class BooksBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class FoodBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class School_TransportBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class CoursesBill(BillBase):
    def __init__(self,billID,billType,year,month,day,payvalue,user):
            super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))
class PlaneTickets:
    def __init__(self,billID,billType,year,month,day,payvalue,user):
        super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class FerryTickets:
    def __init__(self,billID,billType,year,month,day,payvalue,user):
        super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class TrainTickets:
    def __init__(self,billID,billType,year,month,day,payvalue,user):
        super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class Handyman:
    def __init__(self,billID,billType,year,month,day,payvalue,user):
        super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class ConcertTickets:
    def __init__(self,billID,billType,year,month,day,payvalue,user):
        super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class OnlineLibrary:
    def __init__(self,billID,billType,year,month,day,payvalue,user):
        super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class VanTickets:
    def __init__(self,billID,billType,year,month,day,payvalue,user):
        super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class ChemicalCleaning:
    def __init__(self,billID,billType,year,month,day,payvalue,user):
        super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))

class CarRent:
    def __init__(self,billID,billType,year,month,day,payvalue,user):
        super().__init__(billID,billType,year,month,day,payvalue)

    def output_all(self):
            print( '{} \n{} \n{} \n{}'.format(self.ID,self.type, self.paydate,
            self.payvalue,self.user))



