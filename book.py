import this


class Book():
    
    def __init__(self, title, cota, serial, quantity=1):
        self.title = title
        self.cota = cota
        self.serial = serial
        self.available = quantity
        self.unavailable = 0
        self.total = quantity
    
    def addCopy(self, quantity):
        self.available = self.available + quantity


