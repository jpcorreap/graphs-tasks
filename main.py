"""
 Implementar en grupos de 3 personas tanto en java como en python el algoritmo RSA para generar llaves
 privadas y públicas. Los programas deben recibir por argumentos el rango (mínimo y máximo) de valores
 entre los que se debe generar p y q. Para el caso de java, utilizar la clase BigInteger para poder
 trabajar con números grandes. Los programas deben imprimir en consola los parámetros de las funciones
 P(x) y S(x) que corresponden a las llaves pública y privada.

 Para la verificación de primalidad se puede utilizar el algoritmo clásico de complejidad O(2β2)
 Experimentar los programas con diferentes valores del rango de búsqueda de primos y calcular los
 tiempos de ejecución de los programas.
 Entregar un archivo zip que contenga el código fuente de las soluciones a los problemas y un README.txt
 que indique cómo se deben ejecutar los programas implementados.
"""

from decimal import Decimal
import sys
import time


def _gcd(k, totient):
    while totient != 0:
        c = k % totient
        k = totient
        totient = c
    return k


if __name__ == "__main__":
    start = time.time()
    d = 0

    # Variables de entrada
    min_value, max_value = int(sys.argv[1]), int(sys.argv[2])
    message = int(sys.argv[3])
    primes = []
    if min_value == 1:
        primes.append(min_value)
        min_value += 1
        if max_value >= 2:
            primes.append(min_value)
            min_value += 1
    if min_value == 2:
        primes.append(min_value)
    if min_value % 2 == 0:
        min_value += 1
    for i in range(min_value, max_value+1, 2):
        flag = 1
        j = 2
        while(j * j <= i):
            if (i % j == 0):
                flag = 0
                break
            j += 1
        if (flag == 1):
            primes.append(i)
    # Se calculan n y phi(n)
    p, q = primes[-2], primes[-1]
    n = p*q
    phi = (p-1)*(q-1)

    # Se calcula e
    e = 2
    for e in range(2, phi):
        if _gcd(e, phi) == 1:
            break

    # Se calcula d
    for i in range(1, 10):
        x = 1 + i*phi
        if x % e == 0:
            d = int(x/e)
            break

    local_cipher = Decimal(0)
    local_cipher = pow(message, e)
    cipher_text = local_cipher % n

    decrypt_t = Decimal(0)
    decrypt_t = pow(cipher_text, d)
    decrpyted_text = decrypt_t % n
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"Cadena Original: {message}")
    print(f"P(e,n) = P({e}, {n})")
    print(f"S(d,n) = S({d}, {n})")
    print("phi =", str(phi))
    print("Cadena Cifrada =", str(cipher_text))
    print("Cadena Descifrada =", str(decrpyted_text))
    print("Tiempo de Ejecucion = {} ms".format((time.time()-start)*1000))
