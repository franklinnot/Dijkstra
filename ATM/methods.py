# main.py
from Model.Account import Account
from Model.ATM import ATM
from Model.Company import Company
from Model.ServicePay import ServicePay
from Model.Transaction import Transaction
import random

account_list = []
company_list = []
atm_list = []

# creamos 5 cajeros xd
cities = ["JR. Amazonas 344", "Av. Miraflores 655", "Av. Larco 280", "Ov. Marinera 110", "Plazuela el Recreo 120"]
for i in range(5):
    new_atm = ATM(i,cities[i], 20 * i, 25 * i, 18 * i, 33 * i , 28 * i)
    atm_list.append(new_atm)
    
atm = None

# creamos una empresa xd
new_company = Company("878", "Quavii", "Quavii SAC", "Ov. Marina 423", "925584321", "quavii@gmail.com", 6700.0)
company_list.append(new_company)


# menu inicial
def main():
    print("\nBienvenid@ a BunnyBank:")
    print(" 1. Iniciar sesión")
    print(" 2. Registrarse")       
    option = input("Seleccione una opción: ")
    if option == "1":
        account  = login()
        if account != None:
            main_menu(account)
    elif option == "2":
        register()  
        


def register():
    print("Ingrese los siguientes datos:")
    # aqui se debe agregar la logica para verificar que no existe otra cuenta con ese dni, telefono ni email
    dni = input("DNI: ")
    given_name = input("Nombre: ")
    last_name = input("Apellidos: ")
    address = input("Dirección: ")
    phone_number = input("Teléfono: ")
    email = input("Email: ")
    password = input("Contraseña: ")
    balance = input("Depósito inicial: ") # comprobar que sea mayor o igual a 500. Obvio, que los billetes sean ingresados a la atm
    new_account = Account(
        dni=dni,
        given_name=given_name,
        last_name=last_name,
        address=address,
        phone_number=phone_number,
        email=email,
        password=password,
        balance=balance
)
    
    
    account_list.append(new_account)
    
    # implementar el metodo de quicksort por apellidos a la lista de cuentas
    # cada que se registre un nuevo cliente
    
    print("Registro exitoso!")
    

def login():
    
    dni = input("\nIngresa tu DNI: ")
    password = input("Ingresa tu contraseña: ")

    # implementar logica para buscar en la lista y comprobar si la cuenta ingresada es la correcta
    # si encuentra a la cuenta, entonces retornara esta cuenta. Si despues de iterar en la lista
    # no la encuentra, retornar None
    # utilzar búsqueda binaria
    
    # Nota: Si las entradas coinciden con una registrada, llamar al metodo
    # main_menu() pasandole el objeto de tipo account: main_menu(account)
    

def show_balance(account): 
    print(f"Su saldo actual es: {account.balance} soles")

def show_transactions(account):
    print("\nLISTA DE MOVIMIENTOS REGISTRADOS\n")
    transactions = account.transactions
    # agregar codigo para limitar el numero de impresion de transacciones por pasos de 10 o la cantidad
    # que mejor se acomode a la vista. Preguntarle ademas si desea continuar viendo
    for t in transactions:
        if t.cuenta_origen_id == account.id_account:
            other = "" # mostrar datos de a quien hicimos la transaccion
            print(f"{other.given_name} {other.last_name}        -S/ {t.amount}      {t.date}")
        else:
            other = "" # mostrar datos de quien nos hizo la transaccion
            print(f"{other.given_name} {other.last_name}        S/ {t.amount}       {t.date}")

def main_menu(account):
    while True:
        print(f"Bienvenido {account.given_name}!")
        print("1. Ver saldo")
        print("2. Ver transacciones")
        print("3. Hacer una transferencia")
        print("4. Pagar un servicio")
        print("5. Salir")
        
        option = input("Seleccione una opción: ")
        
        if option == "1":
            show_balance(account)
        elif option == "2":
            show_transactions(account)
        elif option == "3":
            make_transfer(account)
        elif option == "4":
            pay_service(account)
        elif option == "5":
            break
        else:
            print("Opción no válida")

        input("\nPresione Enter para continuar...")

def make_transfer(account):
    destination_dni = input("Ingrese el DNI del destinatario: ") 
    # comprobar que la cuenta existe. Si no existe, salir del metodo. Utilizar el if general
    # puesto aquí. Para su "else" imprimir el mensaje de que esa cuenta no existe
    destination_account = ""
    if destination_account == "existe": # obvio, no se va a comparar con "existe" xddd
        amount = float(input("Ingrese el monto a transferir: "))

        if account.balance >= amount:
            account.balance -= amount
            destination_account.balance += amount
                
            new_transaction = Transaction(
                amount = amount,
                origin_account = account,
                destination_account = destination_account,
                atm = atm
            )

            # agragar la transaccion a la lista de transacciones
            # tanto del que la hace como el que la recibe
            
            print("Transferencia exitosa!")
        else:
            print("Saldo insuficiente")
    else:
        print("Cuenta de destinatario no encontrada")

def pay_service(account):
    
    # agregar logica para mostrar la lista de empresas: RUC y nombre comercial (tradename)
    
    ruc = input("Ingrese el RUC de la empresa de servicio: ")
    
    company = "search_company(ruc)" # devolver el objeto de tipo company o None con el metodo de busqueda binaria
    if company != None:
        amount = float(input("Ingrese el monto a pagar: "))
        if account.balance >= amount:
            account.balance -= amount
            company.balance += amount            
            new_servicepay = ServicePay(
                amount=amount,
                origin_account=account,
                destination_company=company,
                atm=atm 
            )
            account.services_pay.append(new_servicepay)
            company.services_pay.append(new_servicepay)
            print("Pago de servicio exitoso!")
        else:
            print("Saldo insuficiente")
        
    else:
        print("Empresa de servicio no encontrada")


# buenas practicas jeje
if __name__ == "__main__":
    
    # usar este codigo solo para pruebas y dando nuevos valores
    '''
    new_account = Account(
    dni="95743215",
    given_name="Camila Jen",
    last_name="Torres Smith",
    address="Buenos Aires",
    phone_number="9957714325",
    email="camilasmith@outlook.com",
    password="reborn123",
    balance=6996.0)
    
    account_list.append(new_account)
    
    temporizador("Registro exitoso!", 3)
    '''
    
    while True:
        atm = random.choice(atm_list)
        main()
    
    