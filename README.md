# Tarea 2 - Análisis de Algoritmos

| Integrante | Login |
| ------ | ------ |
| Juan Pablo Correa Puerta | jp.correap |
| Juan Pablo Sarmiento Sanabria | jp.sarmientos |
| Sergio David Sierra Sanmiguel | sd.sierra |

## ¿Cómo se debe ejecutar?
- Para ejecutar el programa, ingrese en la carpeta input los archivos con extensión .txt con el siguiente formato:

    - La primera línea debe tener la cantidad de personas M y la cantidad de trabajos N.

    - Las siguientes líneas tiene dos números. El primero es un id de persona (de 0 a M-1) y el segundo es un id de trabajo (de 0 a N-1).
La línea indica que la persona i puede hacer el trabajo j.

- Finalmente, ejecute: <br />
  ```
  $ python main.py
  ```

 - Dentro de la carpeta output, podrá ver el resultado de la ejecución de todos los archivos. Recuerde que cada línea de la respuesta representa que la persona *i*, puede realizar el trabajo *j* maximizando la cantidad de trabajos que se pueden realizar.

* Adicionalmente, la cantidad de líneas en los archivos de salida, serán la cantidad de trabajos que pueden maximizarse.



**Caso de prueba demo_1.txt** <br />
Grafo de entrada: <br />
![image](https://user-images.githubusercontent.com/47229643/154191097-3ea1134c-6279-459f-abbd-d2239678e434.png) <br />

Resultado: <br />
![image](https://user-images.githubusercontent.com/47229643/154191061-8c64fafa-acd5-4485-8181-2db1e329b495.png) <br />
