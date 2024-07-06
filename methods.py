# main.py\
from ATM import ATM
from Account import *
from Company import *
from ServicePay import *
from Transaction import *
import random
from os import system

account_list = []
company_list = []
atm_list = []
atm = None

# creamos 10 cajeros xd
cities = ["JR. Amazonas 344", "Av. Miraflores 655", "Av. Larco 280", "Ov. Marinera 110", "Plazuela el Recreo 120", 
          "Av. César Vallejo 202", "Jr. Gamarra 518", "408 Av. Carlos Valderrama","1355 Av. Húsares de Junín", "1595 Av. Larco"]
for i in range(10):
    new_atm = ATM(i,cities[i], 20 * i, 25 * i, 18 * i, 33 * i , 28 * i)
    atm_list.append(new_atm)

# dispensamos billetes de manera iterativa
def dispensador(monto, billetes):
    billsel = []
    
    for bill, count in billetes:
        while monto >= bill and count > 0:
            billsel.append(bill)
            monto -= bill
            count -= 1
    return billsel

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
        atm.bill_two_hundred,
        atm.bill_one_hundred,
        atm.bill_fifty,
        atm.bill_twenty,
        atm.bill_ten
    ])
    #con esa variable comparamos y verificamos si el cajero tiene el dinero suficiente para retirar ese monto 
    if total_cash < user_amount:
        print("\033[31m"+"El cajero no tiene suficiente dinero para este retiro."+"\033[m")
        return

    # calculamos los billetes a dispensar
    bills_to_dispense = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0}

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

def binary_search(lista, target, atributo):
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        if getattr(lista[mid], atributo) == target:
            return lista[mid]
        elif getattr(lista[mid], atributo) < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def search_account(dni=None, email=None, phone_number=None):
    # account_list
    ordenar_cuentas_por_dni()
    if dni is not None:
        return binary_search(account_list, dni, 'dni')
    elif email is not None:
        return binary_search(account_list, email, 'email')
    elif phone_number is not None:
        return binary_search(account_list, phone_number, 'phone_number')
    else:
        return None
    
# creamos una empresa xd
new_company = [
    Company("878", "Quavii", "Quavii S.A.C.", "Ov. Marina 423", "925584321", "quavii@gmail.com.pe", 6700.0),
    Company("540", "Hidrandina", "Hidrandina S.A.", "Jr. San Martin 831", "948327474", "atencionhdna@distriluz.com.pe", 9700.0),
    Company("123", "Movistar", "Telefónica del Perú S.A.A.", "Av. Arequipa 1155", "980011800", "movistar@telefonica.com", 8500.0),
    Company("456", "Luz del Sur", "Luz del Sur S.A.A.", "Av. Canaval y Moreyra 380", "926175000", "info@luzdelsur.com.pe", 12000.0),
    Company("789", "Sedapal", "Servicio de Agua Potable y Alcantarillado de Lima S.A.", "Av. Alcazar 1154", "973256923", "info@sedapal.com.pe", 7500.0),
    Company("987", "Cálidda", "Cálidda S.A.C.", "Av. Juan de Arona 786", "906101515", "atencion@calidda.com.pe", 6500.0),
    Company("654", "Claro", "América Móvil Perú S.A.C.", "Av. Nicolás de Piérola 480", "945549780", "atencion@claro.com.pe", 7800.0),
    Company("321", "Entel", "Entel Perú S.A.", "Av. República de Panamá 3531", "980189834", "atencion@entel.pe", 8000.0),
    Company("543", "AquaSur", "AquaSur S.A.", "Av. La Marina 2100", "955600230", "aquasur@gmail.com.pe", 7000.0),
    Company("654", "Gas Natural Fenosa", "Gas Natural de Lima y Callao S.A.", "Av. Paseo de la República 3245", "968753297", "atencion@gasnaturalfenosa.com.pe", 7200.0),
    Company("765", "Bitel", "Viettel Perú S.A.C.", "Av. Pardo y Aliaga 640", "947051904", "info@bitel.com.pe", 6900.0)
    ]
for company in new_company: 
    company_list.append(company)

def search_company(ruc):
    if ruc is not None:
        return binary_search (company_list, ruc, 'ruc')
    else:
        return None
# implementar el metodo de quicksort por apellidos a la lista de cuentas
# cada que se registre un nuevo cliente
        
def quickSort(lista, atributo): # dni
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2] 
        left = [x for x in lista if getattr(x, atributo) < getattr(pivot, atributo)]
        middle = [x for x in lista if getattr(x, atributo) == getattr(pivot, atributo)]
        right = [x for x in lista if getattr(x, atributo) > getattr(pivot, atributo)]
        return quickSort(left, atributo) + middle + quickSort(right, atributo)

# 🎀 Esto en español xd , necesario para buscar debido al tipo de método de búsqueda :D
def ordenar_cuentas_por_dni():
    global account_list
    account_list = quickSort(account_list, 'dni')
    
    
# menu inicial
def main():
    print("\033[32m"+"\nBienvenid@ a BunnyBank:"+"\033[m")
    print("\033[33m"+" 1. Iniciar sesión")
    print(" 2. Registrarse"+"\033[m")       
    option = input("Seleccione una opción: ")
    if option == "1":
        account = login()
        if account != None:
            main_menu(account)
    elif option == "2":
        register()
        # mostrarLista(lista_ordenada)  #(lo puse para comprobar xd) 

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
        password = input("\033[36m"+"Contraseña: "+"\033[m")
        while True:
            # comprobar que sea mayor o igual a 500. Obvio, que los billetes sean ingresados a la atm
            balance = float(input("\033[35m"+"Depósito inicial: "+"\033[m"))
            
            if balance >= 500:
                ingreso_billetes(balance=balance)
                break                              
            else:
                print("\033[31m"+"Depósito inicial iválido."+"\033[m")
                print("\033[31m"+"El depósito inicial debe ser mayor o igual a 500."+"\033[m")
                print("\033[31m"+"No se admite monedas!"+"\033[m")
                print("\033[31m"+"Por favor, inténtalo de nuevo."+"\033[m")
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
        ordenar_cuentas_por_dni() 
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

def login():
    # En ingles por que zi :D
    attempts = 2  # 🎀 Le daré hasta 2 oportunidades al usuario 🎀
    
    for _ in range(attempts): # Iteramos ...
        dni = input("\033[36m"+"\nIngresa tu DNI: "+"\033[m")
        password = input("\033[36m"+"Ingresa tu contraseña: "+"\033[m")
        account = search_account(dni=dni)
        if account is not None and account.password == password:
            system("cls")
            main_menu(account)
            return
        else:
            system("cls")
            print("\033[31m"+"DNI o contraseña incorrectos. Por favor, inténtalo de nuevo."+"\033[m")
            # No considero necesario que se llame al login, se ingresa infinitamente
            # y no hay forma de salir despues xd
            # login() 
    
    # Si llega aquí... es porque el usuario es un ... falló ambos intentos :D
    system("cls")
    print("\033[1;33m"+"¿Estás registrado? ... ¿ SEGURO ?"+'\033[0;m') 

    main()  # Llamar al método main después de fallar ambos intentos
    
    # implementar logica para buscar en la lista y comprobar si la cuenta ingresada es la correcta
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
                print(f"{other.given_name.upper()} {other.last_name.upper()}        -S/ {t.amount}      {t.date}      {t.atm.address}")
            else:
                other = t.origin_account # mostrar datos de quien nos hizo la transaccion
                print(f"{other.given_name.upper()} {other.last_name.upper()}        S/ {t.amount}       {t.date}      {t.atm.address}")
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
    try:
        destination_dni = input("\033[36m"+"Ingrese el DNI del destinatario: "+"\033[m") 
        destination_account = search_account(dni=destination_dni)
        if destination_account is not None and destination_account == account: 
            print("No es posible realizar una tranferencia a tu misma cuenta.")
            return
        if destination_account is not None: 
            amount = float(input("\033[36m"+"Ingrese el monto a transferir: "+"\033[m"))
            
            if amount <= 0:
                print("\033[31m"+"El monto debe ser mayor a cero."+"\033[m")
                return

            if account.balance >= amount:
                account.balance -= amount
                destination_account.balance += amount
                    
                new_transaction = Transaction(
                    amount=amount,
                    origin_account=account,
                    destination_account=destination_account,
                    atm=atm
                )

                account.transactions.append(new_transaction)
                destination_account.transactions.append(new_transaction)
                
                print("\033[32m"+"Transferencia exitosa!"+"\033[m")
            else:
                print("\033[31m"+"Saldo insuficiente"+"\033[m")
        else:
            print("\033[31m"+"Cuenta de destinatario no encontrada"+"\033[m")
    
    except ValueError:
        print("\033[31m"+"Entrada inválida. Ingrese un valor numérico para el monto."+"\033[m")


# 🎀 Me aseguro de tener la lista de empresas ordenadas por RUC, para así
# Poder generar correctamente la busqueda - Recordar que el metodo de busqueda
# binaria, funciona correctamente con una lista previamente ordenada.
company_list = quickSort(company_list, 'ruc')
def pay_service(account):
    try:
        print("\033[35m" + "Lista de empresas disponibles:" + "\033[m")
        for company in company_list:
            print(f"RUC: {company.ruc}, Nombre Comercial: {company.tradename}")

        ruc = input("\033[35m"+"Ingrese el RUC de la empresa de servicio: "+"\033[m")
        company = search_company(ruc)
        
        if company is not None:
            amount = float(input("\033[36m"+"Ingrese el monto a pagar: "+"\033[m"))
            
            if amount <= 0:
                print("\033[31m"+"El monto debe ser mayor a cero."+"\033[m")
                return
            
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
    
    except ValueError:
        print("\033[31m"+"Entrada inválida. Ingrese un valor numérico para el monto."+"\033[m")


#Metodo para recibir el dinero

def receive_money(account, atm):
    try:
        user_amount = int(input("\033[33m"+"Ingrese la cantidad que desea retirar: "+"\033[m"))
    except ValueError:
        print("\033[31m"+"Entrada inválida. Ingrese un valor numérico por favor."+"\033[m")
        return

    if user_amount <= 0:
        print("\033[31m"+"El monto debe ser mayor a cero."+"\033[m")
        return

    if account.balance < user_amount:
        print("\033[31m"+"No tienes el saldo suficiente para realizar este retiro."+"\033[m")
        return

    total_cash = sum([
        atm.bill_two_hundred * 200,
        atm.bill_one_hundred * 100,
        atm.bill_fifty * 50, 
        atm.bill_twenty * 20,
        atm.bill_ten * 10
    ])

    if total_cash < user_amount:
        print("\033[31m"+"El cajero no tiene suficiente dinero para este retiro."+"\033[m")
        return

    bills_to_dispense = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0}

    bills = call_dispensador(user_amount, atm)

    if bills is None:
        print("\033[31m"+"No se pueden dispensar los billetes necesarios. Intenta con otro monto."+"\033[m")
        return

    for bill in bills:
        bills_to_dispense[bill] += 1
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

    account.balance -= user_amount

    print("\033[32m"+"Retiro exitoso, recibirás: "+"\033[m")
    for bill, count in bills_to_dispense.items():
        if count > 0:
            print(f"{count} billetes de {bill} soles")

# buenas practicas jeje
if __name__ == "__main__":
    
    # este codigo elije un cajero cada que aparezca el main
    
    while True:
        atm = random.choice(atm_list)
        main()
    
    