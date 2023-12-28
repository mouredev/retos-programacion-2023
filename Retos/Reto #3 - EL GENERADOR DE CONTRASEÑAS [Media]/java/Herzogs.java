package reto03;
public class Herzogs {
    static final String MINUSCULA="abcdefghijklmnopqrstuvwxyz";
    static final String MAYUSCULA="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    static final String SIMBOLOS = "!*{#$%&_'()*+,-./:;<=>?@";

    static class Config {
        public Integer tam;
        public Boolean min;
        public Boolean may;
        public Boolean num;
        public Boolean sim;

        public Config(Integer tam, Boolean min, Boolean may, Boolean num, Boolean sim) {
            this.tam = (tam >= 8 && tam <=16)? tam :8;
            if(min.equals(false) && may.equals(false)&& num.equals(false) && sim.equals(false)){
                this.min = this.may = this.sim = this.num = true;
            }else {
                this.min = min;
                this.may = may;
                this.num = num;
                this.sim = sim;
            }
        }

        public Config() {
            this(8,true,true,true,true);
        }
    }

    private static Integer obtenerNumeroAleatorio(Integer tam){
        return (int) (Math.random() * tam);
    }

    private static String generatePassword (Config con){
        String ps = "";
        Boolean finished = false;
        Integer val = 0;
        while(!finished){
            switch (Herzogs.obtenerNumeroAleatorio(con.tam)){
                case 0:
                    if(con.min) {
                        ps = ps.concat(String.valueOf(Herzogs.MINUSCULA.charAt(obtenerNumeroAleatorio(Herzogs.MINUSCULA.length()))));
                        val ++;
                    }
                    break;
                case 1:
                    if (con.may) {
                        ps = ps.concat(String.valueOf(Herzogs.MAYUSCULA.charAt(obtenerNumeroAleatorio(Herzogs.MAYUSCULA.length()))));
                        val++;
                    }
                    break;
                case 2:
                    if (con.num) {
                        ps = ps.concat(Integer.toString(obtenerNumeroAleatorio(10)));
                        val++;
                    }
                    break;
                case 3:
                    if(con.sim) {
                        ps = ps.concat(String.valueOf(Herzogs.SIMBOLOS.charAt(obtenerNumeroAleatorio(Herzogs.SIMBOLOS.length()))));
                        val++;
                    }
                    break;
            }
            if (val.equals(con.tam))
                finished = true;
        }
        return ps;
    }

    public static void main(String[] args) {
        //CONFIGURACIÓN POR DEFECTO
        Herzogs.Config ctxPorDefecto = new Config();
        //CONFIGURACIÓN PERSONALIZADA
        Herzogs.Config ctxPersonalizado = new Config(3,true,false,true,false);
        System.out.println("PASSWORD GENERADO CON CONTEXTO POR DEFECTO [" + Herzogs.generatePassword(ctxPorDefecto) + "]");
        System.out.println("PASSWORD GENERADO CON CONTEXTO PERSONALIZADO [" + Herzogs.generatePassword(ctxPersonalizado) + "]");
    }
}
