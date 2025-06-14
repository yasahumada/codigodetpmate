 for i, dni in enumerate(dnis):
        pares = sum(1 for d in dni if int(d) % 2 == 0)
        impares = sum(1 for d in dni if int(d) % 2 != 0)
        print(f"DNI #{i+1} ({dni}): {pares} pares, {impares} impares")
        if pares > impares:
            print("Predominan los pares.")
        elif impares > pares:
            print("Predominan los impares.")
        else:
            print("Cantidad igual de pares e impares.")
        if pares == len(dni):
            pares_global = True
        if impares == len(dni):
            impares_global = True
    if pares_global:
        print("Existe al menos un DNI compuesto solo por dígitos pares.")
    if impares_global:
        print("Existe al menos un DNI compuesto solo por dígitos impares.")

# Determina si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


# ----------------------------- PROGRAMA PRINCIPAL -----------------------------

# ----- Ingreso de datos -----
dnis = ingresar_dnis()
conjuntos = [obtener_conjunto_digitos(dni) for dni in dnis]

# ----- Operaciones con conjuntos -----
print("\n--- Operaciones con Conjuntos de Dígitos ---")
union, interseccion, diferencias, diferencia_simetrica = operaciones_conjuntos(conjuntos)

print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
for idx, diff in enumerate(diferencias, start=1):
    print(f"Diferencia del DNI #1 con el DNI #{idx+1}: {diff}")
print(f"Diferencia simétrica: {diferencia_simetrica}")

# ----- Frecuencia de dígitos -----
print("\n--- Frecuencia de Dígitos por DNI ---")
for idx, dni in enumerate(dnis):
    frec = contar_frecuencias(dni)
    print(f"DNI #{idx+1} ({dni}): {frec}")

# ----- Suma de dígitos -----
print("\n--- Suma de Dígitos por DNI ---")
for idx, dni in enumerate(dnis):
    suma = suma_digitos(dni)
    print(f"DNI #{idx+1} ({dni}): Suma = {suma}")

# ----- Evaluación de condiciones -----
print("\n--- Evaluación de Condiciones Lógicas ---")
evaluar_condiciones(conjuntos)

# ----- Análisis de paridad -----
print("\n--- Análisis de Paridad de Dígitos por DNI ---")
analizar_paridad(dnis)

# ----- Análisis de años de nacimiento -----
anios_nacimiento = [1999, 2002, 2004] # Podés cambiar estos años
anios_pares = 0
anios_impares = 0
algun_bisiesto = False

for anio in anios_nacimiento:
    if anio % 2 == 0:
        anios_pares += 1
    else:
        anios_impares += 1
    if es_bisiesto(anio):
        algun_bisiesto = True

print("\n--- Operaciones con Años de Nacimiento ---")
print("Años ingresados:", anios_nacimiento)
print("Cantidad de años pares:", anios_pares)
print("Cantidad de años impares:", anios_impares)

if all(anio > 2000 for anio in anios_nacimiento):
    print("Grupo Z")
if algun_bisiesto:
    print("Tenemos un año especial")

# ----- Producto cartesiano año - edad -----
anio_actual = datetime.now().year
edades = [anio_actual - anio for anio in anios_nacimiento]
producto_cartesiano = list(product(anios_nacimiento, edades))

print("\nProducto cartesiano (Año, Edad):")
for par in producto_cartesiano:
    print(par