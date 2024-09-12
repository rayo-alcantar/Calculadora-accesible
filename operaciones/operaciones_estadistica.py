import math
from collections import Counter

def media(valores):
    """
    Calcula la media aritmética de una lista de valores.
    
    Args:
        valores (list): Lista de números.
    
    Returns:
        float: Media aritmética.
    """
    if len(valores) == 0:
        return "Error: Se requiere al menos un valor."
    return sum(valores) / len(valores)


def mediana(valores):
    """
    Calcula la mediana de una lista de valores.
    
    Args:
        valores (list): Lista de números.
    
    Returns:
        float: Mediana de los valores.
    """
    if len(valores) == 0:
        return "Error: Se requiere al menos un valor."
    
    valores_ordenados = sorted(valores)
    n = len(valores)
    medio = n // 2
    
    if n % 2 == 0:
        return (valores_ordenados[medio - 1] + valores_ordenados[medio]) / 2
    else:
        return valores_ordenados[medio]


def moda(valores):
    """
    Calcula la moda de una lista de valores.
    
    Args:
        valores (list): Lista de números.
    
    Returns:
        list: Lista con el o los valores que aparecen más frecuentemente.
    """
    if len(valores) == 0:
        return "Error: Se requiere al menos un valor."
    
    contador = Counter(valores)
    max_frecuencia = max(contador.values())
    modas = [clave for clave, frecuencia in contador.items() if frecuencia == max_frecuencia]
    
    return modas


def rango(valores):
    """
    Calcula el rango de una lista de valores.
    
    Args:
        valores (list): Lista de números.
    
    Returns:
        float: Diferencia entre el valor máximo y el mínimo.
    """
    if len(valores) == 0:
        return "Error: Se requiere al menos un valor."
    return max(valores) - min(valores)


def varianza(valores):
    """
    Calcula la varianza de una lista de valores.
    
    Args:
        valores (list): Lista de números.
    
    Returns:
        float: Varianza de los valores.
    """
    if len(valores) < 2:
        return "Error: Se requieren al menos dos valores."
    
    promedio = media(valores)
    return sum((x - promedio) ** 2 for x in valores) / len(valores)


def desviacion_estandar(valores):
    """
    Calcula la desviación estándar de una lista de valores.
    
    Args:
        valores (list): Lista de números.
    
    Returns:
        float: Desviación estándar de los valores.
    """
    return math.sqrt(varianza(valores))


def coeficiente_variacion(valores):
    """
    Calcula el coeficiente de variación de una lista de valores.
    
    Args:
        valores (list): Lista de números.
    
    Returns:
        float: Coeficiente de variación.
    """
    promedio = media(valores)
    if promedio == 0:
        return "Error: La media es cero, no se puede calcular el coeficiente de variación."
    return (desviacion_estandar(valores) / promedio) * 100


def percentil(valores, percentil):
    """
    Calcula el percentil de una lista de valores.
    
    Args:
        valores (list): Lista de números.
        percentil (float): El percentil a calcular (0-100).
    
    Returns:
        float: Valor del percentil.
    """
    if len(valores) == 0:
        return "Error: Se requiere al menos un valor."
    
    if not 0 <= percentil <= 100:
        return "Error: El percentil debe estar entre 0 y 100."
    
    valores_ordenados = sorted(valores)
    k = (len(valores) - 1) * (percentil / 100)
    f = math.floor(k)
    c = math.ceil(k)
    
    if f == c:
        return valores_ordenados[int(k)]
    
    d0 = valores_ordenados[int(f)] * (c - k)
    d1 = valores_ordenados[int(c)] * (k - f)
    
    return d0 + d1


def cuartiles(valores):
    """
    Calcula los cuartiles de una lista de valores.
    
    Args:
        valores (list): Lista de números.
    
    Returns:
        dict: Diccionario con los valores de Q1, Q2 (mediana) y Q3.
    """
    if len(valores) == 0:
        return "Error: Se requiere al menos un valor."
    
    return {
        "Q1": percentil(valores, 25),
        "Q2 (Mediana)": mediana(valores),
        "Q3": percentil(valores, 75)
    }


def resumen_estadistico(valores):
    """
    Proporciona un resumen estadístico básico de una lista de valores.
    
    Args:
        valores (list): Lista de números.
    
    Returns:
        dict: Diccionario con la media, mediana, moda, rango, varianza, desviación estándar y coeficiente de variación.
    """
    if len(valores) == 0:
        return "Error: Se requiere al menos un valor."
    
    return {
        "Media": media(valores),
        "Mediana": mediana(valores),
        "Moda": moda(valores),
        "Rango": rango(valores),
        "Varianza": varianza(valores),
        "Desviación Estándar": desviacion_estandar(valores),
        "Coeficiente de Variación": coeficiente_variacion(valores),
        "Cuartiles": cuartiles(valores)
    }