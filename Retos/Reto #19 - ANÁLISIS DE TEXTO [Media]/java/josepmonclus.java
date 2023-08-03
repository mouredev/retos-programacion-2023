
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
public class josepmonclus {
    public static void main(String[] args) {
        String text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ac aliquam orci, sed mattis enim. "
            + "Vivamus eu volutpat mi, non euismod sapien. Aliquam et viverra dui, at tempor erat. Cras metus urna, luctus ut justo eu, "
            + "ultrices elementum odio. Aliquam ultricies sollicitudin lacinia. Pellentesque eget ante nec mi ullamcorper consequat vel "
            + "non odio. Pellentesque ornare sem feugiat condimentum mattis. Suspendisse potenti. Lorem ipsum dolor sit amet, consectetur "
            + "adipiscing elit. Nullam a urna pulvinar, dignissim magna non, lacinia est. Sed varius sed quam vitae porta. Suspendisse aliquet, "
            + "mauris quis facilisis convallis, risus nisl ullamcorper nunc, ac convallis nibh felis eu eros. Proin consectetur, sem iaculis "
            + "eleifend posuere, eros nibh ornare metus, vel elementum massa massa commodo felis. Quisque neque eros, rhoncus quis augue in, "
            + "egestas semper tortor. Proin varius lacus sapien, non luctus velit ornare id. Duis commodo quam in arcu blandit, id venenatis "
            + "enim imperdiet. Vivamus sollicitudin ligula a dolor suscipit, vel suscipit ante scelerisque. Proin a tincidunt purus, at tincidunt "
            + "odio. Donec quis porta enim. Integer sit amet metus posuere, dignissim dui in, rhoncus erat. Nam vel accumsan dolor. Nulla luctus "
            + "neque ut euismod ornare. Suspendisse potenti. Praesent non nisi tempor, cursus velit rutrum, fermentum lectus. Fusce eget elit et "
            + "orci ornare vehicula vel in nisl. Fusce a velit nisl. Duis feugiat turpis ipsum, non pellentesque odio hendrerit in. Quisque "
            + "sed erat pellentesque, auctor justo aliquam, bibendum magna. Fusce et lorem placerat, convallis libero vitae, molestie arcu. "
            + "Donec lacus turpis, sollicitudin a ultrices et, finibus eu dui. Donec ac lacus a purus dictum lobortis. Sed porttitor in ligula "
            + "eu tempor. Sed porttitor fermentum egestas. Mauris vitae mauris rutrum eros porta venenatis ac pulvinar arcu. Vivamus quis ante sem.";
        
        josepmonclus josepmonclus = new josepmonclus();
        josepmonclus.analyzeText(text);
    }

    public void analyzeText(String text) {
        int palabras = 0;
        float media = 0;
        int oraciones = 0;
        String palabraMasLarga = "";

        for(String palabra : text.split(" ")) {
            //Contador de palabras, equivalente a text.split(" ").length
            palabras++;

            //Contador de oraciones al encontrar "."
            if(palabra.endsWith(".")) oraciones++;

            //Eliminamos "." o "," a final de palabra para no tenerlo en cuenta para la media de longitud y la palabra más larga
            if(palabra.endsWith(".") || palabra.endsWith(",")) palabra = palabra.substring(0, palabra.length() - 1);

            //Media de longitud de las palabras
            media = (media + palabra.length()) / 2;

            //Palabra mas larga
            if(palabra.length() > palabraMasLarga.length()) palabraMasLarga = palabra;
        }

        System.out.println("- Número de palabras: " + palabras);
        System.out.println("- Longitud media: " + media);
        System.out.println("- Número de oraciones: " + oraciones);
        System.out.println("- Palabra más larga: " + palabraMasLarga);
    }
}
