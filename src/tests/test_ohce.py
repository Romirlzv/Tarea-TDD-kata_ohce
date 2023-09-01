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
    
