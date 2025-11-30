# -*- coding: utf-8 -*-
"""
Taller de Python para la Ciencia, Tecnología e Ingeniería
Archivo principal con ejercicios básicos del taller

Autor: Beltran Martinez Jesus Antonio
Fecha: 29/11/25
"""

# ============================================================================
# 1. ENTRADA Y SALIDA DE DATOS
# ============================================================================

def ejercicio_hola_mundo():
    """Ejercicio básico de impresión en pantalla"""
    print('=== EJERCICIO: Hola Mundo ===')
    print('Hola', ' ', 'mundo')
    print()

def ejercicio_variables_basicas():
    """Declaración y uso de variables básicas"""
    print('=== EJERCICIO: Variables Básicas ===')
    nombre = 'Jesus'
    carrera = 'ISC'
    edad = 19
    semestre = '5'
    
    # Diferentes formas de imprimir
    print('Hola', nombre, 'de', carrera, 'es un viejo de', edad, 'años, y va en', semestre, 'semestre')
    print(f'Hola {nombre} de {carrera} es un viejo de {edad} años y va en {semestre} semestre')
    print('Hola ' + nombre + ' de la carrera de ' + carrera)
    print()

def ejercicio_entrada_datos():
    """Captura de datos del usuario con conversión de tipos"""
    print('=== EJERCICIO: Entrada de Datos ===')
    nombre = input('¿Cómo te llamas? ')
    edad = int(input('Edad: '))  # Conversión a entero
    estatura = float(input('Estatura (cm): '))  # Conversión a flotante
    print(f'Hola {nombre} de {edad} años y mides: {estatura} cm')
    print()

# ============================================================================
# 2. OPERACIONES ARITMÉTICAS BÁSICAS
# ============================================================================

def ejercicio_operaciones_basicas():
    """Demostración de todas las operaciones aritméticas"""
    print('=== EJERCICIO: Operaciones Aritméticas ===')
    x = 12
    y = 5
    
    print(f'Valores: x = {x}, y = {y}')
    print(f'Suma (+): {x} + {y} = {x + y}')
    print(f'Resta (-): {x} - {y} = {x - y}')
    print(f'Multiplicación (*): {x} * {y} = {x * y}')
    print(f'División (/): {x} / {y} = {x / y}')
    print(f'División entera (//): {x} // {y} = {x // y}')
    print(f'Módulo (%): {x} % {y} = {x % y}')
    print(f'Potencia (**): {x} ** {y} = {x ** y}')
    print()

def calculadora_simple():
    """Calculadora interactiva con estructuras de control"""
    print('=== EJERCICIO: Calculadora Simple ===')
    x = int(input('Primer valor: '))
    y = int(input('Segundo valor: '))
    
    print('\n¿Qué operación deseas realizar?')
    print('1) Suma')
    print('2) Resta')
    print('3) Multiplicación')
    print('4) División')
    print('5) Módulo')
    
    operacion = int(input('Selecciona (1-5): '))
    
    if operacion == 1:
        print(f'La respuesta es: {x + y}')
    elif operacion == 2:
        print(f'La respuesta es: {x - y}')
    elif operacion == 3:
        print(f'La respuesta es: {x * y}')
    elif operacion == 4:
        if y != 0:
            print(f'La respuesta es: {x / y}')
        else:
            print('Error: No se puede dividir entre cero')
    elif operacion == 5:
        print(f'La respuesta es: {x % y}')
    else:
        print('Operación no válida')
    print()

# ============================================================================
# 3. ESTRUCTURAS DE CONTROL - BUCLES
# ============================================================================

def ejercicio_bucle_for():
    """Ejemplos de bucles for con range"""
    print('=== EJERCICIO: Bucles FOR ===')
    
    print('Números del 0 al 9:')
    for i in range(10):
        print(i, end=' ')
    print('\n')
    
    print('Números del 1 al 10:')
    for i in range(1, 11):
        print(i, end=' ')
    print('\n')
    
    print('Números pares del 2 al 20:')
    for i in range(2, 21, 2):
        print(i, end=' ')
    print('\n\n')

def ejercicio_bucle_while():
    """Ejemplo de bucle while"""
    print('=== EJERCICIO: Bucle WHILE ===')
    cont = 1
    while cont <= 5:
        print(f'El valor es: {cont}')
        cont += 1
    print()

# ============================================================================
# 4. LISTAS Y MANIPULACIÓN DE DATOS
# ============================================================================

def ejercicio_promedio_calificaciones():
    """Cálculo de promedio usando listas"""
    print('=== EJERCICIO: Promedio de Calificaciones ===')
    calif = [4, 6, 9, 7, 5]
    suma = 0
    
    print(f'Calificaciones: {calif}')
    
    for i in range(len(calif)):
        suma = suma + calif[i]
    
    prom = suma / len(calif)
    print(f'El promedio es: {prom:.2f}')
    print()

def ejercicio_lista_dinamica():
    """Creación dinámica de listas con input del usuario"""
    print('=== EJERCICIO: Lista Dinámica ===')
    cant = int(input('¿Cuántos números deseas ingresar? '))
    lista = []
    
    for i in range(cant):
        valor = int(input(f'Valor {i + 1}: '))
        lista.append(valor)
    
    print(f'\nLista creada: {lista}')
    print(f'Suma total: {sum(lista)}')
    print(f'Promedio: {sum(lista) / len(lista):.2f}')
    print()

def ejercicio_pares_impares():
    """Identificación de números pares e impares"""
    print('=== EJERCICIO: Pares e Impares ===')
    lista = [15, 22, 7, 10, 33, 18, 9, 14, 21, 6]
    print(f'Lista original: {lista}')
    
    lista_modificada = []
    
    for numero in lista:
        if numero % 2 == 0:
            print(f'El número {numero} es par')
            lista_modificada.append(numero)
        else:
            print(f'El número {numero} es impar - se convierte a {numero + 1}')
            lista_modificada.append(numero + 1)
    
    print(f'\nLista con impares convertidos a pares: {lista_modificada}')
    print()

# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Función principal que ejecuta todos los ejercicios"""
    print('\n' + '='*60)
    print('TALLER DE PYTHON PARA CIENCIA, TECNOLOGÍA E INGENIERÍA')
    print('='*60 + '\n')
    
    # Ejecutar ejercicios de demostración
    ejercicio_hola_mundo()
    ejercicio_variables_basicas()
    ejercicio_operaciones_basicas()
    ejercicio_bucle_for()
    ejercicio_bucle_while()
    ejercicio_promedio_calificaciones()
    ejercicio_pares_impares()
    
    print('='*60)
    print('EJERCICIOS INTERACTIVOS')
    print('='*60 + '\n')
    
    # Ejercicios interactivos (comentados por defecto)
    # Descomenta para ejecutar:
    # ejercicio_entrada_datos()
    # calculadora_simple()
    # ejercicio_lista_dinamica()

if __name__ == '__main__':
    main()
