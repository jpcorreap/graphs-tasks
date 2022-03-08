
/*
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
*/
import java.math.BigInteger;
import java.util.Stack;

public class RSA {
    private static int gcd(int k, int totient) {
        while (totient != 0) {
            int c = k % totient;
            k = totient;
            totient = c;
        }
        return k;
    }

    public static void main(String[] args) {
        // Variables de entrada:
        int minValue = Integer.parseInt(args[0]);
        int maxValue = Integer.parseInt(args[1]);
        int message = Integer.parseInt(args[2]);

        // Otras variables
        Stack<Integer> primes = new Stack<Integer>();
        int d = 0;

        // Se inicia el contador
        long initialTime = System.currentTimeMillis();
        if (minValue == 1) {
            primes.push(minValue);
            minValue += 1;
            if (maxValue >= 2) {
                primes.push(minValue);
                minValue += 1;
            }
        }
        if (minValue == 2) {
            primes.push(minValue);
        }
        if (minValue % 2 == 0)
            minValue += 1;
        for (int i = minValue; i < maxValue + 1; i += 2) {
            int flag = 1;
            int j = 2;
            while (j * j <= i) {
                if (i % j == 0) {
                    flag = 0;
                    break;
                }
                j += 1;
            }
            if (flag == 1)
                primes.push(i);
        }
        int q = primes.pop();
        int p = primes.pop();
        // Se calculan n y phi(n)
        int n = p * q;
        int phi = (p - 1) * (q - 1);

        // Se calcula k
        int e = 2;
        for (int k = 2; k < phi; k++) {
            if (gcd(k, phi) == 1) {
                e = k;
                break;
            }
        }

        // Se calcula d
        for (int i = 1; i < 10; i++) {
            int x = 1 + i * phi;
            if (x % e == 0) {
                d = (int) (x / e);
                break;
            }
        }
        BigInteger localCifrado = new BigInteger(message + "");
        BigInteger localCipher = localCifrado.pow(e);
        BigInteger cipherText = localCipher.mod(new BigInteger(n + ""));

        BigInteger decryptT = cipherText.pow(d);
        BigInteger decrpytedText = decryptT.mod(new BigInteger(n + ""));

        System.out.println("p = " + Integer.toString(p));
        System.out.println("q = " + Integer.toString(q));
        System.out.println("Cadena Original = " + message);
        System.out.println(String.format("P(e,n) = P(%d,%d)", e, n));
        System.out.println(String.format("S(d,n) = S(%d,%d)", d, n));
        System.out.println("phi = " + Integer.toString(phi));
        System.out.println("Cadena Cifrada = " + cipherText);
        System.out.println("Cadena Descrifrada  = " + decrpytedText);
        System.out.println("Tiempo de Ejecucion = " + Double.toString(System.currentTimeMillis() - initialTime) + " ms");
    }
}