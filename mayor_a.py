import sys

# Diccionario de balances del año pasado
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

# Leer el umbral desde los argumentos de la línea de comandos.
umbral = int(sys.argv[1])

# Diccionario para almacenar los meses que superan el umbral requerido.
ventas_superiores = {}

# Diccionario de ventas
for mes, venta in ventas.items():
    # Si la venta es mayor al umbral requerido por el usuario, agregar al diccionario de ventas superiores a este.
    if venta > umbral:
        ventas_superiores[mes] = venta

# Resultado del umbral requerido 
print(ventas_superiores)
