from Model.Account import Account
from Model.ATM import ATM
from Model.Company import Company
from Model.ServicePay import ServicePay
from Model.Transaction import Transaction
import getpass
import os
from methods import *
import time

# menu inicial
def main():
    clear_screen()    
    print("\nBienvenid@ a BunnyBank:")
    print(" 1. Iniciar sesión")
    print(" 2. Registrarse")       
    option = input("Seleccione una opción: ")
    if option == "1":
        account  = login()
        if account == None:
            temporizador("Esta cuenta no existe...", 3)
        else:
            temporizador("Validando datos...", 4)
            main_menu(account)
    elif option == "2":
        register()  
        
 
      

# jejeeeeeeee simule un contador xdddd
def temporizador(texto, tiempo):
    count = tiempo
    while count >= 0:
        clear_screen()
        print('>' * count * 2) 
        print(texto)
        print(f"{count}s")  
        time.sleep(1)
        count -= 1

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
    
    session.add(new_account)
    session.commit()
     
    temporizador("Registro exitoso!", 3)
    '''
    
    while True:
        main()
    
    
    # cuando el usuario vaya a crear una cuenta, preguntar si quiere ingresar dinero
    # de esta manera inicializamos "balance" con ese valor. Obvio, solo billetitos
