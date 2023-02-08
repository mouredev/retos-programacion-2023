import Foundation



func IsPar (num: Int)->Bool{
    
    let asd = num % 2
    
    if asd == 0{
        return true
    }
    else{
        return false
    }
    
}

//IsPrimo(num: 1234535)

func IsPrimo(num: Int)->Bool{
    
    var cont = 0
    for i in 1..<num {
        var asd = num % i
        if asd == 0 {
            cont += 1
        }
    }
    if cont > 2{
        return false
    }
    else{
        return true
    }
    
}

//IsPrimo(num: 98)

func IsFibonacci(num: Int)->Bool{
    
    var act = true
    var nAnt1 = 1
    var nAnt = 2
    var nAct = 0
    while(act){
        nAct = nAnt + nAnt1
        if num == nAct{
            act = false
            return true
        }
        else if nAct > num{
            act = false
            return false
        }
        else{
            nAnt1 = nAnt
            nAnt = nAct
        }
    }
}


func IsTotal(num: Int){
    
    if IsPar(num: num), IsPrimo(num: num), IsFibonacci(num: num){
       print("\(num) es par, primo y fibonacci")
    }
    else if IsPar(num: num), IsPrimo(num: num) {
        print("\(num) es par, no es fibonacci y es primo")
    }
    else if IsPar(num: num), IsFibonacci(num: num) {
        print("\(num) es par, fibonacci y no es primo")
    }
    else if IsPrimo(num: num), IsFibonacci(num: num) {
        print("\(num) es impar, fibonacci y es primo")
    }
    else if IsPrimo(num: num) {
        print("\(num) es impar, no es fibonacci y es primo")
    }
    else if IsPar(num: num) {
        print("\(num) es par, no es fibonacci y no es primo")
    }
    else if IsFibonacci(num: num) {
        print("\(num) es impar, es fibonacci y no es primo")
    }
    else{
        print("\(num) es impar, primo ni fibonacci")
    }
}

IsTotal(num: 21)
