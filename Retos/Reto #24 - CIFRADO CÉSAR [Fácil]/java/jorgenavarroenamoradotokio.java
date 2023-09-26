package com.retos.ej24;

import java.util.ArrayList;
import java.util.List;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		caesarCipher("Mi nombre es MoureDev.", false, 3);
		caesarCipher("ol proeuh hv orxuhghy.", true, 3);
		caesarCipher("Mi nombre es MoureDev.", false, 5);
		caesarCipher("qn rtqgwj jx qtzwjija.", true, 5);
	}

	public static void caesarCipher(String text, boolean decrypt, int shift) {
		String alphabet = "abcdefghijklmnopqrstuvwxyz";
		List<Character> charList = new ArrayList<>();
		for (char c : alphabet.toCharArray()) {
			charList.add(c);
		}
		charList.add(charList.indexOf('n') + 1, 'ñ');

		StringBuilder caesarText = new StringBuilder();

		text = text.toLowerCase();

		for (char value : text.toCharArray()) {
			if (charList.contains(value)) {
				int index = (charList.indexOf(value) + (decrypt ? -shift : shift)) % charList.size();
				if (index < 0) {
					index += charList.size();
				}
				caesarText.append(charList.get(index));
			} else {
				caesarText.append(value);
			}
		}
		System.out.println(caesarText.toString());
	}
}
