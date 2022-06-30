import json
from pathlib import Path

class ObjectEncoder:
    __pathArchivo = None

    def __init__(self, pathArchivo):
        self.__pathArchivo = pathArchivo

    def guardarJSONArchivo(self, lista):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(lista, destino, indent = 4)
            destino.close()
            
    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding = "UTF-8") as fuente:
            lista = json.load(fuente)
            fuente.close()
            return lista