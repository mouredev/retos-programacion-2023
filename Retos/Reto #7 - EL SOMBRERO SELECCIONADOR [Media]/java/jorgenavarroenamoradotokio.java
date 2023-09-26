package com.retos.ej07;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Map;
import java.util.Scanner;
import java.util.function.Function;
import java.util.stream.Collectors;


public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {

		// Creamos las preguntas
		jorgenavarroenamoradotokio examen = new jorgenavarroenamoradotokio();
		jorgenavarroenamoradotokio.Pregunta p1 = examen.new Pregunta("¿Cómo te definirías?");
		jorgenavarroenamoradotokio.Pregunta p2 = examen.new Pregunta("¿Cuál es tu clase favorita?");
		jorgenavarroenamoradotokio.Pregunta p3 = examen.new Pregunta("¿Dónde pasarías más tiempo?");
		jorgenavarroenamoradotokio.Pregunta p4 = examen.new Pregunta("¿Cuál es tu color favorito?");
		jorgenavarroenamoradotokio.Pregunta p5 = examen.new Pregunta("¿Cuál es tu mascota?");
		
		// Almacenamos las preguntas en un listado
		Collection<Pregunta> preguntas = new ArrayList<>();
		preguntas.add(p1);
		preguntas.add(p2);
		preguntas.add(p3);
		preguntas.add(p4);
		preguntas.add(p5);
		
		// Agregamos las respuesta de cada pregunta
		p1.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.GRYFFINDOR.valor, "1. Valiente"));
		p1.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.HUFFLEPUFF.valor, "2. Leal"));
		p1.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.RAVENCLAW.valor, "3. Sabio"));
		p1.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.SLYTHERIN.valor, "4. Ambicioso"));
		
		p2.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.GRYFFINDOR.valor, "1. Vuelo"));
		p2.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.RAVENCLAW.valor, "2. Posciones"));
		p2.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.SLYTHERIN.valor, "3. Animales fantásticos"));
		p2.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.HUFFLEPUFF.valor, "4. Defensa contra las artes oscuras"));
		
		p3.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.HUFFLEPUFF.valor, "1. Invernadero"));
		p3.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.RAVENCLAW.valor, "2. Biblioteca"));
		p3.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.SLYTHERIN.valor, "3. En la sala común"));
		p3.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.GRYFFINDOR.valor, "4. Explorando"));
		
		p4.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.GRYFFINDOR.valor, "1. Rojo"));
		p4.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.RAVENCLAW.valor, "2. Azul"));
		p4.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.SLYTHERIN.valor, "3. Verde"));
		p4.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.HUFFLEPUFF.valor, "4. Amarillo"));
		
		p5.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.GRYFFINDOR.valor, "1. Lechuza"));
		p5.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.RAVENCLAW.valor, "2. Sapo"));
		p5.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.HUFFLEPUFF.valor, "3. Gato"));
		p5.agregarRespuesta(examen.new Respuesta(CasaHarryPotter.SLYTHERIN.valor, "4. Serpiente"));
		
		
		// Alamcenamos las opciones marcadas
		Collection<Integer> opcionesMarcadas = new ArrayList<Integer>();
		Scanner sc = new Scanner(System.in);
		for (Pregunta pregunta : preguntas) {
			System.out.println(pregunta.getEnuncionado());
			for (Respuesta respuesta : pregunta.getRespuestas()) {
				System.out.println("\t" + respuesta.getDescripcion());	
			}
			
			int opcion = Integer.parseInt(sc.nextLine());
			opcionesMarcadas.add(opcion);
		}
		sc.close();
		
		// Almacenamos el numero de veces que se ha marcada cada opcion
		Map<Integer, Long> frecuenciaMap = opcionesMarcadas.stream()
				.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

		// Encontramos la entrada con el valor máximo de frecuencia
		Map.Entry<Integer, Long> maxEntry = frecuenciaMap.entrySet().stream().max(Map.Entry.comparingByValue())
				.orElseThrow();

		// Visualizamos la casa a la que corresponde
		CasaHarryPotter c = null;
		for (CasaHarryPotter casa : CasaHarryPotter.values()) {
			if (casa.getValor() == maxEntry.getKey()) {
				c = casa;
				break;
			}
		}

		System.out.println(c.nombre);

	}
	
	enum CasaHarryPotter {
		GRYFFINDOR("Gryffindor", "Valentía, coraje y determinación", 1),
		HUFFLEPUFF("Hufflepuff", "Lealtad, paciencia y trabajo duro", 2),
		RAVENCLAW("Ravenclaw", "Inteligencia, creatividad y sabiduría", 3),
		SLYTHERIN("Slytherin", "Astucia, ambición y determinación", 4);

		private String nombre;
		private String descripcion;
		private int valor;

		CasaHarryPotter(String nombre, String descripcion, int valor) {
			this.nombre = nombre;
			this.descripcion = descripcion;
			this.valor = valor;
		}

		public String getNombre() {
			return nombre;
		}

		public String getDescripcion() {
			return descripcion;
		}

		public int getValor() {
			return valor;
		}	
	}
	
	class Respuesta {
		private int valor;
		private String descripcion;

		public Respuesta(int valor, String descripcion) {
			this.valor = valor;
			this.descripcion = descripcion;
		}

		public int getValor() {
			return valor;
		}

		public void setValor(int valor) {
			this.valor = valor;
		}

		public String getDescripcion() {
			return descripcion;
		}

		public void setDescripcion(String descripcion) {
			this.descripcion = descripcion;
		}
	}

	class Pregunta {
		private String enuncionado;
		private Collection<Respuesta> respuestas;

		Pregunta(String enunciado) {
			this.enuncionado = enunciado;
			this.respuestas = new ArrayList<>();
		}

		public String getEnuncionado() {
			return enuncionado;
		}

		public void setEnuncionado(String enuncionado) {
			this.enuncionado = enuncionado;
		}

		public Collection<Respuesta> getRespuestas() {
			return respuestas;
		}

		public void agregarRespuesta(Respuesta respuesta) {
			respuestas.add(respuesta);
		}
	}

}
