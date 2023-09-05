Program Reto35;
Uses sysutils;

{Declaracion de constantes}
Const
    NUMERO = 5;
    
{Declaracion de variables}
Type
    tipoString=string[30];
    chr=char;
    int=integer;
    tipoFlotante=Real;
    bol=boolean;
    Dias_semana=(Lunes,Martes,Miercoles,Jueves,Viernes,Sabado,Domingo);
    arr = array[1..10] of integer;

Var
    nombre:tipoString;
    caracter:chr;
    entero:int;
    estatura:tipoFlotante;
    boleano:bol;
    arreglo:arr;
    i:byte;
    dias:Dias_semana;
    a:int;
    b:int;

{Usando Funciones}
procedure PrintAnInteger();
begin
    WriteLn('Este es un entero impreso desde una funcion: ', b);
end;

function triple(const x: integer): integer;
begin
    b := x * 3;
    WriteLn('El triple del numero anterior es: ', b); 
end;

begin
    {Haz un "Hola, mundo!"}
    WriteLn('Hola desde Pascal!');

    WriteLn('Esto es una constante ', NUMERO);
    
    caracter := 'c';
    WriteLn('Esto es un char ', caracter);

    entero := 5;
    WriteLn('Esto es un integer ', entero);
   
    boleano := false;
    WriteLn('Esto es un boolean ', boleano);

    nombre := 'Alejandro';
    WriteLn('Esto es un string ', nombre);

    estatura := 1.74;
    WriteLn('Esto es un flotante (decimal) ', estatura);

    {Declaracion de IF}
    a := 1;
    b := 5;
    if a > b then
	WriteLn('"a" es MAYOR que "b"')
    else
	WriteLn('"a" es MENOR que "b"');

    {Estructura Array}
    arreglo[0] := 30;
    arreglo[1] := 100;
    arreglo[2] := 50;
    arreglo[3] := 80;
    arreglo[4] := 10;
    arreglo[5] := 20;
    arreglo[6] := 90;
    arreglo[7] := 40;
    arreglo[8] := 70;
    arreglo[9] := 60;
    arreglo[10] := 0;
    WriteLn('Estas accediendo a la posicion 5 = ', arreglo[5]);

    {Uso de ciclo For}
    for i:=1 to 7 do
    begin
	case dias of
	    Lunes:WriteLn('Lunes');
	    Martes:WriteLn('Martes');
	    Miercoles:WriteLn('Miercoles');
	    Jueves:WriteLn('Jueves');
	    Viernes:WriteLn('Viernes');
	    Sabado:WriteLn('Saabado');
	    Domingo:WriteLn('Domingo');
	end;
	dias:=succ(dias)
    end;

    {Uso de ciclo While}
    while a <> b do
	begin
	    WriteLn('Esperando');
	    a := a + 1;
	end;

    {Funcion sin parametros}
    PrintAnInteger();

    {Funcion con parametros}
    triple(b);

    try
    	WriteLn('Operacion que puede generar una Excepción');
    except
   	on E:EDivByZero do Writeln(E.Message);
   	on E:EInvalidOp do Writeln(E.Message);
	on E: Exception do Writeln(E.classname,'::',E.Message);
    end;

    {
     Esto genera las siguiente salidas:

	Hola desde Pascal!
	Esto es una constante 5
	Esto es un char c
	Esto es un integer 5
	Esto es un boolean FALSE
	Esto es un string Alejandro
	Esto es un flotante (decimal)  1.7400000000000000E+000
	"a" es MENOR que "b"
	Estas accediendo a la posicion 5 = 20
	Lunes
	Martes
	Miercoles
	Jueves
	Viernes
	Saabado
	Domingo
	Esperando
	Esperando
	Esperando
	Esperando
	Este es un entero impreso desde una funcion: 5
	El triple del numero anterior es: 15
    }

end.
