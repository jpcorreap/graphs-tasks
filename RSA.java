
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
        int p = Integer.parseInt(args[0]);
        int q = Integer.parseInt(args[1]);
        int message = Integer.parseInt(args[2]);

        // Otras variables
        int d = 0;

        // Se inicia el contador
        long initialTime = System.currentTimeMillis();

        // Se calculan n y phi(n)
        int n = p * q;
        int phi = (p - 1) * (q - 1);

        // Se calcula k
        for (int k = 2; k < phi; k++) {
            if (gcd(k, phi) == 1) {
                break;
            }
        }

        // Se calcula d
        for (int i = 2; i < 10; i++) {
            int x = 1 + i * phi;
            if (x % k == 0) {
                d = (int) (x / k);
                break;
            }
        }

        BigInteger localCipher = Math.pow(message, k);
        BigInteger cipherText = localCipher.mod(n);

        BigInteger decryptT = cipherText.pow(d);
        BigInteger decrpytedText = decryptT.mod(n);

        System.out.println("n = " + Integer.toString(n));
        System.out.println("k = " + Integer.toString(k));
        System.out.println("phi = " + Integer.toString(phi));
        System.out.println("d = " + Integer.toString(d));
        System.out.println("cipher text = " + cipherText);
        System.out.println("decrypted text = " + decrpytedText);
        System.out.println("time = " + Double.toString(System.currentTimeMillis() - initialTime) + " ms");
    }
}