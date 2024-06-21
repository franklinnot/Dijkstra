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

# creamos 10 cajeros xd
cities = ["JR. Amazonas 344", "Av. Miraflores 655", "Av. Larco 280", "Ov. Marinera 110", "Plazuela el Recreo 120", 
          "Av. César Vallejo 202", "Jr. Gamarra 518", "408 Av. Carlos Valderrama","1355 Av. Húsares de Junín", "1595 Av. Larco" ]
for i in range(10):
    new_atm = ATM(i,cities[i], 20 * i, 25 * i, 18 * i, 33 * i , 28 * i)
    atm_list.append(new_atm)


#Ingresamos el cajero junto con su dinero
def ingreso_cajero():
    try:
        address = input("Ingrese la dirección del cajero: ")
        number_bill_two_hundred = int(input("Ingrese la cantidad de billetes de 200 que tiene el cajero: ")) 
        number_bill_one_hundred  = int(input("Ingrese la cantidad de billetes de 100 que tiene el cajero: "))
        number_bill_fifty = int(input("Ingrese la cantidad de billetes de 50 que tiene el cajero: "))
        number_bill_twenty = int(input("Ingrese la cantidad de billetes de 20 que tiene el cajero: "))
        number_bill_ten = int(input("Ingrese la cantidad de billetes de 10 que tiene el cajero: "))
        

        new_atm = ATM(address, number_bill_two_hundred, number_bill_one_hundred, number_bill_fifty, number_bill_twenty, number_bill_ten)
        
        atm_list.append(new_atm)
        print("\033[32m"+"El cajero se ha registrado con éxito."+"\033[m")
        return
    
    except ValueError:
        print("\031[31m"+"Entrada inválida. Ingrese un valor numérico para la cantidad de billetes."+"\033[m")
        return
    

# dispensamos billetes de manera iterativa
def dispensador(monto, billetes):
    billsel = []
    for bill, count in billetes:
        while monto >= bill and count > 0:
            billsel.append(bill)
            monto -= bill
            count -= 1
    if monto == 0:
        return billsel
    else:
        return None

# calculamos cuantos billetes tiene el atm
def call_dispensador(monto, atm):
    billetes = [
        [200, atm.bill_two_hundred],
        [100, atm.bill_one_hundred],
        [50, atm.bill_fifty],
        [20, atm.bill_twenty],
        [10, atm.bill_ten]
    ]
    #llamamos al dispensador
    return dispensador(monto, billetes)

def withdraw_money(account, atm):

    try:
        #el usuario ingresa el monto
        user_amount = int(input("\033[33m"+"Ingrese la cantidad que desea retirar: "+"\033[m"))
    except ValueError:
        print("\033[31m"+"Entrada inválida. Ingrese un valor numérico porfavor."+"\033[m")
        return

    #comparamos con el dinero que tiene el usuario en su cuenta
    if account.balance < user_amount:
        print("\033[31m"+"No tienes el saldo suficiente para realizar este retiro."+"\033[m")
        return

    # creamos una variable total cash donde se almacenara la suma de el dinero del cajero
    total_cash = sum([
        atm.bill_two_hundred * 200,
        atm.bill_one_hundred * 100,
        atm.bill_fifty * 50,
        atm.bill_twenty * 20,
        atm.bill_ten * 10
    ])
    #con esa variable comparamos y verificamos si el cajero tiene el dinero suficiente para retirar ese monto
    if total_cash < user_amount:
        print("\033[31m"+"El cajero no tiene suficiente dinero para este retiro."+"\033[m")
        return

    # calculamos los billetes a dispensar
    bills_to_dispense = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0}
    remaining_amount = user_amount

    # llamamos a la funcion para que dispense el dinero
    bills = call_dispensador(user_amount, atm)

    if bills is None:
        print("\033[31m"+"No se pueden dispensar los billetes necesarios. Intenta con otro monto."+"\033[m")
        return

    # actualizamos la cantidad de billetes a dispensar
    for bill in bills:
        bills_to_dispense[bill] += 1
        #actualizamos la cantidad de billetes que se reducen del atm
        if bill == 200:
            atm.bill_two_hundred -= 1
        elif bill == 100:
            atm.bill_one_hundred -= 1
        elif bill == 50:
            atm.bill_fifty -= 1
        elif bill == 20:
            atm.bill_twenty -= 1
        elif bill == 10:
            atm.bill_ten -= 1

    # actualizamos el saldo del usuario
    account.balance -= user_amount

    # mostramos los billetes a dispensar
    print("\033[32m"+"Retiro exitoso, recibiras: "+"\033[m")
    for bill, count in bills_to_dispense.items():
        if count > 0:
            print(f"{count} billetes de {bill} soles")

    
atm = None
def ingreso_billetes(balance): #yo yuleisy modifiqué el codigo de bucchi boy oh yep
    aux = 0
    print("\033[35m"+"Los billetes aceptados son [200] [100] [50] [20] [10]"+"\033[m")
    while aux < balance:
        try:
            billete = float(input("\033[35m"+"Ingrese los billetes: "+"\033[m"))
            if billete in [200, 100, 50, 20, 10]:
                if aux + billete > balance:
                    print("\033[31m"+f"No puede exceder el depósito inicial de {balance}. Ingrese un billete menor."+"\033[m")
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
                print("\033[31m"+"Billete no aceptado. Intente nuevamente."+"\033[m")
        except ValueError:
            print("\033[31m"+"Entrada inválida. Ingrese un valor numérico porfavor."+"\033[m")
    print("\033[32m"+"Depósito completado."+"\033[m")

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
    print("\033[32m"+"\nBienvenid@ a BunnyBank:"+"\033[m")
    print("\033[33m"+" 1. Iniciar sesión")
    print(" 2. Registrarse"+"\033[m")       
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
        print("\033[35m"+"Ingrese los siguientes datos:"+"\033[m")

        dni = input("\033[36m"+"DNI: "+"\033[m")
        if search_account(dni=dni) is not None:
            print("\033[31m"+"Ya existe una cuenta con ese DNI."+"\033[m")
            continue
        given_name = input("\033[36m"+"Nombre: "+"\033[m")
        last_name = input("\033[36m"+"Apellidos: "+"\033[m")
        address = input("\033[36m"+"Dirección: "+"\033[m")
        while True:
            phone_number = input("\033[36m"+"Teléfono: "+"\033[m")        
            if search_account(phone_number=phone_number) is not None:
                print("\033[31m"+"Ya existe una cuenta con ese número de teléfono."+"\033[m")
            else:
                break
        while True:
            email = input("\033[36m"+"Email: "+"\033[m") 
            if search_account(email=email) is not None:
                print("\033[31m"+"Ya existe una cuenta con ese email."+"\033[m")
            else:
                break    
        while True:
            password = input("\033[36m"+"Contraseña: "+"\033[m")
            if search_account(password=password) is not None:
                print("\033[31m"+"Esa contraseña ya ha sido utilizada. Por favor, elija otra."+"\033[m")
            else:
                break    
        while True:
            # comprobar que sea mayor o igual a 500. Obvio, que los billetes sean ingresados a la atm
            balance = float(input("\033[35m"+"Depósito inicial: "+"\033[m"))
            if balance >= 500:
                ingreso_billetes(balance=balance)
                break                              
            else:
                print("\033[31m"+"El depósito inicial debe ser mayor o igual a 500. Por favor, inténtalo de nuevo."+"\033[m")
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
        print("\033[32m"+"Registro exitoso!"+"\033[m")
        print("\033[33m"+" 1. Ir al menú principal")
        print(" 2. Registrar otra cuenta"+"\033[m")
        while True:  
            try:
                option_customer =int(input ("\033[35m"+"Seleccione una opción:"+"\033[m"))
                if option_customer == 1:
                    system('cls')
                    main_menu(new_account)
                    return
                if option_customer ==2:
                    break
                else:
                    print("\033[31m"+"Opción no existente. "+"\033[m")
            except ValueError:
                    print("\033[31m"+"Entrada inválida. Ingrese un número."+"\033[m")
    
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
    dni = input("\033[36m"+"\nIngresa tu DNI: "+"\033[m")
    password = input("\033[36m"+"Ingresa tu contraseña: "+"\033[m")
    account = search_account(dni=dni,password=password)
    account = search_account(dni=dni)
    if account is not None and account.password == password:
        system("cls")
        main_menu(account)
    else:
        system("cls")
        print("\033[31m"+"DNI o contraseña incorrectos. Por favor, inténtalo de nuevo."+"\033[m")
        login()
    

    # implementar logsica para buscar en la lista y comprobar si la cuenta ingresada es la correcta
    # si encuentra a la cuenta, entonces retornara esta cuenta. Si despues de iterar en la lista
    # no la encuentra, retornar None
    # utilzar búsqueda binaria
    
    # Nota: Si las entradas coinciden con una registrada, llamar al metodo
    # main_menu() pasandole el objeto de tipo account: main_menu(account)
    

def show_balance(account): 
    print("\033[32m"+f"Su saldo actual es: {account.balance} soles"+"\033[m")
    

def show_transactions(account):
    print("\033[33m"+"\nLISTA DE MOVIMIENTOS REGISTRADOS\n"+"\033[m")
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
        print("\033[32m"+f"Bienvenido {account.given_name}!"+"\033[m")
        print("\033[33m"+"1. Ver saldo")
        print("2. Ver transacciones")
        print("3. Hacer una transferencia")
        print("4. Pagar un servicio")
        print("5. Retirar dinero"+"\033[m")
        print("\033[31m"+"6. Salir"+"\033[m")
        
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
            withdraw_money(account, atm)
        elif option == "6":
            break

        else:
            print("\033[31m"+"Opción no válida"+"\033[m")

        input("\nPresione Enter para continuar...")

def make_transfer(account):
    destination_dni = input("\033[36m"+"Ingrese el DNI del destinatario: "+"\033[m") 
    # comprobar que la cuenta existe. Si no existe, salir del metodo. Utilizar el if general
    # puesto aquí. Para su "else" imprimir el mensaje de que esa cuenta no existe
    destination_account = ""
    if destination_account == "existe": # obvio, no se va a comparar con "existe" xddd
        amount = float(input("\033[36m"+"Ingrese el monto a transferir: "+"\033[m"))

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
            
            print("\033[32m"+"Transferencia exitosa!"+"\033[m")
        else:
            print("\033[31m"+"Saldo insuficiente"+"\033[m")
    else:
        print("\033[31m"+"Cuenta de destinatario no encontrada"+"\033[m")

def pay_service(account):
    
    # agregar logica para mostrar la lista de empresas: RUC y nombre comercial (tradename)
    
    ruc = input("\033[35m"+"Ingrese el RUC de la empresa de servicio: "+"\033[m")
    
    company = "search_company(ruc)" # devolver el objeto de tipo company o None con el metodo de busqueda binaria
    if company != None:
        amount = float(input("\033[36m"+"Ingrese el monto a pagar: "+"\033[m"))
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
            print("\033[32m"+"Pago de servicio exitoso!"+"\033[m")
        else:
            print("\033[31m"+"Saldo insuficiente"+"\033[m")
        
    else:
        print("\033[31m"+"Empresa de servicio no encontrada"+"\033[m")


# buenas practicas jeje
if __name__ == "__main__":
    
    # este codigo elije un cajero cada que aparezca el main
    
    while True:
        atm = random.choice(atm_list)
        main()
    
    