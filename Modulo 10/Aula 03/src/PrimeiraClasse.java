import java.util.Scanner;

public class PrimeiraClasse {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Digite sua idade: ");
        int idade = s.nextInt();
        String idadeSt = idadeCase(idade);
        System.out.println(idadeSt);
    }

    public static String idadeCase(int idade){
        String result;

        switch (idade) {
            case 0:
            case 5:
                result = "Voce é bebê";
                break;
            case 6:
            case 10:
                result = "Voce é criança";
                break;
            case 11:
            case 18:
                result = "Voce é adolescente";
                break;
            default:
                result = "Voce é adulto";
                break;
        }
        return result;
    }
}
