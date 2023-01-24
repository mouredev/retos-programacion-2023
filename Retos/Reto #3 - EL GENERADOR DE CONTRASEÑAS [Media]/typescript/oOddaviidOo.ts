/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
type Password = string;

interface PasswordGenerationOptions {
  length: number;
  passwordCharacterOptions: PasswordCharacterOptions;
}

enum PasswordCharacterOptions {
  None = 0,
  CombineUppercase = 1 << 0, // 001
  CombineNumbers = 1 << 1, // 010
  CombineSymbols = 1 << 2, // 100
}

const LOWERCASE_LETTERS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",
];
const UPPERCASE_LETTERS = LOWERCASE_LETTERS.map((lowerCaseLetter) => {
  return lowerCaseLetter.toUpperCase();
});
const NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const SYMBOLS = ["!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~",
];

const getRandomNumber = (min: number, max): number => {
  return Math.floor(Math.random() * (max - min + 1)) + min;
};

const EXAMPLE_CONFIG: PasswordGenerationOptions = {
  // Usar opciones de generación aleatorias
  // length: getRandomNumber(8, 16),
  // passwordCharacterOptions: getRandomNumber(0, 7),
  length: 8,
  passwordCharacterOptions:
    PasswordCharacterOptions.CombineUppercase |
    PasswordCharacterOptions.CombineNumbers |
    PasswordCharacterOptions.CombineSymbols,
};

const getRandomCharacterFromCharacterType = (
    characterCollection: string[]
  ): string => {
    return characterCollection[
      getRandomNumber(0, characterCollection.length - 1)
    ];
  };

const getPasswordValidCharacter = (
    passwordCharacterOptions: PasswordCharacterOptions
  ) => {
    let generatedCharacters: string[] = [];
    generatedCharacters.push(getRandomCharacterFromCharacterType(LOWERCASE_LETTERS));
    if (passwordCharacterOptions & PasswordCharacterOptions.CombineUppercase) {
      generatedCharacters.push(getRandomCharacterFromCharacterType(UPPERCASE_LETTERS));
    }
    if (passwordCharacterOptions & PasswordCharacterOptions.CombineNumbers) {
      generatedCharacters.push(getRandomCharacterFromCharacterType(NUMBERS));
    }
    if (passwordCharacterOptions & PasswordCharacterOptions.CombineSymbols) {
      generatedCharacters.push(getRandomCharacterFromCharacterType(SYMBOLS));
    }
    return generatedCharacters[
      getRandomNumber(0, generatedCharacters.length - 1)
    ];
  };

const generatePassword = (
  passwordGenerationOptions: PasswordGenerationOptions
): Password => {
  if (passwordGenerationOptions.length < 8 ||passwordGenerationOptions.length > 16) {
    throw new Error("La longitud especificada para la contraseña no se encuentra entre 8 y 16 caracteres");
  }
  let password: Password = "";
  for (let index = 0; index <= passwordGenerationOptions.length - 1; index++) {
    password+=`${getPasswordValidCharacter(passwordGenerationOptions.passwordCharacterOptions)}`;
  }
  return password;
};

const showGeneratedPassword = (password: Password): void => {
  console.log(`Contraseña generada: ${password}`);
};

const showPasswordCharacterOptions = (
  passwordGenerationOptions: PasswordGenerationOptions
): void => {
  let generationOptionsResult: string = "Opciones de generación: ";
  generationOptionsResult += `\n- Longitud de la contraseña: ${passwordGenerationOptions.length}`;
  if (passwordGenerationOptions.passwordCharacterOptions &PasswordCharacterOptions.CombineUppercase ) {
    generationOptionsResult += "\n- Combinando mayusculas";
  }
  if (passwordGenerationOptions.passwordCharacterOptions &PasswordCharacterOptions.CombineNumbers ) {
    generationOptionsResult += "\n- Combinando números";
  }
  if (passwordGenerationOptions.passwordCharacterOptions &PasswordCharacterOptions.CombineSymbols ) {
    generationOptionsResult += "\n- Combinando símbolos";
  }
  if (passwordGenerationOptions.passwordCharacterOptions === PasswordCharacterOptions.None
  ) { generationOptionsResult += "\n- Solo letras minúsculas";
  }
  console.log(generationOptionsResult);
};

const main = (): void => {
  showGeneratedPassword(generatePassword(EXAMPLE_CONFIG));
  showPasswordCharacterOptions(EXAMPLE_CONFIG);
};

main();
