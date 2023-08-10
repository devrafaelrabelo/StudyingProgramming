package abstratas;

public class Comissado extends Empregado{
    private double totalVenda;
    private double totalComissao;

    @Override
    public Double vencimento() {
        return totalVenda * totalComissao;
    }

    public double getTotalVenda() {
        return totalVenda;
    }

    public void setTotalVenda(double totalVenda) {
        this.totalVenda = totalVenda;
    }

    public double getTotalComissao() {
        return totalComissao;
    }

    public void setTotalComissao(double totalComissao) {
        this.totalComissao = totalComissao;
    }
}
