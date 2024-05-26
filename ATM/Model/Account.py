
# En el fonodo se maneja como si fuera un nodo, pero sin apuntador
# pues, se utilizara la estructura de lista de python y no una propia, o sea creada por nosotros.

from datetime import datetime
from Transaction import Transaction
from ATM import ATM
from Company import Company
from ServicePay import ServicePay
import random

class Account():    
    def __init__(self, dni, given_name, last_name, address, phone_number, email, password, balance):
        self.dni = dni
        self.given_name = given_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.register_date = datetime.now()
        self.balance = balance
        
        self.transactions = [] # lista de objetos "Transaction"
        self.services_pay = [] # lista de objetos "ServicePay"



####################### CÓDIGO DE EJEMPLO COMENTADO



# creamos las listas de los 3 nodos principales
account_list = []
company_list = []
atm_list = []

# creamos 5 cajeros xd
cities = ["JR. Amazonas 344", "Av. Miraflores 655", "Av. Larco 280", "Ov. Marinera 110", "Plazuela el Recreo 120"]
for i in range(5):
    new_atm = ATM(i,cities[i], 20 * i, 25 * i, 18 * i, 33 * i , 28 * i)
    atm_list.append(new_atm)
    
# creamos una empresa xd
new_company = Company("878", "Quavii", "Quavii SAC", "Ov. Marina 423", "925584321", "quavii@gmail.com", 6700.0)
company_list.append(new_company)

# creamos dos cuentas de prueba. cada cuenta tendra una lista de transacciones y pagos de servicio
new_account = Account(dni="75048062",given_name="franklin",last_name="not",address="Trujillo City", phone_number="941225240",
                      email="franklinnot@outlook.com", password="sohigh", balance=7900.0)

second_account = Account(dni="95741369",given_name="boyita",last_name="boy",address="Trujillo City", phone_number="952668412",
                      email="boyiboyt@gmail.com", password="clown", balance=6900.0)

account_list.append(new_account)
account_list.append(second_account)

print("\n LISTA DE CUENTAS")
for c in account_list:
    print(f"{c.dni}     {c.given_name}      {c.balance}")
print("\n")

# sacamos esta cuenta dentro de la lista para comprobar si python interpreta  correctamente las referencias
origin = account_list[0]
destiny = account_list[1]


# realizamos una transaccion como prueba 
# cada una de estas operaciones seran como nuestras aristas que unan a nuestros nodos. 
# Estas aristas tienen como referencia a las instancias correspondientes
atm = random.choice(atm_list)
transaction = Transaction(origin, destiny, 150, atm) # una transaccion a boyita de 150 soles

# registramos este movimiento en la lista de transacciones de las cuentas
# lo probamos con origin y destitny pora verificar si las referencias modifican 
# al espacio de memoria al que apuntan
destiny.transactions.append(transaction)
destiny.balance += transaction.amount # modificamos su saldo
origin.balance -= transaction.amount
# el monto de la transaccion lo ponemos en negativo para quien hace el movimiento
# creamos otra transaccion temporal para poder modificar el signo de la transaccion
# sin afectar a la misma direccion de memoria
origin.transactions.append(transaction)

# Nota: para listar todos los movimientos de una cuenta, verificar si este representa la cuenta origen
# o destino de cada movimiento. De esta manera mostrar solo los datos de la otra persona involucrada

print("LISTA DE CUENTAS")
for c in account_list:
    print(f"CUENTA: {c.dni}     {c.given_name}      {c.balance}")
    print("Transacciones:")
    for t in c.transactions:
        if t.origin_account.dni == c.dni:
            print(f"{t.destination_account.given_name}     -{t.amount}      {t.atm.address}      {t.date}")
        else:
            print(f"{t.origin_account.given_name}     {t.amount}      {t.atm.address}      {t.date}")
    print("\n")


origin = account_list[1] # ahora boyita gastara xd
# Hacemos lo mismo pero para pago de servicio
company = company_list[0]
atm = random.choice(atm_list)
new_spay = ServicePay(origin, company, 230, atm)
company.services_pay.append(new_spay)
company.balance += new_spay.amount
origin.balance -= new_spay.amount
origin.services_pay.append(new_spay)

# litooooooooo, ya hicimos una transaccion y un pago de servicio, veamos si fue correcto. 
print("LISTA DE CUENTAS")
for c in account_list:
    print(f"CUENTA: {c.dni}     {c.given_name}      {c.balance}")
    print("Pagos de Servicio")
    for t in c.services_pay:
        print(f"{t.destination_company.tradename}     -{t.amount}      {t.atm.address}       {t.date}")
    print("\n")