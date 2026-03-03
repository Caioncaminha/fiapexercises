package sala;

public class Teste {

	public static void main(String[] args) {


		Pessoa henrique = new Pessoa();
		henrique.nome = "Henrique";
		henrique.idade = 19;
		henrique.sexo = "M";
		henrique.altura = 1.74f;
		henrique.peso = 70;
		henrique.comer();
		henrique.estudar();
		henrique.dormir();
		
		
		Pessoa otavio = new Pessoa();
		otavio.nome = "Otavio";
		otavio.idade = 19;
		otavio.sexo = "M";
		otavio.altura = 1.8f;
		otavio.peso = 70;
		otavio.comer();
		otavio.estudar();
		otavio.dormir();

	}

}
