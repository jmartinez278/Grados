'''Algoritmo para la conversion de grados sexagesimales y radiales.'''

import math

# Conversión de grados sexagesimales a radianes
grados = float(input("Introduce el ángulo en grados sexagesimales: "))
radianes = grados * math.pi / 180
print(f"{grados} grados es igual a {radianes:.4f} radianes.")

# Conversión de radianes a grados sexagesimales
radianes = float(input("Introduce el ángulo en radianes: "))
grados = radianes * 180 / math.pi
print(f"{radianes:.4f} radianes es igual a {grados:.4f} grados.")
