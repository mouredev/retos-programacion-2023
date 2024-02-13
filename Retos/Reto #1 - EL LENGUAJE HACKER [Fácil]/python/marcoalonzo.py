'''
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
'''

#Function creation passing through the text provided by user input
def hacker_language(text):
	#Define dictionary associating alphabet letters with leet characters
	leet_dict = {
        'A':'4', 'B':'I3', 'C':'[', 'D':')' ,'E':'3', 'F':'|=', 'G':'&', 'H':'#', 'I':'1', 'J':',_|', 'K':'>|',
         'L':'1', 'M':'JVI', 'N':'^/', 'O': '0', 'P':'|*', 'Q':'(_,)', 'R':'I2', 'S':'5', 'T': '7', 'U':'(_)', 'V':'\/', 'W':'\/\/', 'X':'><', 'Y':'j', 'Z': '2',
         '1':'L', '2':'R', '3':'E', '4':'A', '5':'S', '6':'b', '7':'T', '8':'B', '9':'g', '0':'o'}
	
	#Make input text uppercase
	text = text.upper()
	print(f"Your text in human form: {text}")
	#We loop through each charater in the user input text
	for char in text:
		#If a text character is found in the dictionary, we replace that text character with the corresponding leet character
		if char in leet_dict:
			text = text.replace(char,leet_dict[char])
	print(f"Your converted text: {text}")

#We ask the user to provide text and we invoke the function and pass through the provided text
text = input("Please provide a text to convert to Leet talk: ")
hacker_language(text)