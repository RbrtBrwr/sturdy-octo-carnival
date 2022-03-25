from numpy import true_divide
from book import Book
from hashMe import hashMe

opcionYes = ['y','yeah','si','ok','yes']
opcionNo = ['n','nah','no','nope']

def pantallaBusqueda():
    value = input("""
    Elija Opcion De Busqueda:
    1. Titulo
    2. Serial
    3. Cota
    
    >
    """)

    if value == '1':
        # TODO
        return "titulo"
    elif value == '2':
        # TODO
        return "serial"
    elif value == '3':
        # TODO
        return "cota"
    else:
        print ("Ingrese una opcion valida...\n\n")
        return pantallaBusqueda()

def revisarTitulo(dataBase, bookTitle):
    if bookTitle not in dataBase:
        return False
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


    


def registroDeLibros():
    value = True
    while value:
        pass
        # TODO Revisar a ver si el nombre esta en la base de datos ya. 



def pantallaInicio():
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
        return "Rgistrar"
    elif value == '2':
        return "Agregar"
    elif value == '3':
        return "Eliminar"
    elif value == '4':
        return "eliminar"
    elif value == '5':
        return pantallaInicio()
    elif value.lower() == 'exit':
        print("\n\n\n")
        return pantallaBienvenida()
    else:
        print("Por favor ingrese una opcion valida...\n\n")
        return pantallaInicio()

def pantallaBienvenida():
    value = input("""Bienvenido a La Biblioteca
    Presione Cualquier Tecla Para Continuar
    > """)
    if value.lower() == 'exit':
        exit()
    else:
        print("Por favor ingrese una opcion valida...")
        return pantallaInicio()

def agregarLibro(cota, titulo, serial, cantidad, baseDatos):
    nuevoLibro = Book(titulo, cota, serial, cantidad)
    baseDatos.addBook(nuevoLibro)


def main():
    print(pantallaBienvenida())

if __name__ == '__main__':
    main()
    