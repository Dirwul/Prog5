import requests
import xml.etree.ElementTree as ET

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Vals(metaclass=Singleton):
    def __init__(self):
        self._rates = {}

    def getRawRates(self):
        url = "http://www.cbr.ru/scripts/XML_daily.asp"
        response = requests.get(url)
        return ET.fromstring(response.content)

    def parseRates(self, raw):
        for valute in raw.findall(".//Valute"):
            charCode = valute.find("CharCode").text
            nominal = int(valute.find("Nominal").text)
            value = valute.find("Value").text.replace(",", ".")
            rate = float(value) / nominal

            self._rates[charCode] = {
                "CharCode": charCode,
                "Rate": rate
            }

    def updateRates(self):
        self.parseRates(self.getRawRates())

    def getRates(self):
        self.updateRates()
        return self._rates
