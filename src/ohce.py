import unittest
from unittest.mock import patch

class Ohce:
    def __init__(self, nombre):
         self.nombre = nombre
    
    def palabras(self, palabra_input):
        palabra = palabra_input.lower().replace(" ", "")
        reversa = palabra[::-1]
        if palabra == reversa:
            return reversa + "\n" + "¡Bonita palabra!"
        return reversa
    
    def saludos(self):
        import datetime
        
        hora_actual = datetime.datetime.now().hour
        if 20 <= hora_actual or hora_actual < 6:
            return f'¡Buenas noches {self.nombre}!'
        elif 6 <= hora_actual or hora_actual < 12:
            return f'¡Buenos días {self.nombre}!'
        

