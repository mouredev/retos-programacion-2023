program Mariopolonia0;

{
 Crea un generador de números pseudoaleatorios entre 0 y 100.
 No puedes usar ninguna función "random" (o semejante) del 
 lenguaje de programación seleccionado.
 
 Es más complicado de lo que parece...
}

//este paquete es para usar la funcion TimeToStr(Time)
uses sysutils; 

var 
    semilla : integer;
    hasta : integer;
    numero : integer;
    numeroDos : integer;
    contador : integer;
 
begin
    //StrToInt combierte un string a entero
    //El copy puede copiar desde hasta la posicion deseada
    //La funcion TimeToStr(Time) busca la hora actual
    semilla := StrToInt( Copy(TimeToStr(Time), 7, 8) );
    hasta := 0;
    numero := 0;
    numeroDos := 0;
    contador := 0;
    
    write('Cuanto número aleatorio se imprimirán:');
    readLn(hasta);
    
    while contador < hasta do 
    begin 
        numero := (5 * semilla + 7) mod 8;
        numeroDos := numero * 8;
        
        if (numeroDos > 0) and (numeroDos < 100) then
        begin
            writeln(numeroDos);
            contador := contador + 1;
        end;
        
        semilla := numero;
    end;
end.
