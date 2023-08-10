import abstratas.Assalariado;
import abstratas.Comissado;
import abstratas.Empregado;
import abstratas.Horista;

public class PrimeraClasse {
    public static void main(String[] args) {
        System.out.println("Assalariado");
        Assalariado Assalariado = new Assalariado();
        Assalariado.setNome("Rafael Rabelo");
        Assalariado.setSobrenome("Gonçalves");
        Assalariado.setCPF("12407911601");
        Assalariado.setSalario(2500d);
        System.out.println(Assalariado.getNome() + " tem de Salario " + Assalariado.vencimento());
        imprimir(Assalariado);
        System.out.println();

        System.out.println("Comissado");
        Comissado comissado = new Comissado();
        comissado.setNome("Roger Rabelo");
        comissado.setSobrenome("Gonçalves");
        comissado.setCPF("12365498705");
        comissado.setTotalVenda(20d);
        comissado.setTotalComissao(0.50d);
        System.out.println(comissado.getNome() + " tem de Salario " + comissado.vencimento());
        imprimir(comissado);
        System.out.println();

        System.out.println("Horista");
        Horista horista = new Horista();
        horista.setNome("Violeta Rabelo");
        horista.setSobrenome("Gonçalves");
        horista.setCPF("98745632102");
        horista.setHorasTrabalhadas(10d);
        horista.setPrecoHora(50d);
        System.out.println(horista.getNome() + " tem de Salario " + horista.vencimento());
        imprimir(horista);
        System.out.println();
    }

    public static void imprimir(Empregado funcionario) {
        if (funcionario instanceof Assalariado) {
            System.out.println("Assalariado");
            System.out.println(funcionario.getNome() + " tem de Salario " + funcionario.vencimento());
            System.out.println(((Assalariado) funcionario).getSalario());
        } else if (funcionario instanceof Comissado) {
            System.out.println("Comissado");
            System.out.println(funcionario.getNome() + " tem de Salario " + funcionario.vencimento());
            System.out.println(((Comissado) funcionario).getTotalComissao());
            System.out.println(((Comissado) funcionario).getTotalVenda());
        } else if (funcionario instanceof Horista) {
            System.out.println("Horista");
            System.out.println(funcionario.getNome() + " tem de Salario " + funcionario.vencimento());
            System.out.println(((Horista) funcionario).getHorasTrabalhadas());
            System.out.println(((Horista) funcionario).getPrecoHora());
        }

    }

}
