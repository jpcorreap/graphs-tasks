        Tarea 7 - Vertex cover
Programa que implementa cuatro algoritmos
para solucionar el problema de cubrimiento de
vertices

----------------------------------------------
                   Equipo #4
----------------------------------------------
Integrante                    | Login
----------------------------------------------
Juan Pablo Correa Puerta      | jp.correap
Juan Pablo Sarmiento Sanabria | jp.sarmientos
Sergio David Sierra Sanmiguel | sd.sierra

Para ejecutar el programa, abra una línea de comandos en esta carpeta y ejecute lo siguiente,
recuerde reemplazar los valores entre los símbolos <>, sin incluirlos:

Todos los valores de entrada deben ser ingresados en el correcto orden:

Una vez validado que cumple lo anterior, ejecute:
    python vertex_cover.py "<archivo de entrada>" <numero del algoritmo>

Un ejemplo de la ejecución anterior es:
    python vertex_cover.py "test_files/ensayo.txt" 2

Posteriormente, verá en la consola el conjunto de vértices a elegir, y el
tiempo que tomó al algoritmo hayar esa solución.

----------------
  ¡IMPORTANTE!
----------------
El archivo de entrada debe contar con los ejes del grafo de esta forma:
- Cada línea del archivo debe contener una pareja de números que representan
  los dos vértices conectados, separados por tab.
- NO incluya una línea adicional al inicio del archivo indicando la cantidad de
  vértices o de ejes, esto haría creer al programa que existe una conexión entre
  esos dos números e implicaría que no se ejecutaran correctamente los programas.