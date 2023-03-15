// Dada una URL con parámetros, crea una función que obtenga sus valores.
// No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.

const URLTEST = {
    reto: 'https://retosdeprogramacion.com?year=2023&challenge=0',
    example:
      'https://www.example.com/search?query=banana&category=fruit&page=2&sort=price_asc',
  };
  
  const getParams = (url: string): void => {
    const urlSplitByInterrogation = url.split('?')[1];
    const urlSplitByAnd = urlSplitByInterrogation.split('&');
    const output = _getParams(urlSplitByAnd);
  
    console.log(output);
  };
  
  const _getParams = (urlArray: string[]): string[] => {
    if (urlArray.length === 0) return [];
    const firstElement = urlArray[0].split('=');
    const restElement = urlArray.slice(1);
  
    return [firstElement[1], ..._getParams(restElement)];
  };
  
  getParams(URLTEST['example']);
  // ["banana", "fruit", "2", "price_asc"]
