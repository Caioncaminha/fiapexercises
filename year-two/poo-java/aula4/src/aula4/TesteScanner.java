package aula4;

import java.util.Scanner;

public class TesteScanner {
	
	public static void main(String[] args) {
		
		Scanner entrada = new Scanner(System.in);
		
		System.out.println("Digite sua idade:");
		short idade = entrada.nextShort();
		
		entrada.nextLine();
		
		System.out.println("Digite seu nome:");
		String nome = entrada.nextLine();
		
		// System.out.println("Seu nome é: " + nome + " e idade é: " + idade);
		
		System.out.printf("Seu nome é: %s e sua idade é %d.%n", nome, idade);
		
		entrada.close();
		
	}

}
