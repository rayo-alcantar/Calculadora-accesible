# Módulo: operaciones_basicas.py
# Autor: Ángel Alcántar
# Descripción: Módulo que contiene funciones para realizar las operaciones matemáticas básicas.

def suma(*args):
    """
    Realiza la suma de dos o más números.
    
    Args:
        *args (float): Números a sumar.
        
    Returns:
        float: El resultado de sumar todos los valores.
    """
    try:
        if len(args) < 2:
            return "Error: Se requieren al menos dos números."
        return sum(args)
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def resta(a, b, *args):
    """
    Realiza la resta de dos o más números.
    
    Args:
        a (float): Minuendo.
        b (float): Sustraendo.
        *args (float): Opcional, valores adicionales a restar.
        
    Returns:
        float: El resultado de restar todos los valores en orden.
    """
    try:
        resultado = a - b
        for valor in args:
            resultado -= valor
        return resultado
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def multiplicacion(*args):
    """
    Realiza la multiplicación de dos o más números.
    
    Args:
        *args (float): Números a multiplicar.
        
    Returns:
        float: El resultado de multiplicar todos los valores.
    """
    try:
        if len(args) < 2:
            return "Error: Se requieren al menos dos números."
        resultado = 1
        for valor in args:
            resultado *= valor
        return resultado
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def division(a, b, *args):
    """
    Realiza la división de dos o más números.
    
    Args:
        a (float): Dividendo.
        b (float): Divisor.
        *args (float): Opcional, valores adicionales a dividir en orden.
        
    Returns:
        float: El resultado de dividir todos los valores en orden. Si algún divisor es 0, retorna un error.
    """
    try:
        if b == 0 or any(valor == 0 for valor in args):
            return "Error: división por cero no permitida."
        resultado = a / b
        for valor in args:
            resultado /= valor
        return resultado
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def residuo(a, b, *args):
    """
    Calcula el residuo de la división de dos o más números (operación módulo).
    
    Args:
        a (float): Dividendo.
        b (float): Divisor.
        *args (float): Opcional, valores adicionales para calcular el residuo en orden.
        
    Returns:
        float: El residuo de dividir todos los valores en orden.
    """
    try:
        if b == 0 or any(valor == 0 for valor in args):
            return "Error: división por cero no permitida."
        resultado = a % b
        for valor in args:
            resultado %= valor
        return resultado
    except TypeError:
        return "Error: todos los valores deben ser numéricos."


def exponente(base, exponente, *args):
    """
    Calcula la potencia de uno o más números.
    
    Args:
        base (float): Base de la potencia.
        exponente (float): Exponente inicial.
        *args (float): Opcional, exponentes adicionales para calcular en orden.
        
    Returns:
        float: El resultado de elevar base a la potencia exponente y luego aplicar las potencias adicionales en orden.
    """
    try:
        resultado = base ** exponente
        for valor in args:
            resultado **= valor
        return resultado
    except TypeError:
        return "Error: todos los valores deben ser numéricos."

def porcentaje_total(parte, total):
    """
    Calcula el porcentaje que representa una parte de un total.
    
    Args:
        parte (float): El valor de la parte.
        total (float): El valor total.
        
    Returns:
        float: El porcentaje que representa la parte sobre el total.
    """
    try:
        if total == 0:
            return "Error: el total no puede ser cero."
        return (parte / total) * 100
    except TypeError:
        return "Error: los valores deben ser numéricos."


def porcentaje_aplicado(valor, porcentaje):
    """
    Calcula el valor de un porcentaje aplicado a un valor específico.
    
    Args:
        valor (float): El valor base.
        porcentaje (float): El porcentaje a aplicar.
        
    Returns:
        float: El resultado del porcentaje aplicado al valor.
    """
    try:
        return (valor * porcentaje) / 100
    except TypeError:
        return "Error: los valores deben ser numéricos."
