with Ada.Text_IO;

procedure MiPrograma is
    -- Punto 1: Hola, mundo!
    use Ada.Text_IO;
begin
    Put_Line("Hola, mundo!");

    -- Punto 2: Crea una variable de texto o string
    Mi_Texto : String := "¡Hola desde Ada!";

    -- Punto 3: Crea una variable de número entero
    Mi_Entero : Integer := 42;

    -- Punto 4: Crea una variable de número con decimales
    Mi_Decimal : Float := 3.14;

    -- Punto 5: Crea una variable de tipo booleano
    Mi_Booleano : Boolean := True;

    -- Punto 6: Crea una constante
    Mi_Constante : constant String := "Valor constante";

    -- Punto 7: Usa un if, else if y else
    if Mi_Entero > 50 then
        Put_Line("El número es mayor que 50");
    elsif Mi_Entero < 50 then
        Put_Line("El número es menor que 50");
    else
        Put_Line("El número es igual a 50");
    end if;

    -- Punto 8: Crea un Array
    type Mi_Array is array(1..5) of Integer := (1, 2, 3, 4, 5);

    -- Punto 9: Crea una lista (Array en Ada)
    type Mi_Lista is array(1..3) of String := ("Manzana", "Banana", "Naranja");

    -- Punto 10: Crea una tupla (no aplicable en Ada)

    -- Punto 11: Crea un set (no aplicable en Ada)

    -- Punto 12: Crea un diccionario (utilizando tipos compuestos)
    type Mi_Diccionario is record
        Clave1 : String;
        Clave2 : String;
    end record;

    Dic : Mi_Diccionario := (Clave1 => "valor1", Clave2 => "valor2");

    -- Punto 13: Usa un ciclo for
    for i in 1..Mi_Array'Length loop
        Put_Line(Integer'Image(Mi_Array(i)));
    end loop;

    -- Punto 14: Usa un ciclo foreach (no aplicable en Ada)

    -- Punto 15: Usa un ciclo while
    Contador : Integer := 0;
    while Contador < 3 loop
        Put_Line("Contador: " & Integer'Image(Contador));
        Contador := Contador + 1;
    end loop;

    -- Punto 16: Crea una función sin parámetros que no retorne nada
    procedure Funcion_Sin_Parametros is
    begin
        Put_Line("Función sin parámetros");
    end Funcion_Sin_Parametros;

    -- Punto 17: Crea una función con parámetros que no retorne nada
    procedure Funcion_Con_Parametros(Param1 : Integer; Param2 : String) is
    begin
        Put_Line("Parámetro 1: " & Integer'Image(Param1));
        Put_Line("Parámetro 2: " & Param2);
    end Funcion_Con_Parametros;

    -- Punto 18: Crea una función con parámetros que retorne valor
    function Funcion_Con_Retorno(A, B : Integer) return Integer is
    begin
        return A + B;
    end Funcion_Con_Retorno;

    -- Punto 19: Crea una clase (Ada no tiene clases como en otros lenguajes, utiliza tipos y subprogramas)

    -- Punto 20: Muestra control de excepciones
    begin
        declare
            Resultado : Float := Mi_Entero / 0.0;
        begin
            null;
        exception
            when others =>
                Put_Line("Error: " & Exception_Message);
        end;
    end;
end MiPrograma;
