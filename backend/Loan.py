from Config import Configuration
from Trade import *

def GetMaxLoanAmountByID(cardid):
    db = Configuration()
    db.connect()

    MaxLoanAmount = 0
    re = db.select('cards','loanlimit, loan',{'cardid':cardid})

    if re != None:
        loan = float(re[0]['loan'])
        loanlimit = float(re[0]['loanlimit'])
        if loan<=loanlimit:
            MaxLoanAmount = loanlimit-loan
    db.close()
    return MaxLoanAmount

def LoanMoney(cardid,amount,startdate,enddate,rate):
    db = Configuration()
    db.connect()
    re = db.select('cards','loan',{'cardid':cardid})
    MaxLoanAmount = float(GetMaxLoanAmountByID(cardid))
    amount = float(amount)


    if amount <= MaxLoanAmount:
        new_loan = float(re[0]['loan'])+amount
        re =  db.update('cards',{'loan':new_loan}, {'cardid':cardid})
        if re and db.insert('loans',{'cardid':cardid,'startdate':startdate,'enddate':enddate,'amount':amount,'rate':rate,'hasrepay':'0'}):
            db.close()
            return newloan(cardid,amount)
        return False

     

