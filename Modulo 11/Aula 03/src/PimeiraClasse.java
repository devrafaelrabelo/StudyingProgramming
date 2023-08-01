import java.util.PriorityQueue;
import java.util.Queue;

public class PimeiraClasse {
    public static void main(String[] args) {
        exemplePriorityQueue();
    }
    public static void exemplePriorityQueue(){
        //Ordenação Natural
        Queue<String> queue = new PriorityQueue<String>();
        queue.add("Short");
        queue.add("Camisa");
        queue.add("Tenis");
        while (queue.size() != 0) {
            System.out.println(queue.remove());
        }
    }

}
