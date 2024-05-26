

class Company():
    def __init__(self, ruc, tradename, business_name, address, phone_number, email, balance):
        self.ruc = f"000{ruc}"
        self.tradename = tradename
        self.business_name = business_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.balance = balance

        self.services_pay = [] # lista de objetos "ServicePay"