package abstratas;

public class Assalariado extends Empregado {
       private double salario;

       @Override
       public Double vencimento() {
              return salario;
       }

       public double getSalario() {
              return salario;
       }

       public void setSalario(double salario) {
              this.salario = salario;
       }
}
