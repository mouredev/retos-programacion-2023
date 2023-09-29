import java.util.*;

public class Alvarogtz {
    
    static Map teclado = new HashMap<>();
    
    public static void main(String args[]){
        
        Scanner sc = new Scanner(System.in);
        cargaTeclado();
        System.out.println("6-666-88-777-33-3-33-888");
        System.out.println("2-555-888-2-777-666-0-1111");
        
        System.out.println("Inserta texto T9: ");
        transformaTexto(sc.nextLine());
        //transformaTexto("2-555-888-2-777-666-0-1111");
    }

    private static void transformaTexto(String texto) {
        if(!texto.replace("-","").matches("[0-9]+")) {
            System.out.println("La cadena introducida contiene valores incorrectos");
        }else {
            String[] caracteres = texto.split("-");
            for (String caracter : caracteres) {
                System.out.print(teclado.get(Integer.parseInt(caracter)));
            }
        }
    }

    private static void cargaTeclado() {
        
        char[] caracteres = ",.?!ABCDEFGHIJKLMNOPQRSTUVWXYZ1?º".toCharArray();
        List teclas = new ArrayList();

        for(char caracter : caracteres){
            teclas.add(caracter);
        }

        teclado.put(0," ");

        for(int i = 1; i <= 9; i++) {
            for(int x = 1; x <= 4; x++){
                for (int y = 0; y <= teclas.size();y++) {
                    if(x == 4 && i!=1 && i!=7 && i!= 9)
                        break;
                    int tecla = i;
                    if(x==2)
                        tecla = i * 11;
                    else if (x==3) {
                        tecla = i * 111;
                    } else if (x==4) {
                        tecla = i * 1111;
                    }
                    teclado.put(tecla,teclas.get(y));
                    teclas.remove(y);
                    y--;
                    break;
                }
            }
        }
    }
}
