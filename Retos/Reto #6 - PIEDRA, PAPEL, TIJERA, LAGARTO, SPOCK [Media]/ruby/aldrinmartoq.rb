# Aldrin Martoq - Reto 6
# 
# Esta implementación crea un módulo Cachipún con toda las reglas.
# El método `#partida` retorna un String con el resultado de una partida.
module Cachipún
  OPCIONES = %w[✂️ 📄 🗿 🦎 🖖]
  # mapa de qué opción le gana a cuales. Notar que gana a la siguiente y subsubsiguiente
  # https://adams.osu.edu/sites/adams/files/imce/4-H/STEM_Camp/Rock%20Paper%20Scissors%20Lizard%20Spock.pdf
  GANA = OPCIONES.each_with_index.to_h do |opción, índice|
    gana_a = OPCIONES[(índice + 1) % OPCIONES.length]
    gana_b = OPCIONES[(índice + 3) % OPCIONES.length]

    [opción, [gana_a, gana_b]]
  end

  def partida(jugadas)
    puntaje = [0, 0]
    jugadas.each do |jugada|
      if GANA[jugada[0]].include? jugada[1]     # ganó el primero
        puntaje[0] += 1
      elsif GANA[jugada[1]].include? jugada[0]  # ganó el segundo
        puntaje[1] += 1
      end
    end

    if puntaje[0] > puntaje[1]
      "Player1"
    elsif puntaje[0] < puntaje[1]
      "Player2"
    else
      "Tie"
    end
  end
end

# Ejemplo de uso
include Cachipún
puts partida [%w[🗿 ✂️], %w[✂️ 🗿], %w[📄 ✂️]]
# =>"Player2"
