
from datetime import datetime

class Transaction():
    
    def __init__(self, origin_account, destination_account, amount, atm):
        self.date = datetime.now()
        self.amount = amount
        
        self.origin_account = origin_account
        self.destination_account = destination_account
        self.atm = atm