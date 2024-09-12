import math

# Operaciones con logaritmos
def logaritmo_base_n(numero, base):
    if numero <= 0 or base <= 0:
        return "Error: el número y la base deben ser mayores a cero."
    return math.log(numero, base)

def logaritmo_natural(numero):
    if numero <= 0:
        return "Error: el número debe ser mayor a cero."
    return math.log(numero)

def logaritmo_base_10(numero):
    if numero <= 0:
        return "Error: el número debe ser mayor a cero."
    return math.log10(numero)

# Raíces y potencias
def raiz_n(numero, n):
    if n == 0:
        return "Error: no se puede calcular la raíz con índice cero."
    if numero < 0 and n % 2 == 0:
        return "Error: no se puede calcular la raíz de un número negativo si el índice es par."
    return numero ** (1 / n)

def potencia(base, exponente):
    return base ** exponente

# Conversión entre grados y radianes
def radianes_a_grados(radianes):
    return math.degrees(radianes)

def grados_a_radianes(grados):
    return math.radians(grados)

# Funciones trigonométricas
def seno(angulo_radianes):
    return math.sin(angulo_radianes)

def coseno(angulo_radianes):
    return math.cos(angulo_radianes)

def tangente(angulo_radianes):
    return math.tan(angulo_radianes)

def secante(angulo_radianes):
    if math.cos(angulo_radianes) == 0:
        return "Error: Secante indefinida para este ángulo."
    return 1 / math.cos(angulo_radianes)

def cosecante(angulo_radianes):
    if math.sin(angulo_radianes) == 0:
        return "Error: Cosecante indefinida para este ángulo."
    return 1 / math.sin(angulo_radianes)

def cotangente(angulo_radianes):
    if math.tan(angulo_radianes) == 0:
        return "Error: Cotangente indefinida para este ángulo."
    return 1 / math.tan(angulo_radianes)

# Funciones trigonométricas inversas
def arco_seno(valor):
    if valor < -1 or valor > 1:
        return "Error: El valor debe estar entre -1 y 1."
    return math.asin(valor)

def arco_coseno(valor):
    if valor < -1 or valor > 1:
        return "Error: El valor debe estar entre -1 y 1."
    return math.acos(valor)

def arco_tangente(valor):
    return math.atan(valor)

# Funciones hiperbólicas
def seno_hiperbolico(angulo_radianes):
    return math.sinh(angulo_radianes)

def coseno_hiperbolico(angulo_radianes):
    return math.cosh(angulo_radianes)

def tangente_hiperbolica(angulo_radianes):
    return math.tanh(angulo_radianes)

# Funciones estadísticas
def media(valores):
    if len(valores) == 0:
        return "Error: Se requiere al menos un valor."
    return sum(valores) / len(valores)

def varianza(valores):
    if len(valores) < 2:
        return "Error: Se requieren al menos dos valores."
    promedio = media(valores)
    return sum((x - promedio) ** 2 for x in valores) / len(valores)

def desviacion_estandar(valores):
    return math.sqrt(varianza(valores))

# Notación científica
def notacion_cientifica(numero):
    return "{:e}".format(numero)

# Operaciones factoriales y combinatorias
def factorial(n):
    if n < 0:
        return "Error: El número debe ser no negativo."
    return math.factorial(n)

def combinacion(n, r):
    if n < 0 or r < 0 or r > n:
        return "Error: Los valores no son válidos."
    return math.comb(n, r)

def permutacion(n, r):
    if n < 0 or r < 0 or r > n:
        return "Error: Los valores no son válidos."
    return math.perm(n, r)
