import java.util.Scanner;

public class PrimeiraClasse {


    public static void main(String args[]) {
        maioreMenor();
        entreNumeros();

    }

    public static void maioreMenor() {
        int result = scannerInt();
        if (result >= 2) {
            System.out.println("Numero maior que 2");
        } else {
            System.out.println("Numero menor que 2");
        }
    }

    public static void entreNumeros() {
        int result = scannerInt();
        if (result >= 1 && result <= 5) {
            System.out.println("Numero esta entre 1 e 5");
        } else if (result >= 6 && result <= 10) {
            System.out.println("Numero esta entre 6 e 10");
        } else {
            System.out.println("Fora dos quadros anteriores ");
        }
    }

    public static int scannerInt() {
        Scanner s = new Scanner(System.in);

        System.out.print("Digite: ");
        int dado = s.nextInt();
        return dado;
    }

    public static int scannerString() {
        Scanner s = new Scanner(System.in);

        System.out.print("Digite: ");
        int dado = s.nextInt();
        return dado;
    }
}