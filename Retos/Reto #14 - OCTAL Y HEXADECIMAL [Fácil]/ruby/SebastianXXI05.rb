=begin 
* Crea una función que reciba un número decimal y lo trasforme a Octal y Hexadecimal.
* - No está permitido usar funciones propias del lenguaje de programación que
* realicen esas operaciones directamente.
=end

# conversión de decimal a hexadecimal
BASEHEX = 16
BASE_OCTAL = 8 

def hexadecimal(decimal)
  positivo = if decimal < 0 then false else true end
  decimal = decimal.abs
  resultado = ''
  letras = ['A', 'B', 'C', 'D', 'E', 'F']

  if decimal.integer?
    if decimal <= BASEHEX
      if decimal == BASEHEX
        resultado = 1
      elsif decimal > 9
        resultado = letras[decimal%10]
      else
        resultado = decimal 
      end
    else
      while decimal != 0
        residuo = decimal % BASEHEX
        if residuo > 9
          resultado += letras[residuo%10]
        else
          resultado += residuo.to_s
        end
        decimal /= BASEHEX
      end
    resultado = resultado.reverse
    end
  else
    corte = decimal.to_s.split('.')
    numeroEntero = corte[0].to_i
    numeroDecimal = ('0.'+corte[1]).to_f
    
    if numeroEntero <= BASEHEX
      if numeroEntero == BASEHEX
        numeroEntero = '1'
      elsif numeroEntero > 9
        resultado = letras[numeroEntero%10]
      else
        resultado += numeroEntero.to_s 
      end
    else
      while numeroEntero != 0
        residuo = numeroEntero % BASEHEX
        if residuo > 9
          resultado += letras[residuo%10]
        else
          resultado += residuo.to_s
        end
        numeroEntero /= BASEHEX
      end
    end
    resultado = resultado.reverse
    resultado += '.'

    for i in 1..5 do
      numeroDecimal *= BASEHEX
      c = numeroDecimal.to_s.split('.')
      
      if c[0].to_i > 9
        resultado += letras[(c[0].to_i)%10]
      else
        resultado += c[0]
      end
      
      numeroDecimal = ('0.'+c[1]).to_f
    end
  end
  if positivo
    return resultado
  else
    return '-'+resultado.to_s
  end
end

# conversión de decimal a octal
def octal(decimal)
  positivo = if decimal < 0 then false else true end
  corte = decimal.to_s.split('.')
  numeroEntero = corte[0].to_i.abs
  numeroDecimal = if corte.length == 2 then ('0.'+corte[1]).to_f else nil end
  resultado = ''

  while numeroEntero > 0
    residuo = numeroEntero%BASE_OCTAL
    resultado += residuo.to_s 

    numeroEntero /= BASE_OCTAL
  end
  resultado = resultado.reverse

  if !numeroDecimal.nil?
    resultado += '.'
    for i in 1..5 do
      numeroDecimal *= BASE_OCTAL
      c = numeroDecimal.to_s.split('.')
      resultado += c[0]

      if c[1].to_i == 0
        break
      end
      numeroDecimal = ('0.'+c[1]).to_f
    end
  end

  if positivo
    return resultado
  else
    return '-'+resultado
  end
end

# Solución
def solucion(decimal)
  puts "Decimal: #{decimal}. Hexadecimal: #{hexadecimal(decimal)}. Octal: #{octal(decimal)}" 
end

# casos de prueba
=begin
solucion(23.55) # Decimal: 23.55. Hexadecimal: 17.8CCCC. Octal: 27.43146
solucion(-782) # Decimal: -782. Hexadecimal: -30E. Octal: -1416
solucion(3.3) # Decimal: 3.3. Hexadecimal: 3.4CCCC. Octal: 3.23146
=end