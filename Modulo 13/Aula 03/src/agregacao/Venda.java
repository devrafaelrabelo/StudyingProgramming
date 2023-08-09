package agregacao;

import java.util.ArrayList;
import java.util.List;

public class Venda {
    private Comprador comprador;
    private Vendedor vendedor;
    private List<Produto> produtos;

    public Comprador getComprador() {
        return comprador;
    }

    public void setComprador(Comprador comprador) {
        this.comprador = comprador;
    }

    public Vendedor getVendedor() {
        return vendedor;
    }

    public void setVendedor(Vendedor vendedor) {
        this.vendedor = vendedor;
    }

    public List<Produto> getProdutos() {
        return produtos;
    }

    public void setProdutos(List<Produto> produtos) {
        this.produtos = produtos;
    }

    public Venda() {
        this.produtos = new ArrayList<>();
    }

    public void addProduto(Produto produto) {
        this.produtos.add(produto);
    }

 /**
  * public void removeProduto(Produto produto) {
  *     this.produtos.remove(produto);
  }*/

    public void concretizarVenda() {
        System.out.println("Comprador: " + this.comprador.getNome());
        System.out.println("Comprou os itens: ");
        for (Produto prod : this.produtos) {
            System.out.println("Nome: " + prod.getNome() + " R$ " + prod.getPreco());
        }
        System.out.println("Vendedor: " + this.vendedor.getNome());
    }

    public void cancelarVenda() {
        System.out.println("Compra Cancelada");
    }
}
