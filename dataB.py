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
        cotaList = [item['cota'] for item in self.listaAuxiliar]
        print(cotaList)
        return cota in cotaList
            

    def checkSeriales(self, serial):
        serialList = [item['serial'] for item in self.listaAuxiliar]
        print(serialList)
        return serial in serialList
    
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
        # Llega hasta aqui el search pero aqui da False no se que hace esta funcion si ya tenemos que 
        # el titulo se encuentra lo podriamos sacar de una la info pero como lo hacemos "a" 
        book = self.grupos[hashBook].searchBook(cota)
        # Este book da un booleano esta mega sus hay que cambiar esto para que muestre bien la info el libro pero ya estoy rascado salu2 robert
        print("True o false di")
        if book:
            book.showInfo()
        else:
            print("El libro que busca no se encuentra en nuestra base de datos...")

        input('Presione cualquier tecla para continuar...')