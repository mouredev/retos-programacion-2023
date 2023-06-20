//
//  main.swift
//  Soragunter
//
//  Created by Soragunter on 29/3/23.
//

import Foundation

introduccion()

func introduccion(){
    print("Bienvenido a: Adivina la Palabra!")
    print("Sabes las reglas del juego? SI / NO")
    escogeSiNo()
}

func reglas(){
    
    print("-------------------------------------------------------------")
    print("Las reglas son sencillas:")
    print("Te aparecerá una palabra sin algunas letras")
    print("Tu objetivo será adivinar dicha palabra y escribirla")
    print("En cada turno podrás escribir una letra o la palabra resuelta")
    print("Tendrás el doble de intentos que letras falten")
    print("-------------------------------------------------------------")
    
}

func juego(){
    
    let palabra = Randomizador()
    var palabraGuiones = ""
    var contador60Porcentaje = 0.0
    var letrasAdivinar : [String] = []
    var numeroaumento = 0
    var truefalseArray : [Bool] = []
    var todasletrasArray : [String] = []
 
    print("La palabra a adivinar es:")
    print("-------------------------")
    
    for word in palabra{
        
        let boolRandom = Bool.random()
        let calculo = round(Double(palabra.count) * 0.6)
        
        if contador60Porcentaje < calculo && boolRandom == false{
            
            palabraGuiones += "_"
            contador60Porcentaje += 1
            letrasAdivinar.append(String(word))
            todasletrasArray.append(String(word))
            truefalseArray.append(false)
            
            
        }else{
            
            todasletrasArray.append(String(word))
            palabraGuiones += String(word)
            truefalseArray.append(true)
            
        }
    }
    
    var intentos = Int(contador60Porcentaje) * 2
    
    
    
    while intentos > 0{
        
        print("\(palabraGuiones)")
        let palabraGuionesfallo = palabraGuiones
        palabraGuiones = ""
        print("-------------------------")
        print("Escribe una letra o la palabra entera; tienes \(intentos) intentos")
        
        let letraPalabraIntroducida = readLine()
        if letraPalabraIntroducida == palabra{
            
            print("¡Correcto!")
            print("----------")
            print("¡FELICIDADES!: ¡¡Has ganado el juego!! ")
            VolverJugar()
                        
        }else if letraPalabraIntroducida == letrasAdivinar[numeroaumento]{
            
            numeroaumento += 1
            var contadorTemp = 0
            for _ in truefalseArray{
                
                if truefalseArray[contadorTemp] == true{
                    
                    palabraGuiones += todasletrasArray[contadorTemp]
                    
                }else{
                    
                    truefalseArray[contadorTemp] = true
                    while contadorTemp < truefalseArray.count{
                        if truefalseArray[contadorTemp]  == true{
                            palabraGuiones += todasletrasArray[contadorTemp]
                        }else{
                            palabraGuiones += "_"
                        }
                        contadorTemp += 1
                    }
                    break
                }
                
                contadorTemp += 1
            }
            print("¡Correcto!")
            print("----------")
            
            
        }else if letraPalabraIntroducida != letrasAdivinar[numeroaumento]{
            
            intentos -= 1
            print("Has fallado. Vuelve a intentarlo")
            palabraGuiones = palabraGuionesfallo
        }
    }
    
    if intentos == 0{
        
        print("---------------------------------------------------------------")
        print("Ohhhhh, se te han acabado los intentos... Pero, quieres volver a jugar? SI/NO")
        VolverJugar()
    }
    
}

func VolverJugar(){
    
    print("---------------------------------------")
    print("¿Quieres volver a jugar? SI/NO")
    
    let siNo = readLine()
    
    if siNo! == "SI"{
        
        print("¡Estupendo! ¡Vamos a ello!")
        print("--------------------------")
        juego()
        
    }else if siNo! == "NO"{
        
        print("Gracias por jugar a: ¡Adivina la palabra!")
        print("¡Hasta la próxima!")
        exit(0)
        
    }else{
        
        print("Creo que no te he entendido, vuelve a intentarlo:")
        VolverJugar()
        
    }
}

func Randomizador() -> String{
    
    let palabras : [String] = ["TORMENTAS","SORAGUNTER","ORDENADOR","PROGRAMACION","SWIFT","LANZA","ESPADA","GUANTE","DANZANTE","CORREDOR","VERDAD","TEJEDOR","CAMINO","VIAJE","DESTINO","FORTALEZA","DEBILIDAD","ROMPEDORES","CIELO","VIENTO"]
    
    let numeroRandomizar = Int.random(in: 1...palabras.count)
    
    let palabraRandomizada = palabras[numeroRandomizar - 1]
    
    return palabraRandomizada
    
}

func escogeSiNo(){
    
    print("-------------------------------------")
    
    let siNo = readLine()
    
    if siNo! == "SI"{
        
        print("---------------------------------")
        print("¡¡QUE COMIENCEN LOS JUEGOS PUES!!")
        print("---------------------------------")
        juego()
        
    }else if siNo! == "NO"{
        
        reglas()
        print("Explicadas las reglas; ¡¡QUE COMIENCEN LOS JUEGOS!!")
        print("---------------------------------------------------")
        juego()
        
    }else{
        
        print("Creo que no te he entendido, vuelve a intentarlo:")
        escogeSiNo()
    }
}
