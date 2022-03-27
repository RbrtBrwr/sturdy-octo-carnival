from grupo import Group
from hashMe import hashMe


class DataB():
    listaCotas = []
    listaSeriales = []
    listaTitulos = []
    grupos = [Group(), Group()]
    listaAuxiliar = []


    def addBook(self, book):
        hashBook = hashMe(book.cota)
        self.grupos[hashBook].addBook(book)

        aux = {'cota': book.cota, 'title':book.title, 'serial':book.serial}
        self.listaAuxiliar.append(aux)

    # estas retornan falso si no encuentran el valor en la lista
    # TODO esto podria hacer las listas atributos de dataB? o se si se 
    # updatearian automaticamente cuando agrego o quito vainas
    def checkCotas(self, cota):
        return len(list(filter(lambda x: x['cota'].lower() == cota.lower(), self.listaAuxiliar))) < 0

            

    def checkSeriales(self, serial):
        return len(list(filter(lambda x: x['serial'].lower() == serial.lower(), self.listaAuxiliar))) < 0

    
    def checkTitles(self, title):
        print(list(filter(lambda x: x['serial'].lower() == title.lower(), self.listaAuxiliar)))
        return len(list(filter(lambda x: x['title'].lower() == title.lower(), self.listaAuxiliar))) < 0


    def searchBook(self, cota):
        hashBook = hashMe(cota)
        book = self.grupos[hashBook].searchBook(cota)
        if book:
            book.showInfo()
        else:
            print("El libro que busca no se encuentra en nuestra base de datos...")

        input('Presione cualquier tecla para continuar...')