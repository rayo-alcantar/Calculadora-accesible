import math

# Cinemática
def velocidad(distancia, tiempo):
    """
    Calcula la velocidad de un objeto dado la distancia recorrida y el tiempo transcurrido.
    
    Args:
        distancia (float): Distancia recorrida en metros.
        tiempo (float): Tiempo transcurrido en segundos.
    
    Returns:
        float: Velocidad en metros por segundo (m/s).
    """
    if tiempo == 0:
        return "Error: El tiempo no puede ser cero."
    return distancia / tiempo

def aceleracion(velocidad_inicial, velocidad_final, tiempo):
    """
    Calcula la aceleración de un objeto dada su velocidad inicial, final y el tiempo.
    
    Args:
        velocidad_inicial (float): Velocidad inicial en m/s.
        velocidad_final (float): Velocidad final en m/s.
        tiempo (float): Tiempo transcurrido en segundos.
    
    Returns:
        float: Aceleración en metros por segundo al cuadrado (m/s²).
    """
    if tiempo == 0:
        return "Error: El tiempo no puede ser cero."
    return (velocidad_final - velocidad_inicial) / tiempo

def movimiento_uniforme_acelerado(velocidad_inicial, tiempo, aceleracion):
    """
    Calcula la distancia recorrida en un movimiento uniformemente acelerado.
    
    Args:
        velocidad_inicial (float): Velocidad inicial en m/s.
        tiempo (float): Tiempo transcurrido en segundos.
        aceleracion (float): Aceleración en m/s².
    
    Returns:
        float: Distancia recorrida en metros.
    """
    return velocidad_inicial * tiempo + 0.5 * aceleracion * tiempo ** 2

# Dinámica
def fuerza(masa, aceleracion):
    """
    Calcula la fuerza aplicada sobre un objeto dada su masa y aceleración (segunda ley de Newton).
    
    Args:
        masa (float): Masa del objeto en kilogramos.
        aceleracion (float): Aceleración en m/s².
    
    Returns:
        float: Fuerza en Newtons (N).
    """
    return masa * aceleracion

def energia_cinetica(masa, velocidad):
    """
    Calcula la energía cinética de un objeto dada su masa y velocidad.
    
    Args:
        masa (float): Masa del objeto en kilogramos.
        velocidad (float): Velocidad en m/s.
    
    Returns:
        float: Energía cinética en Joules (J).
    """
    return 0.5 * masa * velocidad ** 2

def energia_potencial_gravitatoria(masa, altura, gravedad=9.81):
    """
    Calcula la energía potencial gravitatoria de un objeto dada su masa y altura.
    
    Args:
        masa (float): Masa del objeto en kilogramos.
        altura (float): Altura en metros.
        gravedad (float): Aceleración debida a la gravedad, por defecto 9.81 m/s².
    
    Returns:
        float: Energía potencial en Joules (J).
    """
    return masa * gravedad * altura

def trabajo(fuerza, distancia):
    """
    Calcula el trabajo realizado por una fuerza dada su magnitud y la distancia sobre la que actúa.
    
    Args:
        fuerza (float): Fuerza en Newtons (N).
        distancia (float): Distancia en metros.
    
    Returns:
        float: Trabajo en Joules (J).
    """
    return fuerza * distancia

# Leyes de la termodinámica
def calor(masa, calor_especifico, cambio_temperatura):
    """
    Calcula el calor transferido a un objeto dado su masa, calor específico y el cambio de temperatura.
    
    Args:
        masa (float): Masa del objeto en kilogramos.
        calor_especifico (float): Calor específico en J/(kg°C).
        cambio_temperatura (float): Cambio de temperatura en °C.
    
    Returns:
        float: Calor en Joules (J).
    """
    return masa * calor_especifico * cambio_temperatura

# Electromagnetismo
def ley_ohm(voltaje, resistencia):
    """
    Calcula la corriente eléctrica usando la Ley de Ohm.
    
    Args:
        voltaje (float): Voltaje en Voltios (V).
        resistencia (float): Resistencia en Ohms (Ω).
    
    Returns:
        float: Corriente en Amperios (A).
    """
    if resistencia == 0:
        return "Error: La resistencia no puede ser cero."
    return voltaje / resistencia

def potencia_electrica(voltaje, corriente):
    """
    Calcula la potencia eléctrica dada el voltaje y la corriente.
    
    Args:
        voltaje (float): Voltaje en Voltios (V).
        corriente (float): Corriente en Amperios (A).
    
    Returns:
        float: Potencia en Vatios (W).
    """
    return voltaje * corriente

# Óptica
def indice_refraccion(velocidad_luz, velocidad_medio):
    """
    Calcula el índice de refracción de un material.
    
    Args:
        velocidad_luz (float): Velocidad de la luz en el vacío en m/s.
        velocidad_medio (float): Velocidad de la luz en el medio en m/s.
    
    Returns:
        float: Índice de refracción.
    """
    if velocidad_medio == 0:
        return "Error: La velocidad en el medio no puede ser cero."
    return velocidad_luz / velocidad_medio

# Gravitación
def fuerza_gravitatoria(masa1, masa2, distancia):
    """
    Calcula la fuerza gravitatoria entre dos masas usando la Ley de la Gravitación Universal.
    
    Args:
        masa1 (float): Masa del primer objeto en kilogramos.
        masa2 (float): Masa del segundo objeto en kilogramos.
        distancia (float): Distancia entre los dos objetos en metros.
    
    Returns:
        float: Fuerza gravitatoria en Newtons (N).
    """
    G = 6.67430e-11  # Constante gravitatoria en m^3 kg^-1 s^-2
    if distancia == 0:
        return "Error: La distancia no puede ser cero."
    return G * (masa1 * masa2) / distancia ** 2
