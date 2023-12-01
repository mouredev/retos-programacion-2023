
    String pal;
    public Scanner scan = new Scanner(System.in).useDelimiter("\n");
    public Set<String> seteo;
    
    public String ingresarPalabra(){
        
        System.out.println("Ingresa la palabra para mostrar todas sus posibles permutaciones");
        return  scan.next();
    }
    
    public ArrayList<String> generarPermutaciones(String palabra) {
        ArrayList<String> permutaciones = new ArrayList<>();
        generarPermutacionesRecursivas("", palabra, permutaciones);
        return permutaciones;
    }
    private void generarPermutacionesRecursivas(String prefijo, String sufijo, ArrayList<String> permutaciones) {
        int n = sufijo.length();
        if (n == 0) {
            permutaciones.add(prefijo);
        } else {
            for (int i = 0; i < n; i++) {
                generarPermutacionesRecursivas(prefijo + sufijo.charAt(i), sufijo.substring(0, i) + sufijo.substring(i + 1), permutaciones);
            }
        }
    }
    
    public void permutar(){
        
        pal = ingresarPalabra();
        ArrayList<String> permutaciones = generarPermutaciones(pal);
        seteo = new HashSet<>(permutaciones);
        System.out.println("Permutaciones de " + pal + ":");
        for (String permutacion : seteo) {
            System.out.println(permutacion);
        }
      
     public static void main(String[] args) {
       permutar();
     }
        
    }
