// Llamar a una API es una de las tareas más comunes en programación.
//
// Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
// resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...

const URLQUOTE: string = 'https://quote-garden.onrender.com/api/v3/quotes';

const getQuote = async (calls: number = 0): Promise<void> => {

  if (calls === 3) return console.log('Reaching 3 max calls to the API quote');
  try {
    const request = await fetch(URLQUOTE);
    const response = await request.json();

     if (response.statusCode !== 200) throw new Error('Failed API call');
     const { data } = response;
     console.log(data);

  } catch (err) {
     console.log(err.message);
     getQuote(calls + 1);

  }
};

getQuote();
