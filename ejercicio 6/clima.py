import requests

class Clima:
    __url = None
    __clima = None
    
    def __init__(self):
        self.__url = 'https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=564c4c901948a8f08a60d25f7a11040a'

    def conectar(self, nombreProvincia, nombreCapital):
        self.__solicitud = requests.get(self.__url.format(nombreProvincia))
        self.__clima = self.__solicitud.json()
        if self.__clima['cod'] == '404':
            self.__solicitud = requests.get(self.__url.format(nombreCapital))
            self.__clima = self.__solicitud.json()            

    def getTemperatura(self):
        temperatura = ''
        if self.__clima != None:
            temperatura = self.__clima['main']['temp']
        return temperatura
    
    def getTermica(self):
        termica = ''
        if self.__clima != None:
            termica = self.__clima['main']['feels_like']
        return termica

    def getHumedad(self):
        humedad = ''
        if self.__clima != None:
            humedad = self.__clima['main']['humidity']
        return humedad   
