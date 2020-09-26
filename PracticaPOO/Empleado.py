
class Empleado:

    def __init__(self):
        self.__nombre = None #String o texto
        self.__apellidos = None #String o texto
        self.__sueldo = None #float o decimal
        self.__diasLiquidados = None #intero


 # get que para mostrar la variable
 # Set que es para modificar la    

    def getNombre(self):
        return self.__nombre

    def getApellidos(self):
        return self.__apellidos

    def getSueldo(self):
        return self.__sueldo
    
    def getDiasLiquidados(self):
        return self.__diasLiquidados

    def setNombre(self, nombre:str):
        self.__nombre = nombre

    def setApellido(self, apellidos:str):
        self.__apellidos = apellidos

    def setSueldo(self, sueldo:float):
        self.__sueldo = sueldo

    def setDiasLiquidados(self, dias:int):
        self.__diasLiquidados = dias

    def SalarioDevengado(self):
        return (self.__sueldo / 30) * int(self.__diasLiquidados)

    def __str__(self):
        return str('Nombre: ' + self.__nombre +
                    '\n Apellido: '+ self.__apellidos +
                    '\n Sueldo: ' + str(self.__sueldo) + 
                    '\n Salario Devengado: ' + str(self.SalarioDevengado()))






