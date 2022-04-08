Tarea 5 - Algoritmos de Compresión

Integrante                    | Login
----------------------------------------------
Juan Pablo Correa Puerta      | jp.correap
Juan Pablo Sarmiento Sanabria | jp.sarmientos
Sergio David Sierra Sanmiguel | sd.sierra


Para ejecutar los programas, abra una línea de comandos en esta carpeta y ejecute los siguientes comandos,
recuerde reemplazar los valores entre los símbolos <>, sin incluirlos:

Todos los valores de entrada deben ser strings e ingresados en el correcto orden.

Para Shannon-Fano:
python shannon.py <archivoEntrada.txt> <archivoSalida.txt>

Para Huffman:
python huffman.py <archivoEntrada.txt> <archivoSalida.txt>

Para Java:
Primero, compilar con:
javac RSA.java`

Después, ejecutar con:
java RSA <minValue> <maxValue> <mensaje (numero)>


Resultados obtenidos:
+------+------+---------+----------------+------------------+
| min  | max  | message | time Java (ms) | time Python (ms) |
+------+------+---------+----------------+------------------+
| 16   | 24   | 123     | 38.00          | 2.00             |
+------+------+---------+----------------+------------------+
| 200  | 500  | 123     | 192.00         | 47.99            |
+------+------+---------+----------------+------------------+
| 1000 | 2000 | 123     | 11494.00       | 17694.05         |
+------+------+---------+----------------+------------------+
| 2000 | 3500 | 123456  | 6095.00        | 12715.44         |
+------+------+---------+----------------+------------------+