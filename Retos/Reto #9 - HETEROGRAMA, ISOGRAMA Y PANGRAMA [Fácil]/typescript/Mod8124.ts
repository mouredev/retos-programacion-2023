// Crea 3 funciones, cada una encargada de detectar si una cadena de
// texto es un heterograma, un isograma o un pangrama.
// - Debes buscar la definición de cada uno de estos términos.
// - Heterograma contiene letras diferentes y únicas, es decir, ninguna letra se repite dentro de la palabra. 1 una vez x cada una
// - Isograma todas la letras tienen la misma cantidad de repeticiones(este no lo entedi muy bien xD), creo que almenos una palabra tiene que tener 2 repiticiones
// - Pangrama contiene todo el abecedario al menos una vez

  interface Iwords {
    heterograma: string[];
    isograma: string[];
    pangram: string[];
  };
  
  interface IAlphabet {
    [key: string]: number;
  };
  
  const words: Iwords = {
    heterograma: ['murciélago', 'azul', 'galo', 'buzón', 'cremalera'],
    isograma: ['Ajedrez', 'Murciélago', 'Zanahoria', 'Clavicordio', 'Hidroavión'],
    pangram: [
      'The quick brown fox jumps over the lazy dog',
      'Portez ce vieux whisky au juge blond qui fume',
      'Sphinx of black quartz, judge my vow',
    ],
  };
  
  const Arrayalphabet: string[] = [...Array(26).keys()].map((i) =>
    String.fromCharCode(i + 97)
  );

  let alphabet: IAlphabet = {};
  Arrayalphabet.forEach((letter: string) => (alphabet[letter] = 0));
  
  const isPangram = (): boolean => {
    const hasEmptyValue = Object.keys(alphabet).some((key) => !alphabet[key]);
    return !hasEmptyValue;
  };
  
  const isHeterogram = (): boolean => {
    for (const [key, value] of Object.entries(alphabet)) {
      if (value > 1) return false;
    }
    return true;
  };
  
  const isIsogram = (): boolean => {
    for (const [key, value] of Object.entries(alphabet)) {
      if (value > 1) return true;
    }
    return false;
  };
  
  const msg = (type: string, positive: boolean = true): string => positive ? `El texto es un ${type}` : `El texto no es un ${type}`;
  
  const whatIsMyText = (text: string) => {
    const defaultAlphabet = alphabet;
  
    for (let i = 0; i < text.length; i++) {
      const key = text[i].toLowerCase();
      if (alphabet.hasOwnProperty(key)) alphabet[key] += 1;
    }
  
    console.log(isPangram() ? msg('pangrama') : msg('pangrama', false));
    console.log(isHeterogram() ? msg('heterograma') : msg('heterograma', false));
    console.log(isIsogram() ? msg('isograma') : msg('isograma', false));
  
    alphabet = defaultAlphabet;
  };
  
  whatIsMyText(words.heterograma[0]);