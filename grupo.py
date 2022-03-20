from hashlib import new
from black import nullcontext


class Group():
    book1 = None
    book2 = None
    book3 = None
    OF = None
    groupNumber = 0

    def addBook(self, book):
        if self.book1 != None:
            self.book1 = book
        elif self.book2 != None:
            self.book2 = book
        elif self.book3 != None:
            self.book3 = book
        else:
            if self.groupNumber <= 6:
                self.OF = Group()
                self.OF.setGroupNumber(self.groupNumber + 1)
            else:
                print("El grupo se ha llenado completamente...")
   
    def addBookCopy(self, bookTitle, quantity):
        # Estoy considerando que nadie va a devolver mas de un ejemplar del mismo libro a la vez
        if self.book1 != None and self.book1.title == bookTitle:
            self.book1.addCopy(quantity)
        elif self.book2 != None and self.book2.title == bookTitle:
            self.book2.addCopy(quantity)
        elif self.book3 != None and self.book3.title == bookTitle:
            self.book3.addCopy(quantity)
        elif self.OF != None:
            self.OF.addBookCopy(bookTitle, quantity)
        else:
            # TODO aqui podria poner la opcion de donar un libro para meterlo en la base de datos
            print('El libro que deseas devolver no esta en nuestra base de datos...')
    
    def setGroupNumber(self, number):
        self.groupNumber = number

    def removeBook(self, bookTitle):
        """
            TODO
            Primero busco para ver si existe
            Como los titulos tienen que ser unicos tambien busco por titulo y ya
        """
        if self.book1 != None and self.book1.title == bookTitle:
            if self.book2 != None:
                self.book1 = self.book2
                self.removeBook(self.book2.title)
            else:
                self.book1 = None

        elif self.book2 != None and self.book2.title == bookTitle:
            if self.book3 != None:
                self.book2 = self.book3
                self.removeBook(self.book3.title)
            else:
                self.book2 = None

        elif self.book3 != None and self.book3.title == bookTitle:
            if self.OF != None:
                self.OF.removeBook(self.OF.book1.title)
            else:
                self.book3 = None
        else:
            print('CREO que ese libro no existe... creo...')
        
        if self.OF.book1 == None:
            self.OF = None

    def leaseBook(self, bookTitle):
        # Estoy considerando que nadie va a alquilar mas de un ejemplar de un mismo libro a la vez
        if self.book1 != None and self.book1.title == bookTitle:
            if self.book1.available > 0:
                self.book1.available = self.book1.available - 1
                self.book1.unavailable = self.book1.unavailable + 1
            else:
                print('No quedan ejemplares de ese libro, por favor volver mas tarde... ')
        elif self.book2 != None and self.book2.title == bookTitle:
            if self.book2.available > 0:
                self.book2.available = self.book2.available - 1
                self.book2.unavailable = self.book2.unavailable + 1
            else:
                print('No quedan ejemplares de ese libro, por favor volver mas tarde... ')
        elif self.book3 != None and self.book3.title == bookTitle:
            if self.book3.available > 0:
                self.book3.available = self.book3.available - 1
                self.book3.unavailable = self.book3.unavailable + 1
            else:
                print('No quedan ejemplares de ese libro, por favor volver mas tarde... ')
        elif self.OF != None:
            self.OF.leaseBook(bookTitle)
        else:
            print('El libro que buscas no esta en nuestra base de datos...')

    def returnBook(self, bookTitle):
        # Estoy considerando que nadie va a devolver mas de un ejemplar del mismo libro a la vez
        if self.book1 != None and self.book1.title == bookTitle:
            if self.book1.unavailable > 0:
                self.book1.unavailable = self.book1.unavailable - 1
                self.book1.available = self.book1.available + 1
            else:
                print('Ese libro no es nuestro... ')
        elif self.book2 != None and self.book2.title == bookTitle:
            if self.book2.unavailable > 0:
                self.book2.unavailable = self.book2.unavailable - 1
                self.book2.available = self.book2.available + 1
            else:
                print('Ese libro no es nuestro... ')
        elif self.book3 != None and self.book3.title == bookTitle:
            if self.book3.unavailable > 0:
                self.book3.unavailable = self.book3.unavailable - 1
                self.book3.available = self.book3.available + 1
            else:
                print('Ese libro no es nuestro... ')
        elif self.OF != None:
            self.OF.returnBook(bookTitle)
        else:
            # TODO aqui podria poner la opcion de donar un libro para meterlo en la base de datos
            print('El libro que deseas devolver no esta en nuestra base de datos...')
