# python 3.7 Flask
from flask import Flask, jsonify, abort, make_response, request
import urllib.parse
import urllib.request
import json

from create import Create
from delete_id import Delete_id
from read_id import Read_id
from read import Read
from update_id import Update_id


# Menu principal 
def menu():
    while True:
        print("\n_______________________________________________________________________________________________________________________________________________________")      
        print("\nMENU PRINCIPAL")
        print(" 1. Lista de clientes")
        print(" 2. Buscar cliente")
        print(" 3. Crear cliente") 
        print(" 4. Actualizar cliente") 
        print(" 5. Eliminar cliente") 

        print(" 0. Salir") 
        option = input("Opcion >>> ")

        if option == "1":             
            Read()
            
        elif option == "2":
            Read_id()
                    
        elif option == "3":
            Create()

        elif option == "4":
            Update_id()

        elif option == "5":
            Delete_id()                        

        elif option == "0":
            option2 = input("Seguro desea salir?\n 1. Si / 2. No : ")
            if option2 == "1":
                print("\nCerrando cliente...")             
                break 
                
            elif option2 == "2": 
                pass

            else:
                print("Digite una opción válida!")
        else:
            print("Digite una opción válida!")
            
    return 0

menu()    