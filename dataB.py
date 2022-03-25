from grupo import Group
from hashMe import hashMe


class DataB():
    listaCotas = []
    listaSeriales = []
    grupos = [Group(), Group()]

    def addBook(self, book):
        hashBook = hashMe(book.cota)
        self.grupos[hashBook].addBook(book)
        self.listaCotas.append((book.cota, book.title))
        self.listaSeriales.append((book.serial, book.title))

    # def searchCotas(self, cota):
        # el problema aqui es que al tener los sets en la lista de cotas entonces me jode la paciencia

    def searchBook(self, cota):
        hashBook = hashMe(cota)
        book = self.grupos[hashBook].searchBook(cota)
        if book:
            print("""
            Titulo: {}
            Serial: {}
            Cota: {}
            Total: {}
            Disponibles: {}
            """.format(book.title, book.serial, book.cota, book.available + book.unavailable, book.available))
        else:
            print("El libro que busca no se encuentra en nuestra base de datos...")
