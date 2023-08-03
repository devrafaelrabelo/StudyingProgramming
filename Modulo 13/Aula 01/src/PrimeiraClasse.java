import Interfaces.*;

public class PrimeiraClasse {
    public static void main(String[] args) {
        System.out.println("Primeiro Teste");
        ICaneta caneta = new canetaEsferografica();
        caneta.escrever("Testando Caneta Esferografica");
        System.out.println(caneta.getCor());
        caneta.escritaComum();
        System.out.println();

        System.out.println("Segundo Teste");
        ICaneta giz = new giz();
        giz.escrever("Testando Giz");
        System.out.println(giz.getCor());
        giz.escritaComum();
        System.out.println();

        System.out.println("Terceiro Teste");
        ICaneta lapis = new lapis();
        lapis.escrever("Testando Lapis");
        System.out.println(lapis.getCor());
        lapis.escritaComum();
        System.out.println();

        System.out.println("Quarto Teste");
        System.out.println("Carro Passeio");
        Icarro carro = new carroPasseio();
        carro.andar();
        carro.parar();
        System.out.println();

        System.out.println("Quinto Teste");
        System.out.println("Carro Veloz");
        Icarro carroVel = new carroCorrida();
        carroVel.andar();
        carroVel.parar();
        System.out.println();


    }
}
