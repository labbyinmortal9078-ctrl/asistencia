import pytest
from main import validar_dni, calcular_asistencia


# --- Pruebas para validar_dni ---

def test_dni_valido():
    """Un DNI de 8 dígitos debe ser válido."""
    assert validar_dni("12345678") is True


def test_dni_muy_corto():
    """Un DNI de menos de 8 dígitos debe ser inválido."""
    assert validar_dni("1234567") is False


def test_dni_muy_largo():
    """Un DNI de más de 8 dígitos debe ser inválido."""
    assert validar_dni("123456789") is False


def test_dni_con_letras():
    """Un DNI con letras debe ser inválido."""
    assert validar_dni("1234abcd") is False


# --- Pruebas para calcular_asistencia ---

def test_asistencia_80_por_ciento():
    """8 de 10 clases debe dar 80%."""
    assert calcular_asistencia(8, 10) == 80.0


def test_asistencia_total_cero():
    """Si el total es 0, debe lanzar ValueError."""
    with pytest.raises(ValueError):
        calcular_asistencia(5, 0)