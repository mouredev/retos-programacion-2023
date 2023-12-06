import re

def analyze_text(text):
    number_sentences = len(text.split(".")) - 1

    search = r"[.,:;¿?¡!()]"
    text = re.sub(search, '', text).lower().split(" ")
    number_words = len(text)

    longest_word = max(text, key=len)
    length_words = [len(word) for word in text]
    mean_words = sum(length_words) / number_words

    output = (
        f"Número total de palabras: {number_words}"
        f"\nLongitud media de las palbras: {mean_words:.1f}"
        f"\nNúmero de oraciones del texto: {number_sentences}"
        f"\nPalabra mas larga: {longest_word}"
    )

    return output


text = (
    "El término digital se deriva de la forma en que las computadoras realizan las operaciones contando dígitos. "
    "Durante muchos años, las aplicaciones de la electrónica digital se limitaron a los sistemas informáticos. "
    "Hoy día, la tecnología digital tiene aplicación en un amplio rango de áreas además de la informática. "
    "Aplicaciones como la televisión, los sistemas de comunicaciones, de radar, sistemas de navegación y guiado, "
    "sistemas militares, instrumentación médica, control de procesos industriales y electrónica de consumo, usan "
    "todos ellos técnicas digitales."
)

print(analyze_text(text))
