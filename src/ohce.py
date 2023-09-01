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
        

