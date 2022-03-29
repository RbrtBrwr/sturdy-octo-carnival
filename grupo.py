from book import Book


class Group():
    book1 = None
    book2 = None
    book3 = None
    OF = None
    groupNumber = 0

    def checkData(self):
        print("grupo: {}".format(self.groupNumber))
        if self.book1 == None:
            return
        else:
            self.book1.showInfo()

        if self.book2 == None:
            return
        else:
            self.book2.showInfo()

        if self.book3 == None:
           return
        else:
            self.book3.showInfo()

        if self.OF == None:
            return
        else:
            return self.OF.checkData()

    def addBook(self, book):
        if self.book1 == None:
            self.book1 = book
        elif self.book2 == None:
            self.book2 = book
        elif self.book3 == None:
            self.book3 = book
        else:
            if self.groupNumber <= 6:
                if self.OF == None:
                    self.OF = Group()
                self.OF.setGroupNumber(self.groupNumber + 1)
                self.OF.addBook(book)
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
        if self.book1 != None and self.book1.title == bookTitle:
                if self.book2 != None:
                    storeBook = self.book2
                    self.removeBook(self.book2.title)
                    self.book1 = storeBook
                    return

                else:
                    self.book1 = None
                    return


        if self.book2 != None and self.book2.title == bookTitle:
                if self.book3 != None:
                    storeBook = self.book3
                    self.removeBook(self.book3.title)
                    self.book2 = storeBook
                    return

                else:
                    self.book2 = None


        if self.book3 != None and self.book3.title == bookTitle:
                if self.OF != None:
                    storeBook = self.OF.book1
                    self.OF.removeBook(self.OF.book1.title)
                    self.book3 = storeBook
                    return

                else:
                    self.book3 = None
                    return 

        print('CREO que ese libro no existe... creo...')
        return


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

    def searchBook(self, cota):
        # print(self.book1.cota)
        if self.book1 == None:
            return False
        elif self.book1.cota == cota:
            return self.book1
        elif self.book2 == None:
            return False
        elif self.book2.cota == cota:
            return self.book2
        elif self.book3 == None:
            return False
        elif self.book3.cota == cota:
            return self.book3
        elif self.OF == None:
            return False
        else:
            return self.OF.searchBook(cota)

