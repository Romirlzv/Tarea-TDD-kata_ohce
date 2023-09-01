import pytest
from src.ohce import Ohce
import unittest
from unittest.mock import patch
import datetime
class Test_Ohce(unittest.TestCase):

    @patch('builtins.input', side_effect=['hola'])
    def test_reversa(self, mock_input):
        ohce = Ohce('Pedro')
        self.assertEqual(ohce.palabras('hola'), 'aloh')
    
    @patch('builtins.input', side_effect=['reconocer'])
    def test_palindromo(self, mock_input):
        ohce = Ohce('Pedro')
        self.assertEqual(ohce.palabras('reconocer'), 'reconocer\n¡Bonita palabra!')
        self.assertEqual(ohce.palabras('luz azul'), 'luza zul\n¡Bonita palabra!')
        self.assertEqual(ohce.palabras('Amor a roma'), 'amor a romA\n¡Bonita palabra!')
        
    @patch('datetime.datetime')
    def test_saludo_buenas_noches(self, mock_datetime):
        mock_datetime.now.return_value.hour = 20 
        ohce = Ohce('Pedro')
        self.assertEqual(ohce.saludos(), '¡Buenas noches Pedro!')
        mock_datetime.now.return_value.hour = 5
        self.assertEqual(ohce.saludos(), '¡Buenas noches Pedro!')
        mock_datetime.now.return_value.hour = 23
        self.assertEqual(ohce.saludos(), '¡Buenas noches Pedro!')

    @patch('datetime.datetime')
    def test_saludo_buenas_dias(self, mock_datetime):
        mock_datetime.now.return_value.hour = 6 
        ohce = Ohce('Pedro')
        self.assertEqual(ohce.saludos(), '¡Buenos días Pedro!')
        mock_datetime.now.return_value.hour = 11
        self.assertEqual(ohce.saludos(), '¡Buenos días Pedro!')
        mock_datetime.now.return_value.hour = 7
        self.assertEqual(ohce.saludos(), '¡Buenos días Pedro!')
