

class ATM(): 
    def __init__(self, id_atm, address, bill_two_hundred, bill_one_hundred, bill_fifty, bill_twenty, bill_ten):
        self.id_atm = f"ATM00{id_atm}"
        self.address = address
        self.bill_two_hundred = bill_two_hundred
        self.bill_one_hundred = bill_one_hundred
        self.bill_fifty = bill_fifty
        self.bill_twenty = bill_twenty
        self.bill_ten = bill_ten
        
        self.transactions = []
        self.services_pay = []
