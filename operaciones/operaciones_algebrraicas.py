# Módulo: operaciones_algebraicas.py
# Autor: Ángel Alcántar
# Descripción: Módulo que contiene funciones para realizar operaciones algebraicas básicas.
import math

def sumar_polinomios(polinomio1, polinomio2):
    """
    Suma dos polinomios de igual o diferente grado.
    
    Args:
        polinomio1 (list): Coeficientes del primer polinomio.
        polinomio2 (list): Coeficientes del segundo polinomio.
        
    Returns:
        list: Coeficientes del polinomio resultante de la suma.
    """
    try:
        # Alinear polinomios de diferente grado
        if len(polinomio1) > len(polinomio2):
            polinomio2 = [0] * (len(polinomio1) - len(polinomio2)) + polinomio2
        else:
            polinomio1 = [0] * (len(polinomio2) - len(polinomio1)) + polinomio1
        
        return [a + b for a, b in zip(polinomio1, polinomio2)]
    except TypeError:
        return "Error: los coeficientes deben ser numéricos."


def restar_polinomios(polinomio1, polinomio2):
    """
    Resta dos polinomios de igual o diferente grado.
    
    Args:
        polinomio1 (list): Coeficientes del primer polinomio.
        polinomio2 (list): Coeficientes del segundo polinomio.
        
    Returns:
        list: Coeficientes del polinomio resultante de la resta.
    """
    try:
        # Alinear polinomios de diferente grado
        if len(polinomio1) > len(polinomio2):
            polinomio2 = [0] * (len(polinomio1) - len(polinomio2)) + polinomio2
        else:
            polinomio1 = [0] * (len(polinomio2) - len(polinomio1)) + polinomio1
        
        return [a - b for a, b in zip(polinomio1, polinomio2)]
    except TypeError:
        return "Error: los coeficientes deben ser numéricos."


def multiplicar_polinomios(polinomio1, polinomio2):
    """
    Multiplica dos polinomios.
    
    Args:
        polinomio1 (list): Coeficientes del primer polinomio.
        polinomio2 (list): Coeficientes del segundo polinomio.
        
    Returns:
        list: Coeficientes del polinomio resultante de la multiplicación.
    """
    try:
        resultado = [0] * (len(polinomio1) + len(polinomio2) - 1)
        for i in range(len(polinomio1)):
            for j in range(len(polinomio2)):
                resultado[i + j] += polinomio1[i] * polinomio2[j]
        return resultado
    except TypeError:
        return "Error: los coeficientes deben ser numéricos."


def derivada_polinomio(polinomio):
    """
    Calcula la derivada de un polinomio.
    
    Args:
        polinomio (list): Coeficientes del polinomio.
        
    Returns:
        list: Coeficientes del polinomio derivado.
    """
    try:
        return [coef * i for i, coef in enumerate(polinomio)][1:]
    except TypeError:
        return "Error: los coeficientes deben ser numéricos."


def evaluar_polinomio(polinomio, x):
    """
    Evalúa un polinomio en un valor específico de x.
    
    Args:
        polinomio (list): Coeficientes del polinomio.
        x (float): Valor de la variable x.
        
    Returns:
        float: Resultado de evaluar el polinomio en x.
    """
    try:
        return sum(coef * (x ** i) for i, coef en enumerate(polinomio))
    except TypeError:
        return "Error: los coeficientes y el valor de x deben ser numéricos."


def resolver_ecuacion_cuadratica(a, b, c):
    """
    Resuelve una ecuación cuadrática de la forma ax^2 + bx + c = 0.
    
    Args:
        a (float): Coeficiente del término cuadrático.
        b (float): Coeficiente del término lineal.
        c (float): Término independiente.
        
    Returns:
        tuple: Las dos soluciones de la ecuación cuadrática, o un mensaje de error si no tiene soluciones reales.
    """
    try:
        discriminante = b ** 2 - 4 * a * c
        if discriminante < 0:
            return "Error: no hay soluciones reales."
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return (x1, x2)
    except TypeError:
        return "Error: los coeficientes deben ser numéricos."
    except ZeroDivisionError:
        return "Error: el coeficiente a no puede ser cero."


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
