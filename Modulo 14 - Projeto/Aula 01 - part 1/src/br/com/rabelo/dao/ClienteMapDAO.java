package br.com.rabelo.dao;

import br.com.rabelo.domain.Cliente;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class ClienteMapDAO implements IClienteDAO{

    private Map<Long, Cliente> map;

    /***
     * Bloco de funções para inicialização dos metodos
     * */
    public ClienteMapDAO(){
        this.map = new HashMap<>();
    }

    /***
     * Função para cadastrar
     * */
    @Override
    public Boolean cadastrar(Cliente cliente) {
        if (this.map.containsKey(cliente.getCpf())) {
            return false;
        }
        this.map.put(cliente.getCpf(), cliente);
        return true;
    }

    /***
     * Função para Excluir
     * */
    @Override
    public void excluir(Long cpf) {
        Cliente clienteCadastrador = this.map.get(cpf);

        if (clienteCadastrador != null) {
            this.map.remove(clienteCadastrador.getCpf(), clienteCadastrador);
        }
    }

    /***
     * Função para Alterar
     * */
    @Override
    public void alterar(Cliente cliente) {
        Cliente clienteCadastrador = this.map.get(cliente.getCpf());
        if (clienteCadastrador != null); {
            clienteCadastrador.setNome(cliente.getNome());
            clienteCadastrador.setTel(cliente.getTel());
            clienteCadastrador.setNumero(cliente.getNumero());
            clienteCadastrador.setEnd(cliente.getEnd());
            clienteCadastrador.setCidade(cliente.getCidade());
            clienteCadastrador.setEstado(cliente.getEstado());
        }

    }

    /***
     * Função para Consultar
     * */
    @Override
    public Cliente consultar(Long cpf) {
        return this.map.get(cpf);
    }

    /***
     * Função para Buscar Todos
     * */
    @Override
    public Collection<Cliente> buscarTodos() {
        return this.map.values();
    }
}
