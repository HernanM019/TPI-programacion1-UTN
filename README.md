# 📘 Trabajo Práctico Integrador — Programación 1  
**Universidad Tecnológica Nacional (UTN) — Grupo 170**

---

## 🧩 Descripción del programa

El presente proyecto consiste en un sistema de **gestión de países** desarrollado en lenguaje **Python**, que permite **leer, registrar, actualizar y analizar información** sobre distintos países utilizando **estructuras de datos básicas** (listas y diccionarios) y archivos **CSV** para la persistencia de datos.

El programa opera mediante una **interfaz de menú en consola**, implementada con estructuras **repetitivas (`while`)** y **condicionales (`match/case`)**.  
Se diseñó respetando los lineamientos del **Trabajo Práctico Integrador de Programación 1**, evitando el uso de clases, funciones lambda o manejo de excepciones, en conformidad con las restricciones de la materia.

---

## ⚙️ Funcionalidades principales

El menú principal ofrece las siguientes opciones:

| Nº | Funcionalidad | Descripción breve |
|----|----------------|-------------------|
| 1 | **Agregar país** | Permite ingresar un nuevo país con nombre, población, superficie y continente. |
| 2 | **Actualizar país** | Modifica los datos de población y superficie de un país existente. |
| 3 | **Buscar país** | Busca por nombre o coincidencia parcial y muestra la información del país. |
| 4 | **Filtrar por continente** | Muestra los países pertenecientes a un continente específico. |
| 5 | **Filtrar por rango de población** | Lista países cuya población se encuentra entre dos valores ingresados. |
| 6 | **Filtrar por rango de superficie** | Lista países según el rango de superficie indicado por el usuario. |
| 7 | **Ordenar países** | Ordena por nombre, población o superficie (ascendente o descendente) utilizando algoritmo de burbuja. |
| 8 | **Ver estadísticas** | Calcula y muestra: país más y menos poblado, promedios y cantidad de países por continente. |
| 9 | **Mostrar todos** | Presenta todo el contenido actual del archivo CSV. |
| 0 | **Salir** | Finaliza la ejecución del programa. |

---

## ▶️ Instrucciones de uso

### 1. Requisitos previos
- **Python 3.10 o superior.**
- No requiere librerías externas: usa únicamente el módulo estándar `csv` y `os`.

### 2. Ejecución
Guarde el archivo principal con el nombre `tpi_g170.py` o cualquier nombre válido, y ejecute desde la terminal o el entorno
de desarrollo.

```bash
python tpi_g170.py
```
### 3. Archivo de datos
Si no existe `paises.csv`, el programa generará automáticamente uno con los siguientes datos iniciales:

| Nombre    | Población   | Superficie | Continente |
| --------- | ----------- | ---------- | ---------- |
| Argentina | 45.376.763  | 2.780.400  | América    |
| Japón     | 125.800.000 | 377.975    | Asia       |
| Brasil    | 213.993.437 | 8.515.767  | América    |
| Alemania  | 83.149.300  | 357.022    | Europa     |

## Ejemplos de uso
### Agregar Pais
Entrada:

````
1 

Nombre: Canadá

Población (entero >= 0): 38900000

Superficie km² (entero >= 0): 9984670

Continente: América
````
Salida:
``AVISO: País agregado correctamente.``

### Buscar Pais
Entrada:

````
3

Nombre o parte del nombre: alemania
````
Salida: ``-  Alemania | Población: 83149300 | Superficie: 357022 | Europa``

### Ver estadísticas
Entrada: ``8``

Salida: 

````
País con mayor población: Brasil (213993437)
País con menor población: Argentina (45376763)
Promedio de población: 119579875.0
Promedio de superficie: 4005531.0
Cantidad por continente:
 - América : 2
 - Asia : 1
 - Europa : 1
````

## Integrantes - Grupo 170
### Moises, Hernan Martin
### Rey, Facundo Tobias
