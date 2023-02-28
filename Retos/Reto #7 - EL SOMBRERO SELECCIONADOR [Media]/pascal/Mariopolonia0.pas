program Mariopolonia0;

var 
    respuesta: array[1..4] of integer;
    contador: integer; 
    select: integer;
    mayor: integer;
    positionMayor: integer;

begin
    contador := 0;
    select := 0;
     
    for contador:= 0 to 3 do
        respuesta[contador] := 0;
        
    writeln('');  
    writeln('EL SOMBRERO SELECCIONADOR');
    
    writeln(''); 
    writeln('¿Qué color le gusta mas?'); 
    writeln('1.Rojo'); 
    writeln('2.Verde'); 
    writeln('3.Amarillo'); 
    writeln('4.Azul'); 
    
    write('Seleccione una opcion del 1 al 4 :');
    readLn(select);
    
    case select of
        1: begin
            respuesta[0] := respuesta[0] + 1;
        end;
        
        2: begin
            respuesta[1] := respuesta[1] + 1;
        end;
        
        3: begin
            respuesta[2] := respuesta[2] + 1;
        end;
        
        4: begin
            respuesta[3] := respuesta[3] + 1;
        end;
        
        Else Begin
			    WriteLn('no selecciono una respuesta correcta');
		    End;
	  End;	
    
    writeln('');
    writeln('¿Qué animal le gusta mas'); 
    writeln('1.Leon'); 
    writeln('2.Serpiente'); 
    writeln('3.Tejón'); 
    writeln('4.Aguila'); 
    
    write('Seleccione una opcion del 1 al 4 :');
    readLn(select);
    
    case select of
        1: begin
            respuesta[0] := respuesta[0] + 1;
        end;
        
        2: begin
            respuesta[1] := respuesta[1] + 1;
        end;
        
        3: begin
            respuesta[2] := respuesta[2] + 1;
        end;
        
        4: begin
            respuesta[3] := respuesta[3] + 1;
        end;
        
        Else Begin
			    WriteLn('no selecciono una respuesta correcta');
		    End;
	  End;	
    
    writeln('');
    writeln('¿Qué mago le gusta mas?'); 
    writeln('1.Hermione Granger'); 
    writeln('2.Draco Malfoy'); 
    writeln('3.Nymphadora Tonks'); 
    writeln('4.Luna Lovegood'); 
    
    write('Seleccione una opcion del 1 al 4 :');
    readLn(select);
    
    case select of
        1: begin
            respuesta[0] := respuesta[0] + 1;
        end;
        
        2: begin
            respuesta[1] := respuesta[1] + 1;
        end;
        
        3: begin
            respuesta[2] := respuesta[2] + 1;
        end;
        
        4: begin
            respuesta[3] := respuesta[3] + 1;
        end;
        
        Else Begin
			    WriteLn('no selecciono una respuesta correcta');
		    End;
	  End;
    
    writeln('');
    writeln('¿Qué especialidad lo indentifica mas?'); 
    writeln('1.Fuerza'); 
    writeln('2.Determinacion'); 
    writeln('3.Lealtad'); 
    writeln('4.Erudicion'); 
    
    write('Seleccione una opcion del 1 al 4 :');
    readLn(select);
    
    case select of
        1: begin
            respuesta[0] := respuesta[0] + 1;
        end;
        
        2: begin
            respuesta[1] := respuesta[1] + 1;
        end;
        
        3: begin
            respuesta[2] := respuesta[2] + 1;
        end;
        
        4: begin
            respuesta[3] := respuesta[3] + 1;
        end;
        
        Else Begin
			    WriteLn('no selecciono una respuesta correcta');
		    End;
	  End;
    
    writeln('');
    writeln('¿A que le das mas valor?'); 
    writeln('1.lealtad'); 
    writeln('2.ambicion'); 
    writeln('3.honor'); 
    writeln('4.valentia'); 
    
    write('Seleccione una opcion del 1 al 4 :');
    readLn(select);
    
    case select of
        1: begin
            respuesta[0] := respuesta[0] + 1;
        end;
        
        2: begin
            respuesta[1] := respuesta[1] + 1;
        end;
        
        3: begin
            respuesta[2] := respuesta[2] + 1;
        end;
        
        4: begin
            respuesta[3] := respuesta[3] + 1;
        end;
        
        Else Begin
			    WriteLn('no selecciono una respuesta correcta');
		    End;
    End;
	
	  mayor := 0;
    positionMayor := 0;
    
    (* ESTE FOR CALCULA EL MAYOR DE LAS OPCIONES *)
    for contador:= 0 to 3 do
    begin
        (* ESTE IF SELECCIONA EL MAYOR  *)
        (* Y ASIGNA LOS VALORES A LAS VAIRABLE *)
        if respuesta[contador] > mayor then
        begin
            mayor := respuesta[contador];
            positionMayor := contador;
        end;
    end;
    
 
    WriteLn('');
    WriteLn('');
    
    (*  AQUI SE DECIDE CUAL ES TU CASA *)
    case positionMayor of 
        0: begin
            WriteLn('Tu casa es la Gryffindor');
        end;
        
        1: begin
            WriteLn('Tu casa es la Slytherin');
        end;
        
        2: begin
            WriteLn('Tu casa es la Hufflepuff');
        end;
        
        3: begin
            WriteLn('Tu casa es la Ravenclaw');
        end;
	End;

End.
