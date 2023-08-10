import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class PrimeiraClasse {
    public static void main(String[] args) {
        //exempleListaSimplesHashSet();
        //exempleListaSimplesHashSetOrdemAsc();
        //exempleListaSimplesHashSetClasse();
        //exempleListaSimplesHashSetClasseConsultando();
        exempleListaSimplesHashSetClasseRemovendo();
    }

    private static void exempleListaSimplesHashSetClasseRemovendo() {
        System.out.println("|| Exemplos Lista Simples HashSet C/ Classe");
        Set<Aluno> conjunto = new HashSet<>();
        Aluno a = new Aluno("Roger Rabelo", "Office Basico", 10);
        Aluno b = new Aluno("Rafael Rabelo","Linux Basico", 5);
        Aluno c = new Aluno("Rafael Rabelo", "Windows Basico", 20);
        Aluno d = new Aluno("Rafael Rabelo", "Windows Basico", 20);
        Aluno e = new Aluno("Violeta Rabelo", "SQL Basico", 5);
        Aluno f = new Aluno("Jessica Souza", "SQL Basico", 5);

        conjunto.add(a);
        conjunto.add(b);
        conjunto.add(c);
        conjunto.add(d);
        conjunto.add(e);
        conjunto.add(f);

        System.out.println(conjunto);
        System.out.println(conjunto.contains(e));

        conjunto.remove(e);
        System.out.println(conjunto.contains(e));

        System.out.println(conjunto);
        System.out.println("");
    }

    private static void exempleListaSimplesHashSetClasseConsultando() {
        System.out.println("|| Exemplos Lista Simples HashSet C/ Classe");
        Set<Aluno> conjunto = new HashSet<>();
        Aluno a = new Aluno("Roger Rabelo", "Office Basico", 10);
        Aluno b = new Aluno("Rafael Rabelo","Linux Basico", 5);
        Aluno c = new Aluno("Rafael Rabelo", "Windows Basico", 20);
        Aluno d = new Aluno("Rafael Rabelo", "Windows Basico", 20);
        Aluno e = new Aluno("Violeta Rabelo", "SQL Basico", 5);
        Aluno f = new Aluno("Jessica Souza", "SQL Basico", 5);

        conjunto.add(a);
        conjunto.add(b);
        conjunto.add(c);
        conjunto.add(d);
        conjunto.add(e);
        conjunto.add(f);

        System.out.println(conjunto.contains(e));

        System.out.println(conjunto);
        System.out.println("");
    }

    private static void exempleListaSimplesHashSetClasse() {
        System.out.println("|| Exemplos Lista Simples HashSet C/ Classe");
        Set<Aluno> conjunto = new HashSet<>();
        Aluno a = new Aluno("Roger Rabelo", "Office Basico", 10);
        Aluno b = new Aluno("Rafael Rabelo","Linux Basico", 5);
        Aluno c = new Aluno("Rafael Rabelo", "Windows Basico", 20);
        Aluno d = new Aluno("Rafael Rabelo", "Windows Basico", 20);
        Aluno e = new Aluno("Violeta Rabelo", "SQL Basico", 5);
        Aluno f = new Aluno("Jessica Souza", "SQL Basico", 5);

        conjunto.add(a);
        conjunto.add(b);
        conjunto.add(c);
        conjunto.add(d);
        conjunto.add(e);
        conjunto.add(f);

        System.out.println(conjunto);
        System.out.println("");
    }

    private static void exempleListaSimplesHashSet() {
        System.out.println("|| Exemplos Lista Simples HashSet");
        Set<String> lista = new HashSet<>();
        lista.add("Roger Rabelo");
        lista.add("Rafael Rabelo");
        lista.add("Rafael Rabelo");
        lista.add("Rafael Rabelo");
        lista.add("Violeta Rabelo");
        lista.add("Jessica Souza");

        System.out.println(lista);
        System.out.println("");

        /**
        Set<Integer> listaNum = new HashSet<>();
        for (int i = 20000 - 1; i > 0 ; i--) {
            listaNum.add(i);
        }
        System.out.println(listaNum);
        System.out.println("");
        */

    }

    private static void exempleListaSimplesHashSetOrdemAsc() {
        System.out.println("|| Exemplos Lista Ordenada Asc HashSet");
        Set<String> lista = new HashSet<String>();
        lista.add("Roger Rabelo");
        lista.add("Jessica Souza");
        lista.add("Rafael Rabelo");
        lista.add("Violeta Rabelo");
        //Collections.sort(lista);
        System.out.println(lista);
        System.out.println("");
    }


}
