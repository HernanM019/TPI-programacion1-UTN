"""

TPI - Programación 1 - UTN
Alumnos:
Moises, Hernan Martin
Rey, Facundo Tobias

GRUPO 170.

"""

import csv
import os

CSV_PATH = "paises.csv"

# ------------------------ Utilidades de validación ------------------------- #

def str_no_vacio(s):
    return isinstance(s, str) and s.strip() != ""

def leer_entero(mensaje, minimo=None, maximo=None):
    """
    Pide un número entero, validando rango opcional.
    """
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit():
            valor = int(dato)
            if minimo is not None and valor < minimo:
                print("ERROR. Debe ser mayor o igual a", minimo)
                continue
            if maximo is not None and valor > maximo:
                print("ERROR. Debe ser menor o igual a", maximo)
                continue
            return valor
        else:
            print("ERROR. Ingrese un número entero válido.")

def leer_texto(mensaje):
    """
    Pide texto no vacío.
    """
    while True:
        dato = input(mensaje).strip()
        if str_no_vacio(dato):
            return dato
        print("ERROR. Este campo no puede estar vacío.")

# ------------------------ Manejo de archivos CSV --------------------------- #

def cargar_csv(ruta=CSV_PATH):
    """
    Carga el archivo CSV si existe. Devuelve lista de diccionarios.
    No usa excepciones.
    """
    paises = []
    if not os.path.exists(ruta):
        return paises

    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre = fila["nombre"].strip()
            poblacion_texto = fila["poblacion"].strip()
            superficie_texto = fila["superficie"].strip()
            continente = fila["continente"].strip()

            if poblacion_texto.isdigit() and superficie_texto.isdigit():
                poblacion = int(poblacion_texto)
                superficie = int(superficie_texto)
                if str_no_vacio(nombre) and str_no_vacio(continente):
                    paises.append({
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    })
    return paises

def guardar_csv(paises, ruta=CSV_PATH):
    """
    Guarda la lista de países en un archivo CSV.
    """
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)

# ------------------------ Funciones de dominio ----------------------------- #

def normalizar_texto(s):
    return s.strip().lower()

def buscar_indices_por_nombre(paises, patron):
    """
    Busca índices de países que contienen el patrón en el nombre.
    """
    patron = normalizar_texto(patron)
    indices = []
    for i in range(len(paises)):
        nombre = normalizar_texto(paises[i]["nombre"])
        if patron in nombre:
            indices.append(i)
    return indices

