# -*- coding: utf-8 -*-
"""
Módulo de funciones auxiliares reutilizables

Este módulo contiene funciones útiles que pueden ser importadas
y utilizadas en otros scripts del proyecto.
"""

import math

# ============================================================================
# FUNCIONES MATEMÁTICAS
# ============================================================================

def area_circulo(radio):
    """
    Calcula el área de un círculo.
    
    Args:
        radio (float): Radio del círculo
    
    Returns:
        float: Área del círculo
    """
    return math.pi * radio ** 2

def volumen_esfera(radio):
    """
    Calcula el volumen de una esfera.
    
    Args:
        radio (float): Radio de la esfera
    
    Returns:
        float: Volumen de la esfera
    """
    return (4/3) * math.pi * radio ** 3

def distancia_euclidiana(x1, y1, x2, y2):
    """
    Calcula la distancia euclidiana entre dos puntos.
    
    Args:
        x1, y1 (float): Coordenadas del primer punto
        x2, y2 (float): Coordenadas del segundo punto
    
    Returns:
        float: Distancia entre los puntos
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# ============================================================================
# FUNCIONES ESTADÍSTICAS
# ============================================================================

def promedio(lista):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        lista (list): Lista de números
    
    Returns:
        float: Promedio de los números
    """
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def encontrar_maximo(lista):
    """
    Encuentra el valor máximo en una lista.
    
    Args:
        lista (list): Lista de números
    
    Returns:
        float: Valor máximo
    """
    if len(lista) == 0:
        return None
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

def encontrar_minimo(lista):
    """
    Encuentra el valor mínimo en una lista.
    
    Args:
        lista (list): Lista de números
    
    Returns:
        float: Valor mínimo
    """
    if len(lista) == 0:
        return None
    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo

# ============================================================================
# FUNCIONES DE CONVERSIÓN
# ============================================================================

def celsius_a_fahrenheit(celsius):
    """
    Convierte temperatura de Celsius a Fahrenheit.
    
    Args:
        celsius (float): Temperatura en Celsius
    
    Returns:
        float: Temperatura en Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """
    Convierte temperatura de Fahrenheit a Celsius.
    
    Args:
        fahrenheit (float): Temperatura en Fahrenheit
    
    Returns:
        float: Temperatura en Celsius
    """
    return (fahrenheit - 32) * 5/9

def metros_a_kilometros(metros):
    """
    Convierte metros a kilómetros.
    
    Args:
        metros (float): Distancia en metros
    
    Returns:
        float: Distancia en kilómetros
    """
    return metros / 1000

# ============================================================================
# EJEMPLO DE USO
# ============================================================================

if __name__ == '__main__':
    print('=== PRUEBAS DE FUNCIONES AUXILIARES ===\n')
    
    # Pruebas matemáticas
    print(f'Área de un círculo con radio 5: {area_circulo(5):.2f}')
    print(f'Volumen de una esfera con radio 3: {volumen_esfera(3):.2f}')
    print(f'Distancia entre (0,0) y (3,4): {distancia_euclidiana(0, 0, 3, 4):.2f}\n')
    
    # Pruebas estadísticas
    datos = [5, 10, 15, 20, 25]
    print(f'Lista de datos: {datos}')
    print(f'Promedio: {promedio(datos):.2f}')
    print(f'Máximo: {encontrar_maximo(datos)}')
    print(f'Mínimo: {encontrar_minimo(datos)}\n')
    
    # Pruebas de conversión
    print(f'25°C = {celsius_a_fahrenheit(25):.2f}°F')
    print(f'77°F = {fahrenheit_a_celsius(77):.2f}°C')
    print(f'5000 metros = {metros_a_kilometros(5000):.2f} km')
