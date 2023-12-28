# Aldrin Martoq - Reto 3
# 
# Retorna un string con una contraseña aleatoria y los parámetros indicados
def contraseña(longitud: 8, mayúsculas: false, números: false, símbolos: false)
  raise "longitud debe estar entre 8 y 16" unless longitud.between? 8, 16

  ítems = ('a'..'z').to_a
  ítems += ('A'..'Z').to_a if mayúsculas
  ítems += ('0'..'9').to_a if números
  ítems += ('!'..'/').to_a if símbolos

  longitud.times.map { ítems.sample }.join
end

# Ejemplo de uso:

puts contraseña
puts contraseña(longitud: 16, números: true)
puts contraseña(símbolos: true, mayúsculas: true)

puts contraseña(longitud: 5) #=> lanza RuntimeError
