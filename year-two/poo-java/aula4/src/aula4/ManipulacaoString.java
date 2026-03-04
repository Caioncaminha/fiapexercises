package aula4;

public class ManipulacaoString {

	public static void main(String[] args) {
		
		String descricao = "A disciplina de java é bosta, ";
		String descricao2 = "";
		
		descricao = descricao.concat("Isso Mesmo!");
		
		if(descricao.contains("java")) {
			System.out.println("tem java");
		};
		
		descricao = descricao.toUpperCase();
		
		if (descricao.equals("A disciplina de java é legal. Isso mesmo!")) {
			System.out.println("O texto é igual");
		};
		
		
		System.out.println(descricao);
	
	}

}
