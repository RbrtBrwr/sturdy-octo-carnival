from turtle import title
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
        selectedGroup = self.grupos[hashBook]
        selectedGroup.addBook(book)

        aux = {'cota': book.cota, 'title':book.title, 'serial':book.serial, 'cantidad':book.available}
        self.listaAuxiliar.append(aux)

    def checkData(self):
        print('lista cotas ----------------')
        print(self.listaCotas)
        print('lista seriales ---------------')
        print(self.listaSeriales)
        print('lista titulos --------------------')
        print(self.listaTitulos)
        print('lista auxiliar ----------------')
        print(self.listaAuxiliar)
        
        for i in self.grupos:
            i.checkData()

        
    def checkCotas(self, cota):
        # return len(list(filter(lambda x: x['cota'].lower() == cota.lower(), self.listaAuxiliar))) < 0          
        cotaList = [item['cota'] for item in self.listaAuxiliar]
        i = 0
        epa = False
        while (i < len(cotaList)):

            if (cotaList[i].lower() == cota.lower()):
                epa = True
                break

            i = i + 1    
        return epa

    def checkSeriales(self, serial):
        # return len(list(filter(lambda x: x['serial'].lower() == serial.lower(), self.listaAuxiliar))) < 0
        serialList = [item['serial'] for item in self.listaAuxiliar]
        i = 0
        epa = False
        while (i < len(serialList)):

            if (serialList[i].lower() == serial.lower()):
                epa = True
                break

            i = i + 1    
        return epa
    
    def checkTitles(self, title):
        titleList = [item['title'] for item in self.listaAuxiliar]
        i = 0
        epa = False
        while (i < len(titleList)):

            if (titleList[i].lower() == title.lower()):
                epa = True
                break

            i = i + 1    
        return epa

    def searchBook(self, cota):
        hashBook = hashMe(cota)
        book = self.grupos[hashBook].searchBook(cota)
        if book:
            book.showInfo()
        else:
            print("El libro que busca no se encuentra en nuestra base de datos...")

        input('Presione cualquier tecla para continuar...')

    def findBook(self, cota):
        hashBook = hashMe(cota)
        book = self.grupos[hashBook].searchBook(cota)
        if book:
            return book
        else:
            print("El libro que busca no se encuentra en nuestra base de datos...")

        input('Presione cualquier tecla para continuar...')
    
    def borrowBook(self, cota):
        hashBook = hashMe(cota)
        book = self.grupos[hashBook].searchBook(cota)
        if book:
            if book.available > 0:
                book.available = book.available - 1
                book.unavailable = book.unavailable + 1
                print("Se ha realizado un prestamo del libro {}".format(book.title))
            else:
                print("No tenemos ejemplares de ese libro en este momento...")
        else:
            print("El libro que busca no se encuentra en nuestra base de datos...")

        input('Presione cualquier tecla para continuar...')
    
    def returnBook(self, cota):
        hashBook = hashMe(cota)
        book = self.grupos[hashBook].searchBook(cota)
        if book:
            book.available = book.available + 1
            book.unavailable = book.unavailable - 1
            print("Se ha regresado el libro {}".format(book.title))
        else:
            print("El libro que busca no se encuentra en nuestra base de datos...")

        input('Presione cualquier tecla para continuar...')

    def addCopy(self, cota, quantity):
        hashBook = hashMe(cota)
        book = self.grupos[hashBook].searchBook(cota)
        if book:
            book.available = book.available + quantity
            for bookInfo in self.listaAuxiliar:
                if (bookInfo.get("title") == book.title):
                    bookInfo["cantidad"] = book.available
            print("Se han agregado {} copias del libro {}".format(quantity, book.title))
        else:
            print("El libro no se encuentra en nuestra base de datos, si desea puede registrarlo...")

        input('Presione cualquier tecla para continuar...')

    def removeBook(self, cota):
        hashBook = hashMe(cota)
        book = self.grupos[hashBook].searchBook(cota)
        if book:
            self.grupos[hashBook].removeBook(book.title)
            print('Todos los ejemplares del libro {} han sido quemados'.format(book.title))
        else:
            print('No hay ejemplares que quemar...')

        input('Presione cualquier tecla para continuar...')

    def findCota(self, title, action, quantity=0):
        for i in self.listaAuxiliar:
            if i['title'].lower() == title.lower():
                if action == 'prestamo':
                    self.borrowBook(i['cota'])
                    return
                elif action == 'regreso':
                    self.returnBook(i['cota'])
                    return
                elif action == 'agregar':
                    self.addCopy(i['cota'], quantity)
                    return
                elif action == 'eliminar':
                    value = input('Escriba "CONFIRMAR" si desea eliminar este libro: ')
                    if value.lower() == 'confirmar':
                        self.removeBook(i['cota'])
                    else:
                        print('Cancelada la eliminacion...')
                    return
        
        print("Se ha presentado un problemilla...")