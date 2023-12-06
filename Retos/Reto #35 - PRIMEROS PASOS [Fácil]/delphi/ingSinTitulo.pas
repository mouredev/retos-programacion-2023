program DelphiExample;

{$APPTYPE CONSOLE}

uses
  SysUtils;

// Punto 1: Hola, mundo!
begin
  Writeln('Hola, mundo!');

  // Punto 2: Crea una variable de texto o string
  var miTexto: string := '¡Hola desde Delphi!';

  // Punto 3: Crea una variable de número entero
  var miEntero: Integer := 42;

  // Punto 4: Crea una variable de número con decimales
  var miDecimal: Double := 3.14;

  // Punto 5: Crea una variable de tipo booleano
  var miBooleano: Boolean := True;

  // Punto 6: Crea una constante
  const MI_CONSTANTE: Integer = 10;

  // Punto 7: Usa un if, else if y else
  if miEntero > 50 then
    Writeln('El número es mayor que 50')
  else if miEntero < 50 then
    Writeln('El número es menor que 50')
  else
    Writeln('El número es igual a 50');

  // Punto 8: Crea un Array (arreglo en Delphi)
  var miArray: array of Integer := [1, 2, 3, 4, 5];

  // Punto 9: Crea una lista (no aplicable en Delphi)

  // Punto 10: Crea una tupla (no aplicable en Delphi)

  // Punto 11: Crea un set (no aplicable en Delphi)

  // Punto 12: Crea un diccionario (no aplicable en Delphi)

  // Punto 13: Usa un ciclo for
  for var elemento in miArray do
    Writeln(elemento);

  // Punto 14: Usa un ciclo foreach (no aplicable en Delphi)

  // Punto 15: Usa un ciclo while
  var contador: Integer := 0;
  while contador < 3 do
  begin
    Writeln('Contador: ', contador);
    Inc(contador);
  end;

  // Punto 16: Crea una función sin parámetros que no retorne nada
  procedure funcionSinParametros;
  begin
    Writeln('Función sin parámetros');
  end;
  funcionSinParametros;

  // Punto 17: Crea una función con parámetros que no retorne nada
  procedure funcionConParametros(param1: Integer; param2: string);
  begin
    Writeln('Parámetro 1: ', param1);
    Writeln('Parámetro 2: ', param2);
  end;
  funcionConParametros(1, 'dos');

  // Punto 18: Crea una función con parámetros que retorne valor
  function funcionConRetorno(a, b: Integer): Integer;
  begin
    Result := a + b;
  end;
  var resultado: Integer := funcionConRetorno(3, 4);
  Writeln('Resultado: ', resultado);

  // Punto 19: Crea una clase (no aplicable en este ejemplo)

  // Punto 20: Muestra control de excepciones (try-except en Delphi)
  try
    var division: Integer := miEntero div 0;
    Writeln('Resultado de la división: ', division);
  except
    on E: Exception do
      Writeln('Error: ', E.Message);
  end;

end.
