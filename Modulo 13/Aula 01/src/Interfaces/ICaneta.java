package Interfaces;

public interface ICaneta {
    public void escrever(String texto);

    public String getCor();

    default void escritaComum(){
        System.out.println("Testendo Escrita igual");
    }
}
