import java.util.ArrayDeque;
import java.util.Deque;

public class exempleArrayDeque {
    public static void main(String[] args) {
        inserindoFila();
        //removendoFila();
        //acessandoFila();
    }

    private static void removendoFila() {
        System.out.println("|| Removendo");
        Deque<String> ad = new ArrayDeque<String>();
        ad.add("Red");
        ad.add("Blue");
        ad.add("White");
        ad.add("Yellow");
        ad.add("Black");

        Deque<String>  d = new ArrayDeque<String>();
        d.add("Green");
        d.add("Orange");
        d.add("Brown");
        d.add("Pink");


        ad.addAll(d);
        System.out.println("Elementos no ArrayQueue: " + ad);

        //String val = ad.remove();
        ad.remove("Black");
        System.out.println("Elementos no ArrayQueue depois da exclusão: " + ad);

        ad.removeFirst();
        ad.removeLast();
        System.out.println("Elementos no ArrayQueue depois removeFirst || removeLast: " + ad);

        ad.poll();
        ad.pollFirst();
        ad.pollLast();
        System.out.println("Elementos no ArrayQueue depois pollFirst || pollLast: " + ad);

        ad.pop();
        System.out.println("Elementos no ArrayQueue depois pop: " + ad);

        ad.retainAll(d);
        System.out.println("Elementos no ArrayQueue depois retainAll: " + ad);

        ad.removeAll(d);
        System.out.println("Elementos no ArrayQueue depois removeAll: " + ad);
    }

    private static void inserindoFila() {
        System.out.println("|| Removendo");
        Deque<String> ad = new ArrayDeque<String>();
        ad.add("Red");
        ad.addFirst("Blue");
        ad.addLast("White");
        ad.add("Yellow");
        ad.add("Black");
        System.out.println("Elementos no ArrayQueue AD: " + ad);

        Deque<String>  d = new ArrayDeque<String>();
        d.add("Green");
        d.addFirst("Orange");
        d.add("Brown");
        d.add("Pink");
        System.out.println("Elementos no ArrayQueue D: " + d);

        ad.addAll(d);
        System.out.println("Elementos no ArrayQueue depois de juntar: " + ad);

        boolean val = ad.offer("Pretin");
        ad.offerFirst("Branquin");
        ad.offerLast("Amarelin");
        System.out.println("Elementos no ArrayQueue depois offerFirst || offerLast " + ad);

        ad.push("Azulin");
        System.out.println("Elementos no ArrayQueue depois push " + ad);
    }

    private static void acessandoFila() {
        System.out.println("|| ACESSANDO");
        Deque<String> ad = new ArrayDeque<String>();
        ad.add("Red");
        ad.add("Blue");
        ad.add("White");
        ad.add("Yellow");
        ad.add("Black");

        Deque<String>  d = new ArrayDeque<String>();
        d.add("Green");
        d.add("Orange");

        ad.addAll(d);
        System.out.println(ad);
        System.out.println(ad.contains("White"));
        System.out.println(d.contains("Brown"));
        System.out.println( d.containsAll(d));

        System.out.println(ad);
        System.out.println("Saida Elemento: " + ad.element());
        System.out.println("Pegando Primeiro elemento usando getFirst: " + ad.getFirst());
        System.out.println("Pegando Ultimo elemento usando getLast: " + ad.getLast());
        System.out.println("Pegando elemento com Peek: " + ad.peek());
        System.out.println("Pegando Primeiro elemento usando peekFirst: " + ad.peekFirst());
        System.out.println("Pegando Ultimo elemento usando peekLast: " + ad.peekLast());
        System.out.println();

    }

}
