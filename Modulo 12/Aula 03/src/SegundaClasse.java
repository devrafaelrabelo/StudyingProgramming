import javax.swing.undo.CannotUndoException;
import java.util.*;

public class SegundaClasse {
    public static void main(String[] args) {
        Map<Integer, List<Aluno>> listaSala = new HashMap<>();

        List<Aluno> alunoSala1 = criarTurma("Sala 01", 10);
        listaSala.put(1, alunoSala1);

        List<Aluno> alunoSala2 = criarTurma("Sala 02", 20);
        listaSala.put(2, alunoSala2);
        System.out.println("Sala 01");
        imprimirAlunosSala(listaSala.get(1));

        System.out.println("\nSala 02");
        imprimirAlunosSala(listaSala.get(2));
        
        exempleIterator();
    }

    private static void exempleIterator() {
        System.out.println("|| Exemplo Lista Iterator");
        List<String> lista = new ArrayList<>();
        lista.add("Rafael Rabelo");
        lista.add("Roger Rabelo");
        lista.add("Violeta Rabelo");

        Iterator<String> it = lista.iterator();

        while (it.hasNext()) {
            System.out.println(it.next());
        }
    }

    private static void imprimirAlunosSala(List<Aluno> alunos) {
        //For - Java 8 API Stream
        System.out.println("For - Java 8 API Stream");
        alunos.forEach(aluno -> System.out.println("Nome: " + aluno.getNome() + " Sala: " + aluno.getSala()));
        System.out.println("");

        System.out.println("For - Java");
        for (Aluno aluno : alunos) {
            System.out.println("Nome: " + aluno.getNome() + " Sala: " + aluno.getSala());
        }
        System.out.println();

        System.out.println("For - Java com Contador");
        for (int i = 0; i < alunos.size(); i++) {
            Aluno aluno = alunos.get(i);
            System.out.println("Nome: " + aluno.getNome() + " Sala: " + aluno.getSala());
        }
    }

    private static List<Aluno> criarTurma(String sala, int count) {
        List<Aluno> alunos = new ArrayList<>();
        for (int i = 0; i < count;i++) {
            Aluno aluno = new Aluno("Nome aluno: " + i, "Sala: " + i, i, sala);
            alunos.add(aluno);
        }
        return alunos;
    }


}
