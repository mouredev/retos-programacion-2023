# Aldrin Martoq - Reto 2
# 
# Esta implementación crea una clase Tenis con toda la lógica y datos de puntuación.
# El método `Tenis#puntuar` retorna un string con el resultado de un punto ganado por jugador.
# El método `Tenis#terminado?` permite determinar si el partido ya terminó.
class Tenis
  PUNTUACIÓN = %w[Love 15 30 40]
  JUGADORES = %w[P1 P2]

  def initialize
    @puntajes = JUGADORES.to_h { |jugador| [jugador, 0] }
  end

  def puntuar(jugador)
    return "Jugador `#{jugador}` inválido, ingrese: #{JUGADORES.join(' ó ')}" unless (@puntajes[jugador])

    @puntajes[jugador] += 1

    max = @puntajes.values.max
    min = @puntajes.values.min
    fin   = @puntajes.values.any? { |puntaje| puntaje >= PUNTUACIÓN.count }         # si alguno supera los 40 pts
    fin ||= @puntajes.values.all? { |puntaje| puntaje >= (PUNTUACIÓN.count - 1) }   # si ambos llegan a 40 pts

    if fin
      @puntajes.map do |jugador, puntaje|
        return "Ha ganado el #{jugador}"  if puntaje - min >= 2 && (@terminado = true)
        return "Ventaja #{jugador}"       if puntaje - min >= 1
        return "Deuce"                    if puntaje == max
      end
    else
      @puntajes.values.map { |puntaje| PUNTUACIÓN[puntaje] }.join(' - ')
    end
  end

  def terminado? = @terminado
end

# Ejemplos de Uso
tenis = Tenis.new
%w[P1 P1 P2 P2 P1 P2 P1 P1].each do |jugador|
  puts tenis.puntuar(jugador)
end

puts "\nEL PARTIDO DE TENIS\n"
tenis = Tenis.new
until tenis.terminado?
  print 'Ingrese jugador: '
  puts tenis.puntuar(gets.chomp)
end
