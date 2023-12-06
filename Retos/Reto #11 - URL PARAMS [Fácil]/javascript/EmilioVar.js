const url = 'https://www.google.com/search?q=retos+mouredev&rlz=1C5CHFA_enES1012ES1012&oq=retos+mouredev&aqs=chrome..69i57j0i22i30.2119j0j7&sourceid=chrome&ie=UTF-8';

function onlyParam(text) {
  let splitString = text.split('&')
  let params = []
  splitString.forEach(element => {
    let cut = element.slice(element.indexOf("=") + 1);
    params.push(cut)
  });
  return params;
}
console.log(onlyParam(url)) // ["1C5CHFA_enES1012ES1012","retos+mouredev","chrome..69i57j0i22i30.2119j0j7","chrome","UTF-8"]