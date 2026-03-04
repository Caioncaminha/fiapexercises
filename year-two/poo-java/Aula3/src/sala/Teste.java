package sala;

public class Teste {

	public static void main(String[] args) {
		
		
		Pessoa caio = new Pessoa();
		caio.nome = "Caio";
		caio.idade = 19;
		caio.sexo = "M";
		caio.altura = 1.85f;
		caio.peso = 92.2f;
		caio.comer();
		caio.estudar();
		caio.dormir();
		
		Pessoa otavio = new Pessoa();
		otavio.nome = "Otavio";
		otavio.idade = 19;
		otavio.sexo = "M";
		otavio.altura = 1.83f;
		otavio.peso = 72.2f;
		otavio.comer();
		otavio.estudar();
		otavio.dormir();
		
	}

}
