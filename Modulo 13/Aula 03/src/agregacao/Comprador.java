package agregacao;

public class Comprador {
    private Double verba;
    private String nome;

    public Comprador(String nome, double verba) {
        this.nome = nome;
        this.verba = verba;
    }

    public double getVerba() {
        return verba;
    }

    public void setVerba(Double verba) {
        this.verba = verba;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void compra() {
        System.out.println("Comprar ");
    }
}