def agregar_pais(paises):
    print("\n➕ Agregar país")
    nombre = leer_texto("Nombre: ")

    # Evita duplicados
    existe = False
    for p in paises:
        if normalizar_texto(p["nombre"]) == normalizar_texto(nombre):
            existe = True
    if existe:
        print("AVISO: Ese país ya existe.")
        return

    poblacion = leer_entero("Población (entero >= 0): ", minimo=0)
    superficie = leer_entero("Superficie km² (entero >= 0): ", minimo=0)
    continente = leer_texto("Continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    guardar_csv(paises)
    print("AVISO: País agregado correctamente.")

def actualizar_pais(paises):
    print("\n Actualizar país")
    if len(paises) == 0:
        print("ERROR. No hay países cargados.")
        return

    patron = leer_texto("Buscar país por nombre: ")
    indices = buscar_indices_por_nombre(paises, patron)

    if len(indices) == 0:
        print("AVISO: No se encontraron coincidencias.")
        return

    for i in range(len(indices)):
        pos = indices[i]
        p = paises[pos]
        print(i + 1, ")", p["nombre"], "-", p["poblacion"], "habitantes,", p["superficie"], "km²")

    seleccion = leer_entero("Seleccione número de país: ", minimo=1, maximo=len(indices))
    indice = indices[seleccion - 1]

    nueva_poblacion = leer_entero("Nueva población: ", minimo=0)
    nueva_superficie = leer_entero("Nueva superficie km²: ", minimo=0)

    paises[indice]["poblacion"] = nueva_poblacion
    paises[indice]["superficie"] = nueva_superficie

    guardar_csv(paises)
    print("AVISO: Datos actualizados.")

def buscar_pais(paises):
    print("\n Buscar país")
    patron = leer_texto("Nombre o parte del nombre: ")
    indices = buscar_indices_por_nombre(paises, patron)

    if len(indices) == 0:
        print("Sin resultados.")
        return

    for i in range(len(indices)):
        p = paises[indices[i]]
        print("- ", p["nombre"], "| Población:", p["poblacion"], "| Superficie:", p["superficie"], "|", p["continente"])

def filtrar_por_continente(paises):
    print("\n Filtrar por continente")
    cont = leer_texto("Ingrese continente: ")
    resultados = []
    for p in paises:
        if normalizar_texto(p["continente"]) == normalizar_texto(cont):
            resultados.append(p)
    mostrar_lista(resultados)

def filtrar_rango(paises, clave):
    print("\nFiltrar por rango de", clave)
    minimo = leer_entero("Valor mínimo: ", minimo=0)
    maximo = leer_entero("Valor máximo: ", minimo=minimo)
    resultados = []
    for p in paises:
        valor = p[clave]
        if valor >= minimo and valor <= maximo:
            resultados.append(p)
    mostrar_lista(resultados)

def ordenar_paises(paises):
    print("\nOrdenar países")
    print("1) Nombre (A-Z)")
    print("2) Población (asc/desc)")
    print("3) Superficie (asc/desc)")
    op = leer_entero("Opción: ", minimo=1, maximo=3)

    if op == 1:
        # Orden por nombre (burbuja)
        for i in range(len(paises) - 1):
            for j in range(len(paises) - 1 - i):
                if normalizar_texto(paises[j]["nombre"]) > normalizar_texto(paises[j + 1]["nombre"]):
                    paises[j], paises[j + 1] = paises[j + 1], paises[j]
    elif op == 2:
        sentido = leer_entero("1) Ascendente  2) Descendente: ", minimo=1, maximo=2)
        for i in range(len(paises) - 1):
            for j in range(len(paises) - 1 - i):
                if sentido == 1:
                    if paises[j]["poblacion"] > paises[j + 1]["poblacion"]:
                        paises[j], paises[j + 1] = paises[j + 1], paises[j]
                else:
                    if paises[j]["poblacion"] < paises[j + 1]["poblacion"]:
                        paises[j], paises[j + 1] = paises[j + 1], paises[j]
    elif op == 3:
        sentido = leer_entero("1) Ascendente  2) Descendente: ", minimo=1, maximo=2)
        for i in range(len(paises) - 1):
            for j in range(len(paises) - 1 - i):
                if sentido == 1:
                    if paises[j]["superficie"] > paises[j + 1]["superficie"]:
                        paises[j], paises[j + 1] = paises[j + 1], paises[j]
                else:
                    if paises[j]["superficie"] < paises[j + 1]["superficie"]:
                        paises[j], paises[j + 1] = paises[j + 1], paises[j]

    mostrar_lista(paises)

def estadisticas(paises):
    print("\nEstadísticas")
    if len(paises) == 0:
        print("AVISO: No hay datos disponibles.")
        return

    mayor_poblacion = paises[0]
    menor_poblacion = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    total = len(paises)

    # Cálculos principales
    for p in paises:
        if p["poblacion"] > mayor_poblacion["poblacion"]:
            mayor_poblacion = p
        if p["poblacion"] < menor_poblacion["poblacion"]:
            menor_poblacion = p
        suma_poblacion += p["poblacion"]
        suma_superficie += p["superficie"]

    promedio_poblacion = suma_poblacion / total
    promedio_superficie = suma_superficie / total

    # Conteo por continente
    conteo = {}
    for p in paises:
        cont = p["continente"]
        if cont in conteo:
            conteo[cont] += 1
        else:
            conteo[cont] = 1

    print("País con mayor población:", mayor_poblacion["nombre"], "(", mayor_poblacion["poblacion"], ")")
    print("País con menor población:", menor_poblacion["nombre"], "(", menor_poblacion["poblacion"], ")")
    print("Promedio de población:", round(promedio_poblacion, 2))
    print("Promedio de superficie:", round(promedio_superficie, 2))
    print("Cantidad por continente:")
    for c in conteo:
        print(" -", c, ":", conteo[c])

def mostrar_lista(lista):
    if len(lista) == 0:
        print("⚠ No hay resultados.")
    else:
        for p in lista:
            print("- ", p["nombre"], "| Población:", p["poblacion"], "| Superficie:", p["superficie"], "|", p["continente"])

def asegurar_csv_base(ruta=CSV_PATH):
    if os.path.exists(ruta):
        return
    datos = [
        {"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400, "continente": "América"},
        {"nombre": "Japón", "poblacion": 125800000, "superficie": 377975, "continente": "Asia"},
        {"nombre": "Brasil", "poblacion": 213993437, "superficie": 8515767, "continente": "América"},
        {"nombre": "Alemania", "poblacion": 83149300, "superficie": 357022, "continente": "Europa"}
    ]
    guardar_csv(datos)

# ------------------------ Menú principal ---------------------- #

def menu():
    asegurar_csv_base()
    paises = cargar_csv()

    while True:
        print("\n===== Gestión de Países =====")
        print("1) Agregar país")
        print("2) Actualizar país")
        print("3) Buscar país")
        print("4) Filtrar por continente")
        print("5) Filtrar por rango de población")
        print("6) Filtrar por rango de superficie")
        print("7) Ordenar países")
        print("8) Ver estadísticas")
        print("9) Mostrar todos")
        print("0) Salir")

        opcion = leer_entero("Opción: ", minimo=0, maximo=9)

        match opcion:
            case 0:
                print("Fin del programa.")
                break
            case 1:
                agregar_pais(paises)
                paises = cargar_csv()
            case 2:
                actualizar_pais(paises)
                paises = cargar_csv()
            case 3:
                buscar_pais(paises)
            case 4:
                filtrar_por_continente(paises)
            case 5:
                filtrar_rango(paises, "poblacion")
            case 6:
                filtrar_rango(paises, "superficie")
            case 7:
                ordenar_paises(paises)
            case 8:
                estadisticas(paises)
            case 9:
                mostrar_lista(paises)
            case _:
                print("ERROR. Opción inválida.")

if __name__ == "__main__":
    menu()
