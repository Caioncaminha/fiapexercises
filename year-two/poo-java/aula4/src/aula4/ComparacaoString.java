package aula4;

public class ComparacaoString {

	public static void main(String[] args) {
		
		String str1 = "hello";
		String str2 = "Hello";
		
		if(str1.equalsIgnoreCase(str2)) {
			System.out.println("O texto é igual!");
		} else {
			System.out.println("O texto é diferente!");
		}

	}

}
