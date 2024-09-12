# Módulo: operaciones_fracciones.py
# Autor: Ángel Alcántar
# Descripción: Módulo que contiene funciones para realizar operaciones con fracciones.

import math

def simplificar_fraccion(numerador, denominador):
    """
    Simplifica una fracción.

    Args:
        numerador (int): Numerador de la fracción.
        denominador (int): Denominador de la fracción.

    Returns:
        tuple: Numerador y denominador simplificados.
    """
    try:
        if denominador == 0:
            return "Error: el denominador no puede ser cero."
        gcd = math.gcd(numerador, denominador)
        return (numerador // gcd, denominador // gcd)
    except TypeError:
        return "Error: el numerador y el denominador deben ser enteros."


def sumar_fracciones(frac1, frac2):
    """
    Suma dos fracciones.

    Args:
        frac1 (tuple): Primera fracción como (numerador, denominador).
        frac2 (tuple): Segunda fracción como (numerador, denominador).

    Returns:
        tuple: Fracción resultante simplificada.
    """
    try:
        num1, denom1 = frac1
        num2, denom2 = frac2
        
        # Encontrar denominador común
        denominador_comun = denom1 * denom2
        numerador_resultante = num1 * denom2 + num2 * denom1
        
        return simplificar_fraccion(numerador_resultante, denominador_comun)
    except (TypeError, ValueError):
        return "Error: las fracciones deben ser tuplas de enteros."


def restar_fracciones(frac1, frac2):
    """
    Resta dos fracciones.

    Args:
        frac1 (tuple): Primera fracción como (numerador, denominador).
        frac2 (tuple): Segunda fracción como (numerador, denominador).

    Returns:
        tuple: Fracción resultante simplificada.
    """
    try:
        num1, denom1 = frac1
        num2, denom2 = frac2
        
        # Encontrar denominador común
        denominador_comun = denom1 * denom2
        numerador_resultante = num1 * denom2 - num2 * denom1
        
        return simplificar_fraccion(numerador_resultante, denominador_comun)
    except (TypeError, ValueError):
        return "Error: las fracciones deben ser tuplas de enteros."


def multiplicar_fracciones(frac1, frac2):
    """
    Multiplica dos fracciones.

    Args:
        frac1 (tuple): Primera fracción como (numerador, denominador).
        frac2 (tuple): Segunda fracción como (numerador, denominador).

    Returns:
        tuple: Fracción resultante simplificada.
    """
    try:
        num1, denom1 = frac1
        num2, denom2 = frac2
        
        numerador_resultante = num1 * num2
        denominador_resultante = denom1 * denom2
        
        return simplificar_fraccion(numerador_resultante, denominador_resultante)
    except (TypeError, ValueError):
        return "Error: las fracciones deben ser tuplas de enteros."


def dividir_fracciones(frac1, frac2):
    """
    Divide dos fracciones.

    Args:
        frac1 (tuple): Primera fracción como (numerador, denominador).
        frac2 (tuple): Segunda fracción como (numerador, denominador).

    Returns:
        tuple: Fracción resultante simplificada.
    """
    try:
        num1, denom1 = frac1
        num2, denom2 = frac2
        
        if num2 == 0:
            return "Error: no se puede dividir entre cero."

        numerador_resultante = num1 * denom2
        denominador_resultante = denom1 * num2
        
        return simplificar_fraccion(numerador_resultante, denominador_resultante)
    except (TypeError, ValueError):
        return "Error: las fracciones deben ser tuplas de enteros."


def fraccion_a_decimal(frac):
    """
    Convierte una fracción a su representación decimal.

    Args:
        frac (tuple): Fracción como (numerador, denominador).

    Returns:
        float: Valor decimal de la fracción.
    """
    try:
        numerador, denominador = frac
        if denominador == 0:
            return "Error: el denominador no puede ser cero."
        return numerador / denominador
    except (TypeError, ValueError):
        return "Error: la fracción debe ser una tupla de enteros."


def decimal_a_fraccion(decimal):
    """
    Convierte un número decimal a fracción.

    Args:
        decimal (float): Número decimal.

    Returns:
        tuple: Fracción equivalente simplificada.
    """
    try:
        # Convertir el decimal a una fracción
        if not isinstance(decimal, (float, int)):
            return "Error: el valor debe ser numérico."

        denominador = 10 ** len(str(decimal).split(".")[1])
        numerador = int(decimal * denominador)
        
        return simplificar_fraccion(numerador, denominador)
    except (TypeError, ValueError):
        return "Error: el valor debe ser numérico."


def fraccion_inversa(frac):
    """
    Calcula la fracción inversa (recíproca).

    Args:
        frac (tuple): Fracción como (numerador, denominador).

    Returns:
        tuple: Fracción recíproca.
    """
    try:
        numerador, denominador = frac
        if numerador == 0:
            return "Error: no se puede calcular la inversa de una fracción con numerador cero."
        return simplificar_fraccion(denominador, numerador)
    except (TypeError, ValueError):
        return "Error: la fracción debe ser una tupla de enteros."
