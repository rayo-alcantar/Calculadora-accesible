# Módulo: operaciones_trigonometricas.py
# Autor: Ángel Alcántar
# Descripción: Módulo que contiene funciones para realizar operaciones trigonométricas básicas y avanzadas.

import math

def seno(*args):
    """
    Calcula el seno de uno o más ángulos en radianes.
    
    Args:
        *args (float): Ángulos en radianes a los que se les calculará el seno.
        
    Returns:
        list: Lista con los resultados del seno de cada ángulo.
    """
    try:
        if len(args) == 0:
            return "Error: Se requiere al menos un ángulo."
        return [math.sin(valor) for valor in args]
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def coseno(*args):
    """
    Calcula el coseno de uno o más ángulos en radianes.
    
    Args:
        *args (float): Ángulos en radianes a los que se les calculará el coseno.
        
    Returns:
        list: Lista con los resultados del coseno de cada ángulo.
    """
    try:
        if len(args) == 0:
            return "Error: Se requiere al menos un ángulo."
        return [math.cos(valor) for valor in args]
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def tangente(*args):
    """
    Calcula la tangente de uno o más ángulos en radianes.
    
    Args:
        *args (float): Ángulos en radianes a los que se les calculará la tangente.
        
    Returns:
        list: Lista con los resultados de la tangente de cada ángulo.
    """
    try:
        if len(args) == 0:
            return "Error: Se requiere al menos un ángulo."
        return [math.tan(valor) for valor in args]
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def arco_seno(*args):
    """
    Calcula el arco seno (inverso del seno) de uno o más valores.
    
    Args:
        *args (float): Valores a los que se les calculará el arco seno.
        
    Returns:
        list: Lista con los resultados del arco seno de cada valor.
    """
    try:
        if len(args) == 0:
            return "Error: Se requiere al menos un valor."
        return [math.asin(valor) if -1 <= valor <= 1 else "Error: el valor debe estar entre -1 y 1." for valor in args]
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def arco_coseno(*args):
    """
    Calcula el arco coseno (inverso del coseno) de uno o más valores.
    
    Args:
        *args (float): Valores a los que se les calculará el arco coseno.
        
    Returns:
        list: Lista con los resultados del arco coseno de cada valor.
    """
    try:
        if len(args) == 0:
            return "Error: Se requiere al menos un valor."
        return [math.acos(valor) if -1 <= valor <= 1 else "Error: el valor debe estar entre -1 y 1." for valor in args]
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def arco_tangente(*args):
    """
    Calcula el arco tangente (inverso de la tangente) de uno o más valores.
    
    Args:
        *args (float): Valores a los que se les calculará el arco tangente.
        
    Returns:
        list: Lista con los resultados del arco tangente de cada valor.
    """
    try:
        if len(args) == 0:
            return "Error: Se requiere al menos un valor."
        return [math.atan(valor) for valor in args]
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def secante(*args):
    """
    Calcula la secante de uno o más ángulos en radianes (inverso del coseno).
    
    Args:
        *args (float): Ángulos en radianes a los que se les calculará la secante.
        
    Returns:
        list: Lista con los resultados de la secante de cada ángulo.
    """
    try:
        if len(args) == 0:
            return "Error: Se requiere al menos un ángulo."
        return [1 / math.cos(valor) if math.cos(valor) != 0 else "Error: secante indefinida para este ángulo." for valor in args]
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def cosecante(*args):
    """
    Calcula la cosecante de uno o más ángulos en radianes (inverso del seno).
    
    Args:
        *args (float): Ángulos en radianes a los que se les calculará la cosecante.
        
    Returns:
        list: Lista con los resultados de la cosecante de cada ángulo.
    """
    try:
        if len(args) == 0:
            return "Error: Se requiere al menos un ángulo."
        return [1 / math.sin(valor) if math.sin(valor) != 0 else "Error: cosecante indefinida para este ángulo." for valor in args]
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def cotangente(*args):
    """
    Calcula la cotangente de uno o más ángulos en radianes (inverso de la tangente).
    
    Args:
        *args (float): Ángulos en radianes a los que se les calculará la cotangente.
        
    Returns:
        list: Lista con los resultados de la cotangente de cada ángulo.
    """
    try:
        if len(args) == 0:
            return "Error: Se requiere al menos un ángulo."
        return [1 / math.tan(valor) if math.tan(valor) != 0 else "Error: cotangente indefinida para este ángulo." for valor in args]
    except TypeError:
        return "Error: todos los valores deben ser numéricos."