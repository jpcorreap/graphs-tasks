# Tarea 6<br />

| Integrante | Login |
| ------ | ------ |
| Juan Pablo Correa Puerta | jp.correap |
| Juan Pablo Sarmiento Sanabria | jp.sarmientos |
| Sergio David Sierra Sanmiguel | sd.sierra |

Implementar en los grupos de trabajo un programa que implemente un arreglo de sufijos para resolver el siguiente problema:

Entradas:

un archivo con un texto que puede estar en varias lineas
un archivo con cadenas a consultar (una cadena por linea).
Salida: Para cada cadena de consulta, el programa debe imprimir una linea con la consulta y, separadas por tabulador, las posiciones en el texto en las que aparece la cadena de consulta. La salida se puede imprimir en salida estandar o en un archivo cuyo nombre debe ser dado por el usuario.

El programa no pueden hacer ninguna suposición acerca del sistema operativo o del sistema de archivos del usuario.

Pasos para solucionar el problema:

1. Construir un arreglo de sufijos
1.1 Leer el texto
1.2 Construir una lista de cadenas con todos los sufijos del texto original
1.3 Ordenar la lista
1.4 Escribir una función que retorne un arreglo de enteros con las posiciones de inicio de los diferentes sufijos.

2. Desarrollar una función que reciba la cadena original, el arreglo de sufijos, y una cadena de consulta y calcule las posiciones en las que se encuentra la cadena de consulta. Implementar búsqueda binaria.

3. El problema principal de esta implementación es que generar la lista de cadenas con todos los sufijos del texto es muy ineficiente en espacio. Modificar la construcción del arreglo de sufijos para generar el arreglo ordenado de posiciones sin tener que calcular explicitamente los sufijos.

Realizar pruebas del archivo con textos de cien mil, un millon y diez millones de caracteres y con mil, diez mil, cien mil y un millon de consultas. Calcular una tabla con los tiempos de ejecución de todos los experimentos.

Entregar un archivo zip con el código fuente del programa, un README que explique la forma en que se debe usar y un archivo de excel con los resultados de los experimentos.