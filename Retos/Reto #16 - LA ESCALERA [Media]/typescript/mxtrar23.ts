const creaEscalon = (orientacion: string) => {
  return (orientacion == "asc") ? "_|" : "|_" ;
}

const creaEspacios = (cantidad: number) => {
  let espacios:string = "";
    for (let i = 0; i < cantidad; i++) {
        espacios += "  ";
    }
    return espacios
}

const creaEscalera = (escalas: number) => {
  if(escalas === 0) return console.log(`__`)

  const orientacion:string = (escalas > 0) ? 'asc' : 'desc';
  const pasos:number = Math.abs(escalas)

  for (let index = 0; index < pasos; index++) {
    let espacios:number = (orientacion == "desc") ? index : pasos-index;
    console.log(creaEspacios(espacios)+creaEscalon(orientacion));
    
  }

}


creaEscalera(5)
creaEscalera(0)
creaEscalera(-5)