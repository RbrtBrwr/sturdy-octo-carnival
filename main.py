from sympy import false
from book import Book
from dataB import DataB
from hashMe import hashMe
import json
import ast
import pdb

opcionYes = ['y','yeah', 'si','ok' ,'yes', 'si va']
opcionNo =  ['n','nah','no','nope', 'no way josay']

def chequeoTxt(dataBase):
    everything = open('DiscoDuro.txt', 'r')
    libros = everything.read().split("\n")
    i = 0
    while (i < (len(libros)- 1)):
        diccionarioLibros = ast.literal_eval(libros[i])
        # cantidad = diccionarioLibros.get("cantidad")
        newLibro = Book(diccionarioLibros.get("title"), diccionarioLibros.get("cota"), diccionarioLibros.get("serial"))
        dataBase.addBook(newLibro)
        i = i + 1 
    print(dataBase.listaAuxiliar)

def actualizoTxt(dataBase):
    z = 0
    with open('DiscoDuro.txt', 'w') as writeCS:
        while (z < len(dataBase.listaAuxiliar)):
            writeCS.write(json.dumps(dataBase.listaAuxiliar[z])+"\n")
            z = z + 1




def buscarTitulo(dataBase):
    value = input("Titulo: ")
    
    if dataBase.checkTitles(value):
        for i in dataBase.listaAuxiliar:

            if i['title'].lower() == value.lower():

                dataBase.searchBook(i['cota'])
                return pantallaInicio(dataBase)
        
        print("Se ha presentado un problemilla...")

    else:
        print('No tenemos ese libro...')
        return pantallaInicio(dataBase)

def buscarSerial(dataBase):
    value = input("Serial: ")
    if dataBase.checkSeriales(value):
        for i in dataBase.listaAuxiliar:
            if i['serial'].lower() == value.lower():
                dataBase.searchBook(i['cota'])
                return pantallaInicio(dataBase)
        
        print("Se ha presentado un problemilla...")

    else:
        print('No tenemos ese libro...')
        return pantallaInicio(dataBase)

def buscarCota(dataBase):
    value = input("Cota: ")
    if dataBase.checkCotas(value):
        dataBase.searchBook(value)
        return pantallaInicio(dataBase)

    else:
        print('No tenemos ese libro...')
        return pantallaInicio(dataBase)

def pantallaBusqueda(dataBase):
    value = input("""
    Elija Opcion De Busqueda:
    1. Titulo
    2. Serial
    3. Cota
    
    >
    """)

    if value == '1':
        return buscarTitulo(dataBase)
    elif value == '2':
        return buscarSerial(dataBase)
    elif value == '3':
        return buscarCota(dataBase)
    else:
        print ("Ingrese una opcion valida...\n\n")
        return pantallaBusqueda()

def revisarTitulo(dataBase, bookTitle):
    if bookTitle not in dataBase.listaTitulos:
        return True
    else:
        value = input("""El libro ya se encuentra registrado...
        Desea agregar ejemplares?
        (Y/N) > """)
        if value in opcionYes:
            pass
            # TODO
            # return agregarEjemplar
        if value in opcionNo:
            pass 
            # TODO en verdad no se que va a pasar aqui


    


def registroDeLibros(dataBase):
    print("Datos del libro a registrar:\n")
    value = True
    while value:
        # TODO Revisar a ver si el nombre esta en la base de datos ya. 
        title = input("Titulo: ")
        if dataBase.checkTitles(title):
            value = False
        # else:
            # TODO aqui pongo el mensaje de error o solo lo imprimo dentro de revisarTitulo y ya?
        else:
            value = False

    value = True
    while value:

        serial = input('Serial: ').strip()
        if serial.lower() == 'exit':
            return pantallaInicio()

        if len(serial) != 12:
            print("El serial debe contener 12 digitos, por favor ingresarlos todos...")
        elif not serial.isdigit():
            print("Todos los caracteres deben ser numericos...")
        elif dataBase.checkSeriales(serial):
            print("Este serial esta asignado a otro libro. Revise que ha sido ingresado correctamente e intente nuevamente...")
        else:
            value = False

    value = True
    while value:
        cota = input("Cota: ").strip()
        if cota.lower() == 'exit':
            return pantallaInicio()

        if len(cota) != 8:
            print("La cota esta conformada por 6 letras seguidas de 2 digitos...")
        elif not cota[0:6].isalpha():
            print("La cota esta conformada por 6 /letras seguidas de 2 digitos...")
        elif not cota[6:].isnumeric():
            print("La cota esta conformada por 6 letras seguidas de 2 /digitos...")
        elif dataBase.checkCotas(cota):
            print("Esta cota ya se encuantra registrada...")
        else:
            value = False
    

    quantity = input("Si desea agregar mas de un ejemplar, por favor indicar cuantos... \nDe lo contrario, presionar enter...\n > ")
    if quantity.lower() == 'exit':
        return pantallaInicio() 
    
    if serial.isnumeric() and int(quantity) > 0:
        quantity = int(quantity)
    else:
        print("Se registrara un solo ejemplar...")
        quantity = 1

    newBook = Book(title, cota, serial, quantity)
    dataBase.addBook(newBook)

    print("""El libro ha sido registrado exitosamente...""")
    newBook.showInfo()
    actualizoTxt(dataBase)
    return pantallaInicio(dataBase)

    # TODO y ya?...
    
            






def pantallaInicio(dataBase):
    value = input("""
    Bienvenido <Human Name>
    Ingrese el numero de la accion que desea realizar:
    1. Registrar Nuevo Libro
    2. Agregar Ejemplares
    3. Realizar Prestamo
    4. Reingresar Un Libro
    5. Buscar Libros

    Ingrese EXIT para salir
    > 
    """)
    if value == '1':
        print(dataBase.listaAuxiliar, dataBase.listaCotas)
        return registroDeLibros(dataBase)
    elif value == '2':
        return "Agregar"
    elif value == '3':
        return "Eliminar"
    elif value == '4':
        return "eliminar"
    elif value == '5':
        return pantallaBusqueda(dataBase)
    elif value.lower() == 'exit':
        print("\n\n\n")
        return pantallaBienvenida(dataBase)
    else:
        print("Por favor ingrese una opcion valida...\n\n")
        return pantallaInicio(dataBase)

def pantallaBienvenida(dataBase):
    value = input("""Bienvenido a La Biblioteca
    Presione Cualquier Tecla Para Continuar
    > """)
    if value.lower() == 'exit':
        exit()
    else:
        return pantallaInicio(dataBase)

def agregarLibro(cota, titulo, serial, cantidad, baseDatos):
    nuevoLibro = Book(titulo, cota, serial, cantidad)
    baseDatos.addBook(nuevoLibro)


def main():
    # TODO
    # Aqui voy a inicialiar la base de datos, le voy a crear un metodo para cargarle la info desde un txt y si no hay txt, la inicializ vacia ya
    dataBase = DataB()
    # Me falta chequear si hay libros en la base de datos o no
    chequeoTxt(dataBase)
    print(dataBase.listaAuxiliar)
    # Metodo para agregar Jsons en el txt
    # actualizoTxt(dataBase)
    pantallaBienvenida(dataBase)

if __name__ == '__main__':
    pdb.run(main())
    