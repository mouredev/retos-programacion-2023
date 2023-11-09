/*
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarán en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
 */

// Vm = (Xf-Xi)/(Tf-Ti) Donde el eje X es la deribada del tiempo y El eje Y es la derivada de la posicion
//Vm(Tf-Ti)=Xf-Xi
//Vm(Tf-Ti) + Xi = Xf como el tiempo inicial=0 entonces la ecuacion queda:
//Xf = Xi + Vm*Tf => /Xf = Xi + (Vf-Vi)*Tf
//Igualdad entre posisciones
//Xf1===Xf2 =>   Xi1 + Vm1*Tf= Xi2 + Vm2*Tf  => Vm1*Tf - Vm2*Tf = Xi2 - Xi1
//Tf = (Xi2 - Xi1)/(Vm-Vm)
//TF = ((x2,y2) - (x1,y1))/(Vm1-Vm2) //(v1X,v1Y) (v2X,v2Y)


const intersecction = (x1,y1,x2,y2,v1X,v1Y,v2X,v2Y) =>{
    const cruceX = (x2-x1)/(v1X-v2X)
    const cruceY = (y2-y1)/(v1Y-v2Y)

    if(cruceX>=0){
        //Xf = Xi + Vm*Tf
        const X = x1 + v1X*cruceX
        const Y = y1 + v1Y*cruceX
        console.log('Se cruzan en el tiempo: '+ cruceX)
        console.log(`Las coordenadas finales son: (${X},${Y})`)
    }
    else if(cruceY>=0){
        const X = x1 + v1X*cruceY
        const Y = y1 + v1Y*cruceY
        console.log('Se cruzan en el tiempo: '+ cruceY)
        console.log(`Las coordenadas finales son: (${X},${Y})`)
    }
    else{
        console.log('No se cruzan')
    }

}

console.log(intersecction(3,2,1,4,2,1,1,2))
console.log(intersecction(1,0,0,1,2,0,0,3))
console.log(intersecction(2,1,4,2,1,0,0,1))
console.log(intersecction(1,2,3,1,1,1,-1,1))
