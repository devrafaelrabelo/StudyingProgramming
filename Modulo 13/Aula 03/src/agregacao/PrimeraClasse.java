package agregacao;

import agregacao.Comprador;
import agregacao.Produto;
import agregacao.Venda;
import agregacao.Vendedor;

public class PrimeraClasse {
    public static void main(String[] args) {
        Produto produtoTV = criarProduto(1L, 10000d, "TV");
        Produto produtoIphone = criarProduto(2L, 5000d, "Iphone");

        Vendedor vendedor = criarVendedor("Rafael Rabelo", 0.20d);

        Comprador comprador = criarComprador("Roger Rabelo", 200000d);


        Venda venda = new Venda();
        venda.setVendedor(vendedor);
        venda.setComprador(comprador);
        venda.addProduto(produtoIphone);
        venda.addProduto(produtoTV);

        venda.concretizarVenda();
    }

    private static Comprador criarComprador(String nome, double verba) {
        return  new Comprador(nome, verba);
    }

    private static Vendedor criarVendedor(String nome, double comissao) {
        Vendedor vendedor = new Vendedor();
        vendedor.setNome(nome);
        vendedor.setComissao(comissao);
        return vendedor;
    }

    private static Produto criarProduto(Long codigo, Double valor, String nome){
        Produto produto = new Produto();
        produto.setNome(nome);
        produto.setCodigo(codigo);
        produto.setPreco(valor);
        return produto;
    }

}
