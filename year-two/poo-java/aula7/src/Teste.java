// Em uma classe de Teste, no método main, crie um objeto da classe Produto, atribua valores e teste os métodos criados.

public class Teste {
    public static void main(String[] args) {
        Produto produto1 = new Produto("Laptop", 1500.00, 5);
        produto1.exibitInformation();
        double totalValue = produto1.calculateTotalValue();
        System.out.println("Total Value: " + totalValue);
    }
}