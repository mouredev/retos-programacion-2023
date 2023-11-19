import java.util.HashMap;

public class Elez95 {

	HashMap<Integer,String> digitos_hex;

	public Elez95() {
		this.digitos_hex = getDigitosHex();

	}
	
	public String codigo_a_hex(String cod_decimal) {

		if(cod_decimal.length() != 7) {
			throw new IllegalArgumentException("El código rgb tiene que ser del tipo #000000");
		}else {

			String red_dec   = cod_decimal.substring(1,3);
			String green_dec = cod_decimal.substring(3,5);
			String blue_dec  = cod_decimal.substring(5,7);
			String cod_hex   = numero_dec_a_hex(red_dec) + numero_dec_a_hex(green_dec) + numero_dec_a_hex(blue_dec);
			return cod_hex;
		}
	}

	public String codigo_a_dec(String cod_hexadecimal) {

		if(cod_hexadecimal.length() != 7) {
			throw new IllegalArgumentException("El código rgb tiene que ser del tipo #000000");
		}else {
			String red_hex   = cod_hexadecimal.substring(1,3);
			String green_hex = cod_hexadecimal.substring(3,5);
			String blue_hex  = cod_hexadecimal.substring(5,7);
			String cod_dec = numero_hex_a_dec(red_hex) + numero_hex_a_dec(green_hex) + numero_hex_a_dec(blue_hex);
			return cod_dec;
		}
	}

	
	private String numero_dec_a_hex(String numero_dec) {

		int numero_parseado = Integer.parseInt(numero_dec);
		int digito_a, digito_b;

		digito_a = numero_parseado / 16;
		digito_b = numero_parseado % 16;

		return digitos_hex.get(digito_a) + digitos_hex.get(digito_b);

	}
	
	private String numero_hex_a_dec(String numero_hex) {
		int numero_parseado_unidad = Integer.parseInt(numero_hex.substring(0,1));
		int numero_parseado_decena = Integer.parseInt(numero_hex.substring(1));
		
		int total = (numero_parseado_unidad *16) + (numero_parseado_decena);
		
		return (total <10)? "0" + total : "" + total;
	}


	private HashMap<Integer,String> getDigitosHex() {

		digitos_hex = new HashMap<>();
		digitos_hex.put(0, "0");
		digitos_hex.put(1, "1");
		digitos_hex.put(2, "2");
		digitos_hex.put(3, "3");
		digitos_hex.put(4, "4");
		digitos_hex.put(5, "5");
		digitos_hex.put(6, "6");
		digitos_hex.put(7, "7");
		digitos_hex.put(8, "8");
		digitos_hex.put(9, "9");
		digitos_hex.put(10, "A");
		digitos_hex.put(11, "B");
		digitos_hex.put(12, "C");
		digitos_hex.put(13, "D");
		digitos_hex.put(14, "E");
		digitos_hex.put(15, "F");

		return digitos_hex;
	}
}
