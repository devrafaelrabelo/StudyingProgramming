package Aula1;

public class PrimeiraClasse {

    public static void main(String args[]) {

        Cliente cliente = new Cliente();
        cliente.setNome("Rafael Rabelo");
        cliente.setCodigo(132456789);
        cliente.cadastrarEndereco("Rua Amazonas 399 A");
        System.out.println(cliente.getNome());
        System.out.println(cliente.getCodigo());
        cliente.imprimirEndereco();
    }
}
