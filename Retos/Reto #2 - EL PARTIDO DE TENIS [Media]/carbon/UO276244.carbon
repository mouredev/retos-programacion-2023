package sample api;



//DOCUMENTACION DE CARBON:
//https://github.com/carbon-language/carbon-lang/blob/trunk/docs/design/README.md

//COMPILADOR web
//https://carbon.compiler-explorer.com/

//Los prints son un poco marroneros porque al parecer el compilador web de Carbon falla más que una 
//escopeta de feria, entonces no puedo concatenar para printear ni cosas similares.

fn SumPoint(currPoints : i32) -> i32{

    if(currPoints == 30){
        return currPoints + 10;
    }else{
        return currPoints + 15;
    }

}


fn PrintState(p1:i32 , p2:i32, adFor:String) -> i32{
    Print("----");
    match(adFor){

        case ("") => {

            if(p1 == 40 and p2 == 40){
                Print("DEUCE");
                
                return 1;
            }else{
                
                
                return 1;
            }

        }

        default => {

            Print("Ventaja para: ");
            Print(adFor);

            return 1;
        }

    }


}


fn Main() -> i32 {

  var p1 : i32 = 0;
  var p2 : i32 = 0;

//Tengo que hacerlo así hardcodeado porque al parecer carbon tampoco tiene nada estable para leer
//datos por consola, ni para obtener la longitud de una array (al menos que yo pudiese encontrar).
  var numPoints: i32 = 12;
  var points : [String ; 12] = ("P1", "P1", "P2", "P2", "P1", "P2", "P1","P2", "P1","P2","P2","P2");


  var pointer : i32 = 0;
  var currPoint : String = "";
  var adFor : String = "";
    while (pointer < numPoints) {

        Print("----");
        currPoint = points[pointer];
        Print(currPoint);

        if(adFor != ""){

            if(adFor == currPoint){
                break;
            }else{
                adFor="";
                Print("DEUCE");
            }
            

        }else if(p1==40 and p2==40){

            adFor = currPoint;
            Print("Ventaja para ");
            Print(adFor);

        }else{

            match(currPoint){
                case ("P1") => {
                    p1 = SumPoint(p1);
                    
                }
                case ("P2") => {
                    p2 = SumPoint(p2);
                    
                }
            }

            if(p1==40 and p2 == 40){
                Print("DEUCE");
            }else{

                Print("{0}",p1);
                Print("-");
                Print("{0}",p2);
            }

            


        }

        pointer = pointer + 1;
    }

    Print("----");

  Print("El ganador es: ");Print(adFor);
  return 1;
}
