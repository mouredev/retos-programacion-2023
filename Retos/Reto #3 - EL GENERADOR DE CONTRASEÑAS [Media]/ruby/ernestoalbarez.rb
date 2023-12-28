def generar_contrasena(longitud, mayusculas=true, numeros=true, simbolos=true)
  cadena = ('a'..'z').to_a
  cadena += ('A'..'Z').to_a if mayusculas
  cadena += ('0'..'9').to_a if numeros
  cadena += %w[! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . / ?] if simbolos
  
  raise ArgumentError, "La longitud debe estar entre 8 y 16." if longitud < 8 || longitud > 16
  
  contrasena = Array.new(longitud) { cadena.sample }.join
end
  
if __FILE__ == $0
  begin
    print "Ingrese la longitud deseada para la contraseña (entre 8 y 16): "
    longitud = gets.chomp.to_i
    
    print "Incluir letras mayúsculas (Sí/No): "
    mayusculas = gets.chomp.strip.downcase == 'si'
    
    print "Incluir números (Sí/No): "
    numeros = gets.chomp.strip.downcase == 'si'
    
    print "Incluir símbolos (Sí/No): "
    simbolos = gets.chomp.strip.downcase == 'si'
  
    contrasena_generada = generar_contrasena(longitud, mayusculas, numeros, simbolos)
    puts "Contraseña generada: #{contrasena_generada}"

  rescue ArgumentError => e
      puts "Error: #{e.message}"
  end
end
  