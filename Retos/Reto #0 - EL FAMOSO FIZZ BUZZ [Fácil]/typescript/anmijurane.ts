const __init__ = () => {

  const length = 100;
  const arrayForNumbers = Array.from({ length }, (_, idx) => idx + 1);

  const isMultleOf = ( val: number, multipleOf: number ) => val % multipleOf === 0;

  const descriptor = [
    { replaceFor: 'fizz', multipleFor: 3 },
    { replaceFor: 'buzz', multipleFor: 5 },
  ];

  (() => {
    arrayForNumbers
      .forEach(number => {
        let accString = '';
        descriptor.forEach(({ multipleFor, replaceFor }) => {
          accString += isMultleOf(number, multipleFor) ? `${replaceFor} ` : ' ';
        });
        accString = accString.trim();
        console.log({ number, accString })
      })
  })();

}

__init__();