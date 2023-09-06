//: PERMUTACIONES

import Foundation

//Explicación
//Empezamos con prefijo vacio y en sufijo está la palabra que se quiere permutar.
//Se van recoriendo las letras del sufijo y se van creando todos los posibles prefijos añadiendo letra a letra.
//En el ejemplo: con prefijo letra s, hacemos prefijo + o, prefijo + l que serán los nuevos prefijos, y así hasta que no haya letras en sufijo y hayamos encontrado una permutación.

// PREF || SUF      PREF || SUF    PREF(¡RESULTADOS!)
//
//  s ---->ol   ---> so ---> l ----> sol
//              ---> sl ---> o ----> slo
//
//  o ---->sl   ---> os ---> l ----> osl
//              ---> ol ---> s ----> ols
//
//  l ---->so   ---> ls ---> o ----> lso
//              ---> lo ---> s ----> los

func perm(pref: String, suf: String, permutations: inout [String] )  {
    if suf.count == 0 {
        permutations.append(pref)
    }
    suf.forEach({ letter in
        let newPref = pref + String(letter)
        var newSuf = suf
        if let index = suf.firstIndex(of: letter) {
            newSuf = String(suf.prefix(upTo: index) + suf.suffix(from: suf.index(after: index)))
        }
        perm(pref: newPref, suf: newSuf , permutations: &permutations)
    })
}
    
var myString = "sol"
var permutations: [String] = []
perm(pref: "", suf: myString, permutations: &permutations)

print(permutations)
