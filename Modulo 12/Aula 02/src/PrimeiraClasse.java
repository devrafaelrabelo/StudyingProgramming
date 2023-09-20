import java.util.Scanner;

public class PrimeiraClasse {
    public static void main(String[] args) {
        //exempleBubbleSortFixo();
        exempleBubbleSortDinamico();
    }

    private static void exempleBubbleSortDinamico() {
        Scanner s = new Scanner(System.in);
        System.out.print("Digitos os numero separados por ( , ): ");
        String resposta = s.next();
        String[] vetStr = resposta.split(",");
        int[] vet = convert(vetStr);
        int aux = 0;
        int i = 0;

        System.out.println("Vertor Desordenado");
        for (i = 0; i < vet.length; i++) {
            System.out.printf(" " + vet[i]);
        }
        System.out.println();

        //Codigo para organizar Array
        for (i = 0; i < vet.length; i++) {
            for (int j = 0; j < vet.length - 1; j++) {
                if (vet[j] > vet[j + 1]) {
                    aux = vet[j];
                    vet[j] = vet[j + 1];
                    vet[j + 1] = aux;
                }
            }
        }
        System.out.println("Vertor Organizado");
        for (i = 0; i < vet.length; i++) {
            System.out.printf(" " + vet[i]);
        }
        System.out.println();
    }

    private static int[] convert(String[] vetStr){
        int[] numbers = new int[vetStr.length];
        for (int i = 0; i < vetStr.length; i++) {
            numbers[i] = Integer.parseInt(vetStr[i]);
        }
        return numbers;
    }

    private static void exempleBubbleSortFixo() {
        int[] vet = {8, 3, 9, 10, 5, 2, 1};
        int aux = 0;
        int i = 0;

        System.out.println("Vertor Desordenado");
        for (i = 0; i < vet.length; i++) {
            System.out.printf(" " + vet[i]);
        }
        System.out.println();

        //Codigo para organizar Array
        for (i = 0; i < 7; i++) {
            for (int j = 0; j < 6; j++) {
                if (vet[j] > vet[j + 1]) {
                    aux = vet[j];
                    vet[j] = vet[j + 1];
                    vet[j + 1] = aux;
                }
            }
        }
        System.out.println("Vertor Organizado");
        for (i = 0; i < vet.length; i++) {
            System.out.printf(" " + vet[i]);
        }
        System.out.println();
    }
}
