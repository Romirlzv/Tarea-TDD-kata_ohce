import pytest
from src.ohce import ohce

def test_reversa():
    assert ohce("hola") == "aloh"