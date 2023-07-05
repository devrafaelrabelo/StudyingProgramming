public class PrimeiraClasse {

    public static void main(String arg[]) {

        operacoesAritmeticas();
        operacoesAtribuicoes();
        operacoesIncrementoDecremento();
        operadadoresRelacionais();
        operacoesLogicas();
    }

    private static void operacoesLogicas() {
        System.out.println("\n**** Operadores Logicos ****");
        System.out.println("**** Not (!...variavel) | Our (||) | And (&&) ****");
        int num1 = 9;
        int num2 = 20;
        Boolean isNot = num1 > num2;
        Boolean isOur = num1 >= 0 || num1 <= 10;
        Boolean isAnd = num2 >= 0 && num2 <= 10;

        System.out.println("\nNOT (!)");
        System.out.println("num1 > num2");
        System.out.println("isNot " + isNot);
        System.out.println("!isNot " + !isNot);

        System.out.println("\nOur (||)");
        System.out.println("num1 >= 0 || num1 <= 10");
        System.out.println("isOur " + isOur);

        System.out.println("\nAnd (&&)");
        System.out.println("num1 >= 0 && num1 <= 10");
        System.out.println("isAnd " + isAnd);


    }

    private static void operadadoresRelacionais() {
        System.out.println("\n**** Operadors Relacionais ****");
        System.out.println("**** Igual (==) | Diferente (!=)  ****");
        System.out.println("**** Maior que (>) | Igual ou maior que (>=)  ****");
        System.out.println("**** Menor que (<) | Igual ou menor que (<=)  ****");
        System.out.println("**** Not (!...variavel) | Our (||) | And (&&) ****");
        int num1 = 10;
        int num2 = 20;

        System.out.println("\nIgual (==)");
        System.out.println(num1 + " == " + num2);
        System.out.println(num1 == num2);

        System.out.println("\nDiferente (!=)");
        System.out.println(num1 + " != " + num2);
        System.out.println(num1 != num2);

        System.out.println("\nMaior que (>)");
        System.out.println(num1 + " > " + num2);
        System.out.println(num1 > num2);

        System.out.println("\nIgual ou maior que (>=)");
        System.out.println(num1 + " >= " + num2);
        System.out.println(num1 >= num2);

        System.out.println("\nMenor que (>)");
        System.out.println(num1 + " < " + num2);
        System.out.println(num1 < num2);

        System.out.println("\nIgual ou menor que (>=)");
        System.out.println(num1 + " <= " + num2);
        System.out.println(num1 <= num2);

    }

    private static void operacoesIncrementoDecremento() {
        System.out.println("\n**** Operacoes Incremento e Decremento ****");
        System.out.println("**** Incremento (++) | Decremento (--)  ****");
        int num1 = 10;
        int num2 = 10;

        System.out.println("\nIncrementando");
        System.out.println("0 " + num1);
        num1++;
        System.out.println("1 " + num1);
        num1++;
        System.out.println("2 " + num1);
        num1++;
        System.out.println("3 " + num1);
        num1++;
        System.out.println("4 " + num1);
        num1++;
        System.out.println("5 " + num1);

        System.out.println("\nDecrementando");
        System.out.println("0 " + num2);
        num2--;
        System.out.println("1 " + num2);
        num2--;
        System.out.println("2 " + num2);
        num2--;
        System.out.println("3 " + num2);
        num2--;
        System.out.println("4 " + num2);
        num2--;
        System.out.println("5 " + num2);
    }

    public static void operacoesAtribuicoes() {
        System.out.println("\n**** Operacoes Atribuicoes ****");
        System.out.println("**** MAIS (+=) | MENOS (-=) ****");
        int num1 = 1;
        System.out.println("Numero 1 = " + num1);
        int num2 = 5;
        System.out.println("Numero 2 = " + num2);

        num1 += num1 + num2;
        System.out.println("\nnum1 += num2 = " + num1);
        System.out.println("resul = num1 + num2 = " + num1);
        num1 -= num1 + num2;
        System.out.println("\nnum1 -= num2 = " + num1);
        System.out.println("resul = num1 - num2 = " + num1);
        num1 *= num1 + num2;
        System.out.println("\nnum1 *= num2 = " + num1);
        System.out.println("resul = num1 * num2 = " + num1);
        num1 /= num1 + num2;
        System.out.println("\nnum1 /= num2 = " + num1);
        System.out.println("resul = num1 / num2 = " + num1);
    }

    public static void operacoesAritmeticas() {
        System.out.println("\n**** Operacoes Aritmeticas ****");
        System.out.println("**** SOMA (+) | MENOS (-) | DIVISAO (/) | MULTIPLICAÇÃO (*) ****");
        int num1 = 10;
        int num2 = 20;

        int resul = num1 + num2;

        int resul1 = num1 - num2;

        int resul2 = num1 / num2;

        int resul3 = num1 * num2;

        int resul4 = (num1 + num2) / 2;

        int resul5 = (num1 - num2) / 2;

        int resul6 = (num1 / num2) / 2;

        int resul7 = (num1 * num2) / 2;

        System.out.println(resul);
        System.out.println(resul1);
        System.out.println(resul2);
        System.out.println(resul3);
        System.out.println(resul4);
        System.out.println(resul5);
        System.out.println(resul6);
        System.out.println(resul7);
    }

}
