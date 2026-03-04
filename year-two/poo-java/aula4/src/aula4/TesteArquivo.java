package aula4;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;


public class TesteArquivo {

	public static void main(String[] args) throws IOException {

		PrintWriter arquivo = new PrintWriter(new FileWriter("saida.txt"));
		arquivo.println("Escrita no arquivo aaasdadsd6");
		arquivo.close();
		
	}

}
