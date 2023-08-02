public class PrimeiraClasse {
    public static void main(String[] args) {
        //declaracaoArray();
        //tamanhoArray();
        //percorrendoArray();
        //percorrendoArrayDois();
        //declaracaoArrayBiDimencional();

    }

    private static void declaracaoArrayBiDimencional() {
        System.out.println("|| Declarando Array Bidimencional");
        int[][] arrayUm = {{1, 2, 3}, {4, 5, 6}};
        int[][] arrayDois = {{1,2},{3}, {4, 5, 6}};

        System.out.println("Valores no arrayUm passados na linha são");
        outputArray(arrayUm);
        System.out.println();

        System.out.println("Valores no arrayDois passados na linha são");
        outputArray(arrayDois);
    }

    private static void outputArray(int[][] array) {
        //Faz um loop pelas linhas de Array
        for (int linha = 0; linha <array.length; linha++) {
            //Faz um loop pelas coluna de Array
            for (int coluna = 0; coluna < array[linha].length; coluna++) {
                System.out.printf(" %d ", array[linha][coluna]);
            }
            System.out.println();
        }
    }

    private static void percorrendoArrayDois() {
        System.out.println("|| Percorrando  Array 2");
        int[] arrayUm = {12, 3, 5, 8, 15, 60, 2, 80, 1000};

        for (int i = 0; i < arrayUm.length;i++) {
            System.out.println(arrayUm[i]);
        }
    }

    private static void percorrendoArray() {
        System.out.println("|| Percorrando  Array");
        int[] arrayUm = {12, 3, 5, 8, 15, 60, 2, 80, 1000};
        int total = 0;


        for (int i : arrayUm) {
            total+= i;
        }

        System.out.println("Total dos valores no Array: " + total);

    }

    private static void tamanhoArray() {
        System.out.println("|| Tamanho do Array");
        int[] arrayUm = {12, 3, 5, 8, 15, 60, 2, 80, 90};
        int[] arrayDois = {56, 58, 59, 62};

        if(arrayDois.length > 5) {
            System.out.println("Tamanho do Array é Maior que 5");
        } else {
            System.out.println("Tamanho do Array é Menor que 5");
        }

        if(arrayUm.length > 5) {
            System.out.println("Tamanho do Array é Maior que 5");
        } else {
            System.out.println("Tamanho do Array é Menor que 5");
        }
    }

    private static void declaracaoArray() {
        System.out.println("|| Declaração de Array");
        //[] São inserido em uma variavel que referencia o Array
        int[] a = new int[4];

        //[] Outra maneira de declarar Array
        int[] b;

        //Declarando variaveis Array
        int[] c = new int[44], d = new int[23];

        //Inicializando valores no Array na sua declaração
        int[] iniciandoValoresArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        //Declara uma array de Inteiros
        int[] meuArray;

        //Alocar memoria para 10 inteiros
        meuArray = new int[10];

        //Inicializar o primeiro elemento

        meuArray [0] = 100;
        meuArray [1] = 102;
        meuArray [2] = 103;
        meuArray [3] = 104;
        meuArray [4] = 105;
        meuArray [5] = 106;
        meuArray [6] = 107;
        meuArray [7] = 108;
        meuArray [8] = 109;
        meuArray [9] = 110;
        //meuArray [10] = 564;
        //Meu Array 10 estoura o limite de espaço alocado

        System.out.println(meuArray [9]);
        System.out.println(meuArray [0]);

    }


}
