import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class PrimeiraClassse {

    public static void main(String[] args) {
        //exempleListaSimplesOrdenadaClasseExterna();
        //exempleListaSimplesOrdenadaComparatorAutor();
        exempleListaSimples();
        exempleLinkedList();
    }

    private static void exempleListaSimplesOrdenadaClasseExterna() {
        System.out.println( "|| Exemplo Lista Simples Ordenada Classe Externa");
        List<Aluno> lista = new ArrayList<Aluno>();

        Aluno a = new Aluno("Rafael Rabelo", "Linux Basico", 20);
        Aluno b = new Aluno("Roger Rabelo", "Office Basico", 5);
        Aluno c = new Aluno("Violeta Rabelo", "Windows Basico", 40);
        Aluno d = new Aluno("Jessica", "Java Basico", 8);
        Aluno e = new Aluno("Oscar Rabelo", "Python Basico", 15);

        lista.add(a);
        lista.add(b);
        lista.add(c);
        lista.add(d);
        lista.add(e);
        System.out.println("|| Lista Normal");
        System.out.println(lista);
        System.out.println("|| Lista Sort (Ordenada)");
        Collections.sort(lista);
        System.out.println(lista);
    }

    public static void exempleListaSimplesOrdenadaComparatorAutor() {
        System.out.println("\n|| Exemplo Lista Simples Ordenada Comparator Autor");
        List<Aluno> lista = new ArrayList<Aluno>();

        Aluno a = new Aluno("Rafael Rabelo", "Linux Basico", 20);
        Aluno b = new Aluno("Roger Rabelo", "Linux Basico", 5);
        Aluno c = new Aluno("Violeta Rabelo", "Linux Basico", 40);
        Aluno d = new Aluno("Jessica", "Linux Basico", 8);
        Aluno e = new Aluno("Oscar Rabelo", "Linux Basico", 15);

        lista.add(a);
        lista.add(b);
        lista.add(c);
        lista.add(d);
        lista.add(e);
        System.out.println("|| Lista Normal");
        System.out.println(lista);
        System.out.println("|| Lista Sort (Ordenada)");
        ComparaNotaAluno comparaNotaAluno = new ComparaNotaAluno();
        Collections.sort(lista, comparaNotaAluno);
        System.out.println(lista);


    }

    public static void exempleListaSimples() {
        System.out.println("\n|| Exemplo Lista Simples");
        List<String> lista = new LinkedList<>();
        lista.add("Roger Rabelo");
        lista.add("Rafal Rabelo");
        lista.add("Jessica");
        System.out.println("|| Normal");
        System.out.println(lista);
        System.out.println("");
    }

    public static void exempleLinkedList() {
        System.out.print("\n|| Exemplo LinkedList");
        List<String> lista = new LinkedList<String>();
        lista.add("Roger Rabelo");
        lista.add("Rafal Rabelo");
        lista.add("Jessica");
        System.out.println("|| Normal");
        System.out.println(lista);
        System.out.println("|| Ordenada Asc");
        Collections.sort(lista);
        System.out.println(lista);
        System.out.println("|| Com remoção");
        lista.remove(1);
        System.out.println(lista);
        boolean contem = lista.contains("Jessica");
        System.out.println("|| Contem (Jessica): " + contem );
        System.out.println("");
    }
}
