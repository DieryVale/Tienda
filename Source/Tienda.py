from Producto import Producto 

class Tienda:
    '''---------------------------------------------------------------------------
    # Atributos 
    ------------------------------------------------------------------------------'''
    ''' __producto1 = None
    __producto2 = None 
    __producto3 = None    # igual que en producto
    __producto4 = None 
    __dineroEnCaja = 0.0'''

    '''-----------------------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------------------'''
    def __init__(self):
        self.__producto1 = Producto("PAPELERIA", "LAPIZ", 500, 30, 9)
        self.__producto2 = Producto("PAPELERIA", "BORRADOR", 300, 15, 5)
        self.__producto3 = Producto("SUPERMERCADO", "CAFE", 5600, 20, 10)
        self.__producto4 = Producto("DROGUERIA", "DESINFECTANTE", 3200, 12, 11)
        self.__dineroEnCaja = 0.0


    def getProducto1(self):
        return self.__producto1
    
    def getProducto2(self):
        return self.__producto2
    
    def getProducto3(self):
        return self.__producto3
    
    def getProducto4(self):
        return self.__producto4
    
    def getdineroEnCaja(self):
        return self.__dineroEnCaja