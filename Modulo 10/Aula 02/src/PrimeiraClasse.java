import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PrimeiraClasse {
    public static void main(String[] args) {
        //exemploUmFor();
        //exemploDoisFor();
        //exemploTresFor();
        //tabuadaFor();
        //exemploBreakUm();
        //exemploBreakDois();
        //exemploWhile();
        //tabuadaWhile();
        tabuadaDoWhile();
    }

   public static void exemploUmFor() {
       System.out.println("exemploUm");
        for (int i = 1; i <= 10; i++) {
            System.out.println("Contato: " + i);
        }
    }

    public static void exemploDoisFor() {
        System.out.println("exemploDois");
        List<Integer> valores = new ArrayList<>();
        for (int i = 1; i < 10; i++) {
            System.out.println("Contato: " + i);
            valores.add(i);
        }
        System.out.println(valores);

        for ( Integer i : valores) {
            System.out.println(i);
        }

        valores.forEach(i-> System.out.println(i));
    }

    public static void exemploTresFor() {
        System.out.println("exemploTres");
        int[] valores = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,15};
        for ( Integer i : valores) {
            System.out.println(i);
        }
    }

    public static void tabuadaFor() {
        Scanner s = new Scanner(System.in);

        System.out.print("Digite um número para gerar tabuada: ");
        int num = s.nextInt();

        for(int i = 0; i <= 10; i++) {
            System.out.println(num + " X " + i + " = " + num*i);

        }
    }

    public static void exemploBreakUm () {
        for (int i=0; i <= 100; i++) {
            System.out.println("Numero: " + i);

            if(i == 50)
                break;

/*          if(i == 50) {
                break;
            }*/
        }
    }

    public static void exemploBreakDois () {
        for (int i =0; i <= 100; i++) {
            if (i%5 != 0) {
                continue;
            }
            System.out.println("Contador: " + i);
          /*  if (i%5 == 0) {
                System.out.println("Contador: " + i);
            }*/

        }
    }

    public static void exemploWhile () {
        int i = 0;
        while (i < 2) {
            System.out.println("Numero: " + i);
        }
    }

    public static void tabuadaWhile() {
        Scanner s = new Scanner(System.in);

        System.out.print("Deseja gerar a tabuada de algum numero: ");
        String resposta = s.next();

        while (resposta.equalsIgnoreCase("Sim") ){
            System.out.print("Digite um numero para gerar a tabuada: ");
            int num = s.nextInt();
            for(int i = 0; i <= 10; i++) {
                System.out.println(num + " X " + i + " = " + num*i);

            }
            System.out.print("Deseja gerar outra tabuada: ");
            resposta = s.next();
        }
        System.out.print("Obrigade!!!");
    }

    public static void tabuadaDoWhile() {
        Scanner s = new Scanner(System.in);
        String resposta;

        do {
            System.out.print("Digite um numero para gerar a tabuada: ");
            int num = s.nextInt();
            for(int i = 0; i <= 10; i++) {
                System.out.println(num + " X " + i + " = " + num*i);

            }
            System.out.print("Deseja gerar outra tabuada: ");
            resposta = s.next();
        }while (resposta.equalsIgnoreCase("Sim"));

        System.out.print("Obrigade!!!");
    }


}
