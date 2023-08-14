package br.com.rabelo;

import br.com.rabelo.dao.ClienteMapDAO;
import br.com.rabelo.dao.IClienteDAO;
import br.com.rabelo.domain.Cliente;

import javax.swing.*;

public class App {

    private static IClienteDAO iClienteDAO;

    public static void main(String[] args) {

        iClienteDAO = new ClienteMapDAO();
        String opcao = painelMenu();

        while (isOpcaoValido(opcao)) {
            if ("".equals(opcao)) {
                sair();
                System.exit(0);
            }

            if ("1".equals(opcao)) {
                String dados = JOptionPane.showInputDialog(null, "Digite os dados do " +
                                "Cliente separados por (,) conforme o Exemplo:\n" +
                                "Nome,CPF,Telefone,Endereço,Numero,Cidade,Estado", "Cadastrando",
                        JOptionPane.INFORMATION_MESSAGE);
                cadastrar(dados);
            } else if ("2".equals(opcao)) {
                String dados = JOptionPane.showInputDialog(null, "Digite o CPF do cliente",
                        "Cadastrando", JOptionPane.INFORMATION_MESSAGE);
                consultar(dados);

            } else if ("3".equals(opcao)) {
                String dados = JOptionPane.showInputDialog(null, "Digite o CPF do cliente",
                        "Excluindo", JOptionPane.INFORMATION_MESSAGE);
                excluir(dados);
            } else if ("4".equals(opcao)) {
                String dados = JOptionPane.showInputDialog(null, "Digite o CPF do cliente",
                        "Excluindo", JOptionPane.INFORMATION_MESSAGE);
                alterar(dados);
            } else if ("5".equals(opcao)) {
                sair();
            }
            opcao = painelMenu();
        }

    }

    private static void alterar(String dados) {
        boolean isExcluir = consultar(dados);
        if (isExcluir) {
            Cliente cliente = iClienteDAO.consultar(Long.parseLong(dados));

            dados = JOptionPane.showInputDialog(null, "NÃO PODE ALTERAR O CPF\nDigite os dados do " +
                            "Cliente separados por (,) conforme o Exemplo:\n" +
                            "Nome,CPF,Telefone,Endereço,Numero,Cidade,Estado", "Cadastrando",
                    JOptionPane.INFORMATION_MESSAGE);
            JOptionPane.showMessageDialog(null, "Cliente Alterado", "Alteração", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(null, "Erro ao Alterar Cliente", "ERRO!!!", JOptionPane.INFORMATION_MESSAGE);
        }
    }
    private static void excluir(String dados) {
        boolean isExcluir = consultar(dados);
        iClienteDAO.excluir(Long.parseLong(dados));
        if (isExcluir) {
            JOptionPane.showMessageDialog(null, "Cliente Excluido", "Excluir", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(null, "Erro ao Excluir Cliente", "ERRO!!!", JOptionPane.INFORMATION_MESSAGE);
        }
    }
    private static boolean consultar(String dados) {
        Cliente cliente = iClienteDAO.consultar(Long.parseLong(dados));
        if (cliente != null) {
            JOptionPane.showMessageDialog(null, "CLIENTE Encontrado: \n" + cliente.toString(), "Consulta", JOptionPane.INFORMATION_MESSAGE);
            return true;
        } else {
            JOptionPane.showMessageDialog(null, "CLIENTE NÃO ENCONTRADO: ", "Consulta", JOptionPane.INFORMATION_MESSAGE);
            return false;
        }
    }
    private static void cadastrar(String dados) {
        String[] dadosSeparados = dados.split(",");
        if (dadosSeparados.length != 7) {
            JOptionPane.showMessageDialog(null, "Falta dados", "Cadastro", JOptionPane.INFORMATION_MESSAGE);
            return;
        }
       for (String campo : dadosSeparados) {
            if (campo == null || campo == ""){
                JOptionPane.showMessageDialog(null, "Dados Invalidos", "Cadastro", JOptionPane.INFORMATION_MESSAGE);
                return;
            }
        }
        Cliente cliente = new Cliente(dadosSeparados[0], dadosSeparados[1], dadosSeparados[2], dadosSeparados[3],
                dadosSeparados[4], dadosSeparados[5], dadosSeparados[6]);
        Boolean isCadastrado = iClienteDAO.cadastrar(cliente);
        if (isCadastrado) {
            JOptionPane.showMessageDialog(null, "Cadastrado", "Cadastro", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(null, "Erro ao cadastrar Cliente", "ERRO!!!", JOptionPane.INFORMATION_MESSAGE);
        }
    }
    private static void sair() {
        JOptionPane.showMessageDialog(null, "Ate logo....", "Exit", JOptionPane.INFORMATION_MESSAGE);
        System.exit(0);
    }
    private static String painelMenu(){
        String opcao = JOptionPane.showInputDialog(null, "\nDigite \n1 - Cadastrar" +
                        " | 2 - Consultar \n3 - Exclusão | 4 - Alteração \n5 - Sair", "Cadastro",
                JOptionPane.INFORMATION_MESSAGE);
        return opcao;
    }
    private static boolean isOpcaoValido(String opcao) {
        if ("1".equals(opcao) || "2".equals(opcao) || "3".equals(opcao) || "4".equals(opcao) ||
                "5".equals(opcao)) {
            JOptionPane.showMessageDialog(null,"Opção Valida");
            return true;
        }
        JOptionPane.showMessageDialog(null,"Opção Não Valida");
        return false;
    }
}