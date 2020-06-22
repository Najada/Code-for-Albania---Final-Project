class ReportBase:

    def __init__(self,reportID,reportType):
        self._ID = reportID
        self._Type = reportType

    def __filter__(self,bills,condition:lambda x:True):
        b = []
        for bill in bills :
            if(condition(bill)):
                b.append(bill)
        return b

    def totalNumberOfBills(self,bills,condition:lambda x:True):
        return len(self.__filter__(bills,condition))
