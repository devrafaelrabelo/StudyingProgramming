package Interfaces;

public interface Icarro {
    default void andar() {
        System.out.println("Andando.");
        System.out.println("Andando..");
        System.out.println("Andando...");
        System.out.println("Andando....");
        System.out.println("Andando.....");
    }

    default void parar(){
        System.out.println("Parando.....");
        System.out.println("Parando....");
        System.out.println("Parando...");
        System.out.println("Parando..");
        System.out.println("Parando.");
        System.out.println("Parando");
    }

}
