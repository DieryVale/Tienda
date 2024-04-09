from enum import Enum

'''--------------------------------------------------------------------------------
# Enumeraciones 
-----------------------------------------------------------------------------------'''
class Tipo (Enum):
    '''-----------------------------------------------------------------------------
    # Enumeraciones
    --------------------------------------------------------------------------------'''
    PAPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3

class Producto:
     #  __subsidio = True 

    #  calidad = 'A'

    '''---------------------------------------------------------------------------
    # Constantes de la
    ------------------------------------------------------------------------------'''

    __IVA_PAPELERIA = 0.16
    __IVA_SUPERMERCADO = 0.04
    __IVA_FARMANCIA = 0.12 

    '''---------------------------------------------------------------------------
    # Atributos 
    ------------------------------------------------------------------------------'''  
    ''' __nombre = None 
    __tipo = Enum('Tipo', ['PAPELERIA', 'SUPERMERCADO', 'FARMACIA'])
    __valorUnitario = 0.0
    __cantidadBodega = 0                                               # al tenerlo en __init__, con el self pasa hacer las variables globales por ende no se nesecita estos atributos  
    __cantidadMinima = 0 
    __cantidadUnidadesVendidas = 0 '''

    '''----------------------------------------------------------------------------
    # Metodos 
    --------------------------------------------------------------------------------'''
    def __init__(self,pTipo, pNombre, pValorUnitario, pCantidadBodega, pCantidadMinima):
        self.__tipo = pTipo
        self.__nombre = pNombre
        self.__valorUnitario = pValorUnitario
        self.__cantidadBodega = pCantidadBodega
        self.__cantidadMinima = pCantidadMinima
        self.__cantidadUnidadesVendidas = 0 


    def getNombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__valorUnitario
    
    def getCantidadBodega(self):
        return self.__cantidadBodega
    
    def getCantidadMinima(self):
        return self.__cantidadMinima
    
    def getCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setTipo(self, tipo):
        self.__tipo = tipo
        
    def setValorUnitario(self, valorUnitario):
        self.__valorUnitario = valorUnitario    
        
    def setCantidadBodega(self, cantidadBodega):
        self.__cantidadBodega = cantidadBodega
    
    def setCantidadMinima(self, cantidadMinima):
        self.__cantidadMinima = cantidadMinima
        
    def setCantidadUnidadesVendidas(self, cantidadUnidadesVendidas):
        self.__cantidadUnidadesVendidas = cantidadUnidadesVendidas
    
    
    def vender(self, cantidad):
        if (cantidad <= self.__cantidadBodega):
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad 
            
        else:
            print("Cantidad no disponible.")
            
    # tarea crear un metodo hay suficiente devuelva tyrue false true si hay las unidades que deseo comprar y falso  en caso contrario.
    
    def haySuficiente(self, cantidad):
        # forma 1
        if(cantidad  <= self.__cantidadBodega):
            return True
        else:
            return False  
        # forma 2
        '''return cantidad  <= self.__cantidadBodega'''
        
        
    def getIVA(self):
        if (self.__tipo == "PAPELERIA"):
            return self.__IVA_PAPELERIA
        
        elif self.__tipo == "FARMACIA":
            return self.__IVA_FARMACIA
        
        elif self.__tipo == "SUPERMERCADO":
            return self.__IVA_SUPERMERCADO
        
        else:
            print("Categoría no soportata ")

    def subirValorUnitario(self):

        if(self.valorProducto < 1000):
            self.__valorUnitario += self.valorProducto * 0.1
        
        elif(self.valorProducto >= 1000 and self.valorProducto <= 5000):
            self.__valorUnitario += self.valorProducto * 0.2

        else: # cualquier producto si cuesta más de $ 5000 entra aqui
            self.__valorUnitario += self.valorProducto * 0.3

    def hacerPedido(self, pCantidad):
        if(self.__cantidadBodega < self.__cantidadMinima):
                self.__cantidadBodega += pCantidad
    
    def cambiarValorUnitario(self):
        if(self.__tipo == "DROGUERIA" or self.__tipo == "PAPELERIA"):
            self.__valorUnitario -= self.__valorUnitario * 0.1
        else: # se supone que es de tipo SUPERMERCADO|
            self.__valorUnitario += self.__valorUnitario * 0.5

    def nombreTipoProducto(self):
        self.tipoProducto = " "
        if self.__tipo == "SUPERMERCADO":           # lower: para modificar mayusculas pasandolas a minusculas 
         return "El producto es de "+ self.tipoProducto.lower()   
        else:
            self.tipoProducto = "Desconocido"     

    def aumentarValorUnitario(self):
        if self.__tipo == "DROGUERIA":
            self.__valorUnitario += self.__valorUnitario * 0.1
        
        elif self.__tipo == "SUPERMERCADO" or self.__tipo == "PAPELERIA":
           if  self.__tipo == "SUPERMERCADO":
               self.__valorUnitario += self.__valorUnitario * 0.3
           else:
               self.__valorUnitario += self.__valorUnitario * 0.2
        else:
            self.__tipo = "Desconosido"
               