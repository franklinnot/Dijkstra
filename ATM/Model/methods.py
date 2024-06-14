# main.py
from Account import Account
from ATM import ATM
from Company import Company
from ServicePay import ServicePay
from Transaction import Transaction
import random
from os import system

account_list = []
company_list = []
atm_list = []

# creamos 5 cajeros xd
cities = ["JR. Amazonas 344", "Av. Miraflores 655", "Av. Larco 280", "Ov. Marinera 110", "Plazuela el Recreo 120"]
for i in range(5):
    new_atm = ATM(i,cities[i], 20 * i, 25 * i, 18 * i, 33 * i , 28 * i)
    atm_list.append(new_atm)
    
atm = None
def ingreso_billetes(balance): #yo yuleisy modifiqué el codigo de bucchi boy oh yep
    aux = 0
    print("Los billetes aceptados son [200] [100] [50] [20] [10]")
    while aux < balance:
        try:
            billete = float(input("Ingrese los billetes: "))
            if billete in [200, 100, 50, 20, 10]:
                if aux + billete > balance:
                    print(f"No puede exceder el depósito inicial de {balance}. Ingrese un billete menor.")
                else:
                    if billete == 200:
                        aux += 200
                        atm.bill_two_hundred += 1
                    elif billete == 100:
                        aux += 100
                        atm.bill_one_hundred += 1
                    elif billete == 50:
                        aux += 50
                        atm.bill_fifty += 1
                    elif billete == 20:
                        aux += 20
                        atm.bill_twenty += 1
                    elif billete == 10:
                        aux += 10
                        atm.bill_ten += 1
                    print(f"Total ingresado: {aux} / {balance}")
            else:
                print("Billete no aceptado. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingrese un valor numérico.")
    print("Depósito completado.")

def binary_search(accounts, target, key):
    low = 0
    high = len(accounts) - 1

    while low <= high:
        mid = (low + high) // 2
        if getattr(accounts[mid], key) == target:
            return accounts[mid]
        elif getattr(accounts[mid], key) < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def search_account(dni=None, email=None, phone_number=None,password=None):
    account_list
    if dni is not None:
        return binary_search(account_list, dni, 'dni')
    elif email is not None:
        return binary_search(account_list, email, 'email')
    elif phone_number is not None:
        return binary_search(account_list, phone_number, 'phone_number')
    elif password is not None:
        return binary_search(account_list,password,'password')
    else:
        return None
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
        if account != None:
            main_menu(account)
    elif option == "2":
        register()  
        lista_ordenada = quickSort(account_list,"last_name")        
        #mostrarLista(lista_ordenada)  #(lo puse para comprobar xd) 

def register():    
    while True:
        print("Ingrese los siguientes datos:")

        dni = input("DNI: ")
        if search_account(dni=dni) is not None:
            print("Ya existe una cuenta con ese DNI.")
            continue
        given_name = input("Nombre: ")
        last_name = input("Apellidos: ")
        address = input("Dirección: ")
        while True:
            phone_number = input("Teléfono: ")        
            if search_account(phone_number=phone_number) is not None:
                print("Ya existe una cuenta con ese número de teléfono.")
            else:
                break
        while True:
            email = input("Email: ") 
            if search_account(email=email) is not None:
                print("Ya existe una cuenta con ese email.")
            else:
                break    
        while True:
            password = input("Contraseña: ")
            if search_account(password=password) is not None:
                print("Esa contraseña ya ha sido utilizada. Por favor, elija otra.")
            else:
                break    
        while True:
            # comprobar que sea mayor o igual a 500. Obvio, que los billetes sean ingresados a la atm
            balance = float(input("Depósito inicial: "))
            if balance >= 500:
                ingreso_billetes(balance=balance)
                break                              
            else:
                print("El depósito inicial debe ser mayor o igual a 500. Por favor, inténtalo de nuevo.")
        new_account = Account(
            dni=dni,
            given_name=given_name,
            last_name=last_name,
            address=address,
            phone_number=phone_number,
            email=email,
            password=password,
            balance=balance)
        account_list.append(new_account)
        print("Registro exitoso!")
        print(" 1. Ir al menú principal")
        print(" 2. Registrar otra cuenta")
        while True:  
            try:
                option_customer =int(input ("Seleccione una opción:"))
                if option_customer == 1:
                    system('cls')
                    main_menu(new_account)
                    return
                if option_customer ==2:
                    break
                else:
                    print("Opción no existente. ")
            except ValueError:
                    print("Entrada inválida. Ingrese un número.")
    
"""def mostrarLista(lista):
    print("═"*120)
    print("DNI".ljust(10," "), end = "| ")
    print("NOMBRE".center(18," "), end = "| ")
    print("APELLIDO".center(22," "), end = "| ")
    print("DIRECCIÓN".center(35," "), end = "| ")
    print("TELÉFONO".center(15," "), end = "| ")
    print("EMAIL".center(15," "))
    print("═"*120)
    for account in lista:
        print(account.dni.ljust(10," "), end = "| ")
        print(account.given_name.upper().ljust(18," "), end= "| ")
        print(account.last_name.upper().ljust(22," "), end= "| ")
        print(account.address.upper().ljust(35," "), end= "| ")
        print(account.phone_number.ljust(15," "), end= "| ")
        print(account.email.upper().ljust(15," "))
        print("-"*120)
"""
# implementar el metodo de quicksort por apellidos a la lista de cuentas
    
# cada que se registre un nuevo cliente
        
def quickSort(lista, atributo):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if getattr(x, atributo) < getattr(pivot, atributo)]
        middle = [x for x in lista if getattr(x, atributo) == getattr(pivot, atributo)]
        right = [x for x in lista if getattr(x, atributo) > getattr(pivot, atributo)]
        return quickSort(left, atributo) + middle + quickSort(right, atributo)


def login():
    dni = input("\nIngresa tu DNI: ")
    password = input("Ingresa tu contraseña: ")
    account = search_account(dni=dni,password=password)
    account = search_account(dni=dni)
    if account is not None and account.password == password:
        system("cls")
        main_menu(account)
    else:
        system("cls")
        print("DNI o contraseña incorrectos. Por favor, inténtalo de nuevo.")
        login()
    

    # implementar logsica para buscar en la lista y comprobar si la cuenta ingresada es la correcta
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
    num_transactions = len(transactions)
    steps = 10 #cantidad de transacciones x page
    for start in range(0, num_transactions, steps):
        end = start + steps
        page_transactions = transactions[start:end]    
        for t in page_transactions:
            if t.origin_account == account:
                other = t.destination_account # mostrar datos de a quien hicimos la transaccion
                print(f"{other.given_name.upper()} {other.last_name.upper()}        -S/ {t.amount}      {t.date}")
            else:
                other = t.origin_account # mostrar datos de quien nos hizo la transaccion
                print(f"{other.given_name.upper()} {other.last_name.upper()}        S/ {t.amount}       {t.date}")
        if end < num_transactions:
            continuar_viendo = input("¿Desea continuar viendo más transacciones? (s/n): ")
            if continuar_viendo.upper() != 'S':
                break
        
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
    
    # este codigo elije un cajero cada que aparezca el main
    
    while True:
        atm = random.choice(atm_list)
        main()
    
    