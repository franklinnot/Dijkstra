
from datetime import datetime

class ServicePay():
    
    def __init__(self, origin_account, destination_company, amount, atm):
        self.date = datetime.now()
        self.amount = amount
        
        self.origin_account = origin_account
        self.destination_company = destination_company
        self.atm = atm