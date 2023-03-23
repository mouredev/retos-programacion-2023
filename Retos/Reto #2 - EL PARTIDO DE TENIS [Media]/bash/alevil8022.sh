#!/usr/bin/bash
 # Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 # El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 # gane cada punto del juego.
 #
 # - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 # - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 #   15 - Love
 #   30 - Love
 #   30 - 15
 #   30 - 30
 #   40 - 30
 #   Deuce
 #   Ventaja P1
 #   Ha ganado el P1
 # - Si quieres, puedes controlar errores en la entrada de datos.
 # - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.

declare -i p
p[1]=0
p[2]=0


#declare -i p=(0 0)
declare -a puntuacion=(Love 15 30 40 ventaja ganador)
score=""

function titulo
{
	echo "#--------------------------------"
	echo " PARTIDO DE TENIS"
	echo "#--------------------------------"
}


function pantalla
{
        echo "#-----------------------------#"
        echo "  P u N T U A C I O N         "
        echo "#-----------------------------#"
        echo $mensaje
        echo "#-----------------------------#"
}


function marcador
{
		echo "Quien obtuvo el punto?"
		echo "[1] => Jugador 1"
		echo "[2] => Jugador 2"
		read -p "=> " punto
		clear
		titulo
}


function convertir
{
	if [ $punto -eq 1 ]
	then
        	punto=1
              	puntoi=2
	else
        	punto=2
        	puntoi=1
	fi


}


function marcar
{

	convertir
	p[$punto]+=1

	if [ ${p[$punto]} -eq 3 ]
	then
		if [ ${p[$puntoi]} -eq 3 ]
		then
			score="Deuce"
			mensaje="Score => Deuce"
		elif [ ${p[$puntoi]} -gt 3 ]
		then
			p[$puntoi]=3
		else
			mensaje="Score => P$punto=> ${puntuacion[${p[$punto]}]}- P$puntoi => ${puntuacion[${p[$puntoi]}]}"
		fi
	elif  [ ${p[$punto]} -gt 3 ]
	then
		if [ ${p[$punto]} -lt 5 ]
		then
			if [[ $score = "Deuce" ]]
			then
				mensaje="Ventaja para el Jugador $punto"
	                        score="ventaja"

			else
				if [[ $score = "ventaja" ]]
				then
					score="Deuce"
					p[$puntoi]=3
					p[$punto]=3
					mensaje="Score => Deuce"
				else
					mensaje="El Ganador es el Player $punto"
					ganador=1
				fi

			fi

		else
			mensaje="El Ganador es el Player $punto"
			ganador=1
		fi
	else
		mensaje="Score => P$punto => ${puntuacion[${p[$punto]}]}- P$puntoi => ${puntuacion[${p[$puntoi]}]}"
	fi

}



clear
titulo
ganador=0
while [ $ganador -ne 1 ]
do
	marcador
	marcar
	pantalla
done
