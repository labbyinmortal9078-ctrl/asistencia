# Proyecto: Control de Asistencia SCM - Práctica
# Autor: psosa

def validar_dni(dni: str) -> bool:
    """
    Valida que un DNI tenga exactamente 8 dígitos numéricos.
    Regla: debe tener 8 caracteres y todos deben ser dígitos.
    """
    if not isinstance(dni, str):
        return False
    if len(dni) != 8:
        return False
    return dni.isdigit()


def calcular_asistencia(presentes: int, total: int) -> float:
    """
    Calcula el porcentaje de asistencia.
    Regla: total debe ser mayor a 0.
    """
    if total <= 0:
        raise ValueError("El total de clases debe ser mayor a 0")
    return (presentes / total) * 100


if __name__ == "__main__":
    print("Sistema de Asistencia - psosa")
    print(validar_dni("12345678"))  # True
    print(calcular_asistencia(8, 10))  # 80.0