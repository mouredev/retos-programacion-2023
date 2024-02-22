#!/usr/bin/python3

"""
# Reto #13: Adivina la palabra
/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


LIST_PALABRAS = ['ellos', 'tener', 'desde', 'caliente', 'palabra', 'algunos', 'usted', 'tenido', 'fuera', 'otros', 'hacer', 'tiempo', 'lo hará', 'dicho', 'decir', 'conjunto', 'querer', 'también', 'jugar', 'pequeño', 'poner', 'puerto', 'grande', 'deletrear', 'añadir', 'incluso', 'tierra', 'grande', 'por qué', 'preguntar', 'hombres', 'cambio', 'se fue', 'fuera', 'necesitará', 'imagen', 'tratar', 'nosotros', 'de nuevo', 'animal', 'punto', 'madre', 'mundo', 'cerca', 'construir', 'tierra', 'padre', 'cualquier', 'nuevo', 'trabajo', 'parte', 'tomar', 'conseguir', 'lugar', 'hecho', 'vivir', 'donde', 'después', 'espalda', 'ronda', 'hombre', 'buena', 'nuestro', 'nombre', 'a través de', 'forma', 'frase', 'pensar', 'decir', 'ayudar', 'línea', 'ser distinto', 'a su vez,', 'causa', 'mucho', 'significará', 'antes', 'movimiento', 'derecho', 'viejo', 'demasiado', 'misma', 'cuando', 'hasta', 'camino', 'acerca', 'muchos', 'entonces', 'ellos', 'escribir', 'haría', 'éstos', 'largo', 'hacer', 'tiene', 'buscar', 'podía', 'venir', 'número', 'sonar', 'personas', 'sobre', 'saber', 'llamada', 'primero', 'puede', 'abajo', 'estado', 'ahora', 'encontrar', 'cabeza', 'de pie', 'propio', 'página', 'debería', 'encontrado', 'respuesta', 'escuela', 'crecer', 'estudio', 'todavía', 'aprender', 'planta', 'cubierta', 'alimentos', 'cuatro', 'entre', 'estado', 'mantener', 'nunca', 'último', 'dejar', 'pensado', 'ciudad', 'árbol', 'cruzar', 'granja', 'inicio', 'podría', 'historia', 'sierra', 'ahora', 'dibujar', 'izquierda', 'tarde', 'ejecutar', 'mientras', 'prensa', 'Cerrar', 'noche', 'reales', 'pocos', 'norte', 'libro', 'llevar', 'ciencia', 'comer', 'habitación', 'amigo', 'comenzó', 'gusta', 'peces', 'montaña', 'Deténgase', 'una vez', 'base de', 'escuchar', 'caballo', 'cortada', 'seguro', 'colores', 'madera', 'principal', 'abierta', 'parecer', 'juntos', 'próximo', 'blanco', 'niños', 'comenzar', 'conseguido', 'caminar', 'ejemplo', 'aliviar', 'papel', 'grupo', 'siempre', 'música', 'ambos', 'marca', 'menudo', 'carta', 'hasta', 'milla', 'coche', 'cuidado', 'segundo', 'suficiente', 'llano', 'chica', 'habitual', 'joven', 'listo', 'por encima de', 'nunca', 'lista', 'aunque', 'sentir', 'charla', 'pájaro', 'pronto', 'cuerpo', 'perro', 'familia', 'directa', 'plantear', 'dejar', 'canción', 'medir', 'puerta', 'producto', 'negro', 'corto', 'numeral', 'clase', 'viento', 'pregunta', 'suceder', 'completo', 'buque', 'medio', 'orden', 'fuego', 'problema', 'pieza', 'dicho', 'sabía', 'pasar', 'desde', 'calle', 'pulgadas', 'multiplicar', 'curso', 'quedarse', 'rueda', 'completo', 'fuerza', 'objeto', 'decidir', 'superficie', 'profunda', 'sistema', 'ocupado', 'prueba', 'registro', 'barco', 'común', 'posible', 'plano', 'lugar', 'maravilla', 'corrió', 'comprobar', 'juego', 'forma', 'equiparar', 'caliente', 'señorita', 'traído', 'calor', 'nieve', 'neumáticos', 'traer', 'distante', 'llenar', 'al este', 'pintar', 'idioma', 'entre', 'unidad', 'potencia', 'ciudad', 'cierto', 'volar', 'conducir', 'grito', 'oscuro', 'máquina', 'espere', 'plan de', 'figura', 'estrella', 'sustantivo', 'campo', 'resto', 'correcta', 'capaz', 'libra', 'hecho', 'belleza', 'unidad', 'destacado', 'contener', 'delante', 'enseñar', 'semana', 'último', 'verde', 'rápido', 'desarrollar', 'océano', 'caliente', 'libre', 'minuto', 'fuerte', 'especial', 'mente', 'detrás', 'claro', 'Produce', 'hecho', 'espacio', 'mejor', 'horas', 'mejor', 'verdadero', 'durante', 'cinco', 'recordar', 'temprana', 'mantenga', 'oeste', 'suelo', 'interés', 'llegar', 'rápido', 'verbo', 'cantar', 'escuchar', 'viajes', 'menos', 'mañana', 'sencilla', 'varios', 'vocal', 'hacia', 'guerra', 'sentar', 'contra', 'patrón', 'lenta', 'centro', 'persona', 'dinero', 'servir', 'aparecerá', 'carretera', 'lluvia', 'regla', 'gobernar', 'Halar', 'aviso', 'energía', 'probable', 'hermano', 'huevo', 'paseo', 'celular', 'creer', 'quizás', 'recoger', 'repentina', 'contar', 'plaza', 'razón', 'longitud', 'representar', 'sujeto', 'región', 'tamaño', 'variar', 'resolver', 'hablar', 'general', 'hielo', 'materia', 'círculo', 'incluir', 'brecha', 'sílaba', 'sentido', 'corazón', 'presente', 'pesada', 'danza', 'motor', 'posición', 'brazo', 'amplio', 'materiales', 'fracción', 'bosque', 'sentarse', 'carrera', 'ventana', 'tienda', 'verano', 'sueño', 'demostrar', 'solitario', 'pierna', 'ejercicio', 'pared', 'capturas', 'monte', 'desear', 'cielo', 'bordo', 'alegría', 'invierno', 'satélite', 'escrito', 'salvaje', 'instrumento', 'guardado', 'vidrio', 'hierba', 'trabajo', 'borde', 'signo', 'visita', 'pasado', 'suave', 'diversión', 'brillante', 'tiempo', 'millones', 'soportar', 'acabado', 'feliz', 'esperanza', 'vestir', 'extraño', 'se ha ido', 'comercio', 'melodía', 'viaje', 'oficina', 'recibir', 'exacta', 'símbolo', 'morir', 'menos', 'problema', 'grito', 'excepto', 'escribió', 'semilla', 'unirse', 'sugerir', 'limpia', 'rotura', 'patio', 'aumentando', 'golpe', 'aceite', 'sangre', 'tocar', 'creció', 'ciento', 'mezclar', 'equipo', 'alambre', 'costo', 'perdido', 'marrón', 'desgaste', 'jardín', 'igual', 'enviado', 'elegir', 'encajar', 'fluir', 'justo', 'banco', 'recoger', 'guardar', 'el control', 'decimal', 'demás', 'bastante', 'rompió', 'medio', 'matar', 'momento', 'escala', 'fuerte', 'primavera', 'observar', 'recta', 'consonante', 'nación', 'diccionario', 'leche', 'velocidad', 'método', 'órgano', 'pagar', 'sección', 'vestido', 'sorpresa', 'tranquila', 'piedra', 'pequeño', 'ascenso', 'fresco', 'diseño', 'pobre', 'mucho', 'experimento', 'inferior', 'clave', 'hierro', 'palillo', 'plana', 'veinte', 'sonrisa', 'pliegue', 'agujero', 'saltar', 'pueblo', 'se reúnen', 'comprar', 'aumentar', 'resolver', 'de metal', 'empujar', 'siete', 'párrafo', 'tercero', 'deberá', 'en espera', 'describir', 'cocinero', 'ya sea', 'resultado', 'quemar', 'colina', 'seguro', 'siglo', 'considerar', 'costa', 'copia', 'frase', 'silencio', 'de altura', 'arena', 'suelo', 'rollo', 'temperatura', 'industria', 'valor', 'lucha', 'mentira', 'batir', 'excitar', 'naturales', 'vista', 'sentido', 'de capital', 'no lo hará', 'silla', 'peligro', 'fruta', 'de espesor', 'soldado', 'proceso', 'operar', 'práctica', 'separada', 'difícil', 'médico', 'por favor', 'proteger', 'mediodía', 'de cultivos', 'moderno', 'elemento', 'golpear', 'estudiante', 'esquina', 'partido', 'suministro', 'localizar', 'anillo', 'carácter', 'insecto', 'capturado', 'período', 'indicar', 'Radio', 'habló', 'átomo', 'humana', 'historia', 'efecto', 'eléctrica', 'esperar', 'hueso', 'ferrocarril', 'imaginar', 'proporcionar', 'acuerdo', 'por tanto,', 'suave', 'mujer', 'capitán', 'adivinar', 'necesario', 'agudo', 'crear', 'vecino', 'lavado', 'más bien', 'multitud', 'comparar', 'poema', 'cadena', 'campana', 'dependerá', 'carne', 'frotar', 'famoso', 'dólar', 'corriente', 'miedo', 'vista', 'delgado', 'triángulo', 'planeta', 'prisa', 'colonia', 'reloj', 'empate', 'entrar', 'importante', 'fresco', 'búsqueda', 'enviar', 'amarillo', 'pistola', 'permitir', 'print', 'muerto', 'lugar', 'desierto', 'traje', 'actual', 'ascensor', 'llegar', 'master', 'pista', 'padre', 'orilla', 'división', 'sustancia', 'favorecer', 'conectar', 'mensaje', 'pasar', 'acorde', 'grasa', 'contento', 'originales', 'cuota', 'estación', 'cobrar', 'adecuada', 'barra', 'oferta', 'segmento', 'esclavo', 'instantánea', 'mercado', 'grado', 'poblar', 'polluelo', 'querido', 'enemigo', 'responder', 'bebida', 'producirse', 'apoyo', 'discurso', 'naturaleza', 'alcance', 'vapor', 'movimiento', 'camino', 'líquido', 'significado', 'cociente', 'dientes', 'concha', 'cuello', 'oxígeno', 'azúcar', 'muerte', 'bastante', 'habilidad', 'mujeres', 'temporada', 'solución', 'plata', 'gracias', 'partido', 'sufijo', 'especialmente', 'miedo', 'enorme', 'hermana', 'acero', 'discutir', 'adelante', 'similar', 'guiar', 'experiencia', 'puntuación', 'manzana', 'comprado', 'llevado', 'pitch', 'abrigo', 'tarjeta', 'banda', 'cuerda', 'deslizamiento', 'ganar', 'soñar', 'noche', 'condición', 'pienso', 'herramienta', 'totales', 'básico', 'valle', 'doble', 'asiento', 'continuar', 'bloque', 'tabla', 'sombrero', 'vender', 'éxito', 'empresa', 'restar', 'evento', 'particular,', 'acuerdo', 'nadar', 'plazo', 'opuesta', 'esposa', 'zapato', 'hombro', 'propagación', 'organizar', 'campamento', 'inventar', 'algodón', 'nacido', 'determinar', 'cuarto de galón', 'nueve', 'camión', 'ruido', 'nivel', 'oportunidad', 'reunir', 'tienda', 'tramo', 'lanzar', 'brillo', 'propiedad', 'columna', 'molécula', 'seleccionar', 'repita', 'exigir', 'amplio', 'preparar', 'nariz', 'plurales', 'cólera', 'reclamación', 'continente']



from collections import Counter
from math import ceil, floor
from random import choice, choices, randint, shuffle
from string import ascii_lowercase
from unidecode import unidecode


def convert_ascii(cadena):
    cadena2 = "".join([ (unidecode(item) if item != "ñ" else item) for item in cadena ])
    return cadena2


def preprocesar_cadena(cadena):
    cadena = "".join([ item for item in cadena if item.isalpha() ])
    cadena = cadena.lower()
    cadena = convert_ascii(cadena)
    return cadena


class Pasapalabra: 

	def __init__(self, palabra, vidas=None, modo_vida=True):
		self._palabra = preprocesar_cadena(palabra)
		self._mascara = [False for item in palabra]
		self._modo_vida = modo_vida
		self._vidas = 0
		if vidas is None:
			self._vidas = len(self._palabra) if self._modo_vida else len(self._palabra)

	def mostrar_palabra(self, sep=""):
		for p, m in zip(self._palabra, self._mascara):
			print(p if m == True else "_", end=sep)
		print()

	def ganar(self):
		for item in self._mascara:
			if not item:
				return False
		return True

	def adivina(self, letra):
		if self._vidas == 0:
			cadena = "vidas" if self._modo_vida else "intentos"
			raise Exception(f"Has agotado el numero de {cadena}")
		letra = preprocesar_cadena(letra)
		bandera = False
		if len(letra) > 1: 
			bandera = self._adivina_palabra(letra)
		else:
			bandera = self._adivina_letra(letra)
		if self._modo_vida and bandera == False:
			self._vidas -= 1
		elif not self._modo_vida: 
			self._vidas -= 1

	def _adivina_palabra(self, letra):
		if letra == self._palabra:
			self._mascara = [ True for item in self._palabra ]
			return True
		return False

	def _adivina_letra(self, letra):
		bandera = False
		brandera_repetir = False
		for i,item in enumerate(self._palabra):
			if item == letra and self._mascara[i] == False:
				bandera = True
				self._mascara[i] = True
			if item == letra and self._mascara[i] == True and bandera == False:
				brandera_repetir = True
		if brandera_repetir:
			print("Has repetido la letra ", letra)
			return False
		return bandera

	def obtener_vidas(self):
		return self._vidas

	def obtener_modo(self):
		return self._modo_vida



def juego(palabra, vidas=None, modo_vida=True):

	print("BIENVIENIDO al juego de ADIVINA la palabra")

	# --------------------------------------------------
	# contruimos el objeto
	# --------------------------------------------------
	
	pasapalabra = Pasapalabra(palabra, vidas, modo_vida)

	# --------------------------------------------------

	# --------------------------------------------------
	# vamos a mostrar entre el 40% y el 80% 
	# --------------------------------------------------

	set_palabra = set(palabra)
	len_set_palabra = len(set_palabra)

	lim_in = int(ceil(len_set_palabra * 0.4))
	lim_su = int(floor(len_set_palabra * 0.8))
	rand_limite = randint(lim_in, lim_su)

	lista_letras_mostrar = list(set_palabra) 
	shuffle(lista_letras_mostrar)
	lista_letras_mostrar = lista_letras_mostrar[rand_limite:]

	for item in lista_letras_mostrar:
		pasapalabra.adivina(item)
	
	# --------------------------------------------------
	
	# --------------------------------------------------
	# main loop
	# --------------------------------------------------

	while True:

		print()
		print("Adivina la palabra")
		print()
		pasapalabra.mostrar_palabra(sep=" ")
		print()
		vidas = pasapalabra.obtener_vidas()
		print("tienes", vidas, "vidas" if pasapalabra.obtener_modo() else "intentos")
		print("❤︎" * vidas)
		print()

		temp_palabra = input()
		pasapalabra.adivina(temp_palabra)

		if pasapalabra.ganar():
			print("FELICIDADES HAS ADIVINADO LA PALABRA")
			pasapalabra.mostrar_palabra()
			break

		if pasapalabra.obtener_vidas() == 0:
			print("LO SIENTO; NO GANASTE")
			print("la palabra era: ", palabra)
			break

	# --------------------------------------------------

if __name__ == '__main__':

	palabra = choice(LIST_PALABRAS)
	palabra = preprocesar_cadena(palabra)
	juego(palabra)
