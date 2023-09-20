import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PrimeiraClasse {

    public static void main(String[] args) {
        //exempleListaSimples();
        exempleListaSimplesOrdenadoAscendente();
    }

    public static void exempleListaSimples(){
        System.out.println( "|| Exemplo Lista Simples ||");
        List<String> lista = new ArrayList<>();
        lista.add("Rafael Rabelo");
        lista.add("Roger Rabelo");
        lista.add("Violeta Rabelo");
        lista.add("Oscar Rabelo");
        lista.add("Jessica");
        System.out.println(lista);
        System.out.println(" ");
    }

    public static void exempleListaSimplesOrdenadoAscendente(){
        System.out.println( "|| Exemplo Lista Simples");
        List<String> lista = new ArrayList<>();
        lista.add("Rafael Rabelo");
        lista.add("Roger Rabelo");
        lista.add("Violeta Rabelo");
        lista.add("Oscar Rabelo");
        lista.add("Jessica");
        System.out.println("|| Normal");
        System.out.println(lista);
        System.out.println("|| Sort");
        Collections.sort(lista);
        System.out.println(lista);
        System.out.println(" ");
    }

}
