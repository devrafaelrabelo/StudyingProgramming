import java.util.*;

public class PrimeiraClasse {
    public static void main(String[] args) {
        exempleListaSimples();
        exempleListaSimplesIterandoValores();
        exempleListaSimplesIterandoChaves();
        exempleListaSimplesIterandoChavesValores();
        exempleListaSimplesPegandoValor();

        exempleListaSimplesTree();
        exempleListaSimplesTreeIterandoValores();
        exempleListaSimplesTreeIterandoChaves();
        exempleListaSimplesTreeIterandoChavesValores();
        exempleListaSimplesTreePegandoValor();

        exempleListaSimplesLinkedHash();
        exempleListaSimplesLinkedHashIterandoValores();
        exempleListaSimplesLinkedHashIterandoChaves();
        exempleListaSimplesLinkedHashIterandoChavesValores();
        exempleListaSimplesLinkedHashPegandoValor();
    }

    /**
     * Permite chaves e valores null. Não existe a garantia que os dados ficarão ordenados
     *
     * Para usar uma classe que implementa Map, quaisquer classes que forem utilizadas como chaves
     * devem sobrescrever os metodos hashcode() e equals()
     */
    private static void exempleListaSimplesIterandoChavesValores() {
        System.out.println("|| Exemplo Lista Simples Iterando Chaves e Valores");
        Map<Integer, String> lista = new HashMap<>();
        lista.put(1, "Rafael Rabelo");
        lista.put(2, "Roger Rabelo");
        lista.put(3, "Jessica Souza");
        lista.put(4, "Violeta Rabelo");

        System.out.println("|| For Comum");
        Set<Map.Entry<Integer, String>> entry = lista.entrySet();
        for (Map.Entry<Integer, String> e : entry) {
            System.out.println("Chave: " + e.getKey());
            System.out.println("Valor: " + e.getValue());
        }
        System.out.println();

        System.out.println("|| ForEach Stream");
        lista.entrySet().forEach(e -> {
            System.out.println("Chave: " + e.getKey());
            System.out.println("Valor: " + e.getValue());
        });
        System.out.println();

        System.out.println("|| ForEach Stream 1");
        lista.keySet().stream().forEach(System.out::println);
        System.out.println();

        System.out.println("|| ForEach Stream 2");
        lista.values().stream().forEach(System.out::println);
        System.out.println();

        System.out.println("|| ForEach Stream 3 ");
        lista.entrySet().stream().forEach(System.out::println);
        System.out.println();

        System.out.println("|| ForEach Stream 4 ");
        lista.forEach((key, value) -> System.out.println(key + " " + value));
        System.out.println();

        System.out.println("|| Iterator");
        Iterator<Map.Entry<Integer, String>> it = lista.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<Integer, String> entry1 = it.next();
            System.out.println("Chave: " + entry1.getKey());
            System.out.println("Valor: " + entry1.getValue());

        }
        System.out.println();
    }
    private static void exempleListaSimplesIterandoChaves() {
        System.out.println("|| Exemplo Lista Simples Iterando Chaves");
        Map<Integer, String> lista = new HashMap<>();
        lista.put(1, "Rafael Rabelo");
        lista.put(2, "Roger Rabelo");
        lista.put(3, "Jessica Souza");
        lista.put(4, "Violeta Rabelo");

        for (Integer value : lista.keySet()) {
            System.out.println(value);
        }
        System.out.println();
    }
    private static void exempleListaSimplesIterandoValores() {
        System.out.println("|| Exemplo Lista Simples Iterando Valores");
        Map<Integer, String> lista = new HashMap<>();
        lista.put(1, "Rafael Rabelo");
        lista.put(2, "Roger Rabelo");
        lista.put(3, "Jessica Souza");
        lista.put(4, "Violeta Rabelo");
        for (String value : lista.values()) {
            System.out.println(value);
        }
        System.out.println();
    }
    /**
     * Chave nunca se repete
     * Pode ser retirado do mapa por chave
     */
    private static void exempleListaSimples() {
        System.out.println("|| Exemplo Lista Simples");
        Map<Integer, String> lista = new HashMap<>();
        lista.put(1, "Rafael Rabelo");
        lista.put(2, "Roger Rabelo");
        lista.put(3, "Jessica Souza");
        lista.put(4, "Violeta Rabelo");

        System.out.println(lista);
        System.out.println();
    }
    private static void exempleListaSimplesPegandoValor() {
        System.out.println("|| Exemplo Lista Simples");
        Map<Integer, String> lista = new HashMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");

        String nome = lista.get(3);
        System.out.println(nome);
        System.out.println();
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    private static void exempleListaSimplesTreeIterandoChavesValores() {
        System.out.println("|| Exemplo Lista Simples Tree Iterando Chaves e Valores");
        Map<Integer, String> lista = new TreeMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");


        System.out.println("|| For Comum");
        Set<Map.Entry<Integer, String>> entry = lista.entrySet();
        for (Map.Entry<Integer, String> e : entry) {
            System.out.println("Chave: " + e.getKey());
            System.out.println("Valor: " + e.getValue());
        }
        System.out.println();

        System.out.println("|| ForEach Stream");
        lista.entrySet().forEach(e -> {
            System.out.println("Chave: " + e.getKey());
            System.out.println("Valor: " + e.getValue());
        });
        System.out.println();

        System.out.println("|| ForEach Stream 1");
        lista.keySet().stream().forEach(System.out::println);
        System.out.println();

        System.out.println("|| ForEach Stream 2");
        lista.values().stream().forEach(System.out::println);
        System.out.println();

        System.out.println("|| ForEach Stream 3 ");
        lista.entrySet().stream().forEach(System.out::println);
        System.out.println();

        System.out.println("|| ForEach Stream 4 ");
        lista.forEach((key, value) -> System.out.println(key + " " + value));
        System.out.println();

        System.out.println("|| Iterator");
        Iterator<Map.Entry<Integer, String>> it = lista.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<Integer, String> entry1 = it.next();
            System.out.println("Chave: " + entry1.getKey());
            System.out.println("Valor: " + entry1.getValue());

        }
        System.out.println();
    }
    private static void exempleListaSimplesTreeIterandoChaves() {
        System.out.println("|| Exemplo Lista Simples Tree Iterando Chaves");
        Map<Integer, String> lista = new TreeMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");


        for (Integer value : lista.keySet()) {
            System.out.println(value);
        }
        System.out.println();
    }
    private static void exempleListaSimplesTreeIterandoValores() {
        System.out.println("|| Exemplo Lista Simples Tree Iterando Valores");
        Map<Integer, String> lista = new TreeMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");

        for (String value : lista.values()) {
            System.out.println(value);
        }
        System.out.println();
    }
    /**
     * Chave nunca se repete.
     * Garante que as chaves sempre estarão em Ordem Ascendente.
     * Pode ser retirado do mapa por chave.
     */
    private static void exempleListaSimplesTree() {
        System.out.println("|| Exemplo Lista Simples Tree");
        Map<Integer, String> lista = new TreeMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");

        System.out.println(lista);
        System.out.println();
    }
    private static void exempleListaSimplesTreePegandoValor() {
        System.out.println("|| Exemplo Lista Simples");
        Map<Integer, String> lista = new TreeMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");

        String nome = lista.get(3);
        System.out.println(nome);
        System.out.println();
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    private static void exempleListaSimplesLinkedHashIterandoChavesValores() {
        System.out.println("|| Exemplo Lista Simples Tree Iterando Chaves e Valores");
        Map<Integer, String> lista = new LinkedHashMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");


        System.out.println("|| For Comum");
        Set<Map.Entry<Integer, String>> entry = lista.entrySet();
        for (Map.Entry<Integer, String> e : entry) {
            System.out.println("Chave: " + e.getKey());
            System.out.println("Valor: " + e.getValue());
        }
        System.out.println();

        System.out.println("|| ForEach Stream");
        lista.entrySet().forEach(e -> {
            System.out.println("Chave: " + e.getKey());
            System.out.println("Valor: " + e.getValue());
        });
        System.out.println();

        System.out.println("|| ForEach Stream 1");
        lista.keySet().stream().forEach(System.out::println);
        System.out.println();

        System.out.println("|| ForEach Stream 2");
        lista.values().stream().forEach(System.out::println);
        System.out.println();

        System.out.println("|| ForEach Stream 3 ");
        lista.entrySet().stream().forEach(System.out::println);
        System.out.println();

        System.out.println("|| ForEach Stream 4 ");
        lista.forEach((key, value) -> System.out.println(key + " " + value));
        System.out.println();

        System.out.println("|| Iterator");
        Iterator<Map.Entry<Integer, String>> it = lista.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<Integer, String> entry1 = it.next();
            System.out.println("Chave: " + entry1.getKey());
            System.out.println("Valor: " + entry1.getValue());

        }
        System.out.println();
    }
    private static void exempleListaSimplesLinkedHashIterandoChaves() {
        System.out.println("|| Exemplo Lista Simples Tree Iterando Chaves");
        Map<Integer, String> lista = new LinkedHashMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");


        for (Integer value : lista.keySet()) {
            System.out.println(value);
        }
        System.out.println();
    }
    private static void exempleListaSimplesLinkedHashIterandoValores() {
        System.out.println("|| Exemplo Lista Simples Tree Iterando Valores");
        Map<Integer, String> lista = new LinkedHashMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");

        for (String value : lista.values()) {
            System.out.println(value);
        }
        System.out.println();
    }
    /**
     * Chave nunca se repete.
     * Garante que as chaves sempre estarão em Ordem Ascendente.
     * Pode ser retirado do mapa por chave.
     */
    private static void exempleListaSimplesLinkedHash() {
        System.out.println("|| Exemplo Lista Simples Tree");
        Map<Integer, String> lista = new LinkedHashMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");

        System.out.println(lista);
        System.out.println();
    }
    private static void exempleListaSimplesLinkedHashPegandoValor() {
        System.out.println("|| Exemplo Lista Simples");
        Map<Integer, String> lista = new LinkedHashMap<>();
        lista.put(3, "Jessica Souza");
        lista.put(1, "Rafael Rabelo");
        lista.put(4, "Violeta Rabelo");
        lista.put(2, "Roger Rabelo");

        String nome = lista.get(3);
        System.out.println(nome);
        System.out.println();
    }

}
