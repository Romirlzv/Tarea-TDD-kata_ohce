import pytest
from src.ohce import ohce

def test_reversa():
    assert ohce("hola") == "aloh"
    
def test_palindromo():
    assert ohce("reconocer") == "reconocer" + "\n" "¡Bonita palabra!"