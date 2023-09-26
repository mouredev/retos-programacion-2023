package com.retos.ej28;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		System.out.println(checkMathExp("3 + 5"));
		System.out.println(checkMathExp("3 a 5"));
		System.out.println(checkMathExp("-3 + 5"));
		System.out.println(checkMathExp("- 3 + 5"));
		System.out.println(checkMathExp("-3 a 5"));
		System.out.println(checkMathExp("-3+5"));
		System.out.println(checkMathExp("3 + 5 - 1 / 4 % 8"));
	}

	private static boolean checkMathExp(String expression) {
		String[] components = expression.split(" ");

		if (components.length < 3 || components.length % 2 == 0) {
			return false;
		}

		boolean check = true;
		for (int index = 0; index < components.length; index++) {
			String component = components[index];
			if (index % 2 == 0) {
				try {
					Double.parseDouble(component);
				} catch (NumberFormatException e) {
					check = false;
				}
			} else {
				check = "+".equals(component) || "-".equals(component) || "*".equals(component) || "/".equals(component)
						|| "%".equals(component);
			}

			if (!check) {
				return false;
			}
		}
		return check;
	}
}
