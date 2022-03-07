
# Implementar en grupos de 3 personas tanto en java como en python el algoritmo RSA para generar llaves
# privadas y públicas. Los programas deben recibir por argumentos el rango (mínimo y máximo) de valores
# entre los que se debe generar p y q. Para el caso de java, utilizar la clase BigInteger para poder
# trabajar con números grandes. Los programas deben imprimir en consola los parámetros de las funciones
# P(x) y S(x) que corresponden a las llaves pública y privada.
# 
# Para la verificación de primalidad se puede utilizar el algoritmo clásico de complejidad O(2β2)
# Experimentar los programas con diferentes valores del rango de búsqueda de primos y calcular los
# tiempos de ejecución de los programas.
# Entregar un archivo zip que contenga el código fuente de las soluciones a los problemas y un README.txt
# que indique cómo se deben ejecutar los programas implementados.

import math
 
message = int(input("Enter the message to be encrypted: ")) 
 
p = 11
q = 7
e = 3
 
n = p*q
 
def encrypt(me):
    en = math.pow(me,e)
    c = en % n
    print("Encrypted Message is: ", c)
    return c
 
print("Original Message is: ", message)
c = encrypt(message)