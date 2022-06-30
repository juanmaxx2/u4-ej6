class Provincia:
    __nombre = ''
    __capital = ''
    __habitantes = 0
    __cantDepartamentos = 0

    def __init__(self,nombre,capital,habitantes,cantDeptos):
        self.__nombre = self.requerido(nombre,'Nombre es un valor requerido')
        self.__capital = self.requerido(capital,'Capital es un valor requerido')
        self.__habitantes = self.requerido(habitantes,'Habitantes es un valor requerido')
        self.__cantDepartamentos = self.requerido(cantDeptos,'Cantidad de departamentos es un valor requerido')
    
    def getNombre(self):
        return self.__nombre
    def getCapital(self):
        return self.__capital
    def getCantHabitantes(self):
        return self.__habitantes
    def getCantDepartamentos(self):
        return self.__cantDepartamentos
    
    def requerido(self,valor,mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        __atributos__=dict(
            nombre=self.__nombre,
            capital = self.__capital,
            habitantes = self.__habitantes,
            cantDeptos = self.__cantDepartamentos
            )
        )
        return d