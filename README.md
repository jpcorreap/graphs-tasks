# Graph Tasks<br />

| Integrante | Login |
| ------ | ------ |
| Juan Pablo Correa Puerta | jp.correap |
| Juan Pablo Sarmiento Sanabria | jp.sarmientos |
| Sergio David Sierra Sanmiguel | sd.sierra |

<br />
Los ejercicios están separados en archivos .py con los respectivos nombres.

Para probar cada uno de los puntos, se adicionaron tres archivos test.py.

Para ejecutar los tests, abra una línea de comandos en esta carpeta y ejecute: <br />
`python tests_exercise_<No. de ejercicio>.py`

Es importante mencionar que la representación de grafo que usamos para cada punto es distinta:

- **Ejercicio 1:** representación como lista de adyacencias.
- **Ejercicio 4:** representación como matriz de adyacencias.
- **Ejercicio 5:** representación como lista de arcos, donde cada elemento de la lista esta compuesto por un nodo de inicio, nodo final y el costo del arco, i. e. `[u, v, w]`.

Adicionalmente, anexamos representaciones gráficas para algunos de los tests implementados, para que le faciliten al evaluador la revisión y validación de los algoritmos: <br />
<br /><br />
## **Punto 1:** <br />
### Test 3: <br />
Grafo de entrada: <br />
![image](https://user-images.githubusercontent.com/47229643/153119611-6e1c40e4-b4ed-4fe7-950d-9d5cc4b2ba20.png) <br />
El algoritmo calcula el BFS: <br />
![ezgif com-gif-maker](https://user-images.githubusercontent.com/47229643/153119495-02207416-b019-44f6-8f89-6d64a116a24b.gif) <br />
*Arreglo final de separación entre el nodo de inicio y los demás vértices:* [0, 2, 1, 1, 2, 3, 3, 4, 3, 2]
<br />
<br />
## **Punto 4:** <br />
### Test 1: <br />
Grafo de entrada: <br />
![image](https://user-images.githubusercontent.com/47229643/153116681-0348b3f6-49af-4fb7-a1b6-2a82605edc31.png) <br />

Dijkstra entre 8 y 4: <br />
![image](https://user-images.githubusercontent.com/47229643/153116880-918651b7-dc52-4393-b2ea-393ec0b29b15.png)
<br /><br />
## **Punto 5:** <br />
### Test 1: <br />
Grafo de entrada: <br />
![image](https://user-images.githubusercontent.com/47229643/153114757-a6b2ccc9-5099-432d-ad7a-b33c53c045c2.png)

El algoritmo hallará el MST: <br />
![image](https://user-images.githubusercontent.com/47229643/153114943-1f423c38-f780-4d39-9cff-555994886cb3.png)

Y el inverso de este MST será la respuesta al algoritmo: <br />
![image](https://user-images.githubusercontent.com/47229643/153115517-9c5bf16e-0d50-4816-a797-163b397c538a.png)



