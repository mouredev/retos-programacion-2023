//
//  Soragunter.swift
//  Aurebesh
//
//  Created by Soragunter on 12/4/23.
//

import Foundation

func Aurebesh(texto: String)-> String{
    
    var textoTraducir = texto
    var letraAurebesh = ""
    var textoTraducidoEspañol = ""
    var textoTraducidoAurebesh = ""
    var textoTraducido = ""
    
    // Traducción del Aurebesh al Español
    for word in textoTraducir{
        
        letraAurebesh += String(word.uppercased())
        
        switch letraAurebesh{
            
            case "AUREK":
                textoTraducidoEspañol += "A"
                letraAurebesh = ""
            case "BESH":
                textoTraducidoEspañol += "B"
                letraAurebesh = ""
            case "CRESH":
                textoTraducidoEspañol += "C"
                letraAurebesh = ""
            case "DORN":
                textoTraducidoEspañol += "D"
                letraAurebesh = ""
            case "ESK":
                textoTraducidoEspañol += "E"
                letraAurebesh = ""
            case "FORN":
                textoTraducidoEspañol += "F"
                letraAurebesh = ""
            case "GREK":
                textoTraducidoEspañol += "G"
                letraAurebesh = ""
            case "HERF":
                textoTraducidoEspañol += "H"
                letraAurebesh = ""
            case "ISK":
                textoTraducidoEspañol += "I"
                letraAurebesh = ""
            case "JENTH":
                textoTraducidoEspañol += "J"
                letraAurebesh = ""
            case "KRILL":
                textoTraducidoEspañol += "K"
                letraAurebesh = ""
            case "LETH":
                textoTraducidoEspañol += "L"
                letraAurebesh = ""
            case "MERN":
                textoTraducidoEspañol += "M"
                letraAurebesh = ""
            case "NERN":
                textoTraducidoEspañol += "N"
                letraAurebesh = ""
            case "OSK":
                textoTraducidoEspañol += "O"
                letraAurebesh = ""
            case "PETH":
                textoTraducidoEspañol += "P"
                letraAurebesh = ""
            case "QEK":
                textoTraducidoEspañol += "Q"
                letraAurebesh = ""
            case "RESH":
                textoTraducidoEspañol += "R"
                letraAurebesh = ""
            case "SENTH":
                textoTraducidoEspañol += "S"
                letraAurebesh = ""
            case "TRILL":
                textoTraducidoEspañol += "T"
                letraAurebesh = ""
            case "USK":
                textoTraducidoEspañol += "U"
                letraAurebesh = ""
            case "VEV":
                textoTraducidoEspañol += "V"
                letraAurebesh = ""
            case "WESK":
                textoTraducidoEspañol += "W"
                letraAurebesh = ""
            case "XESH":
                textoTraducidoEspañol += "X"
                letraAurebesh = ""
            case "YIRT":
                textoTraducidoEspañol += "Y"
                letraAurebesh = ""
            case "ZEREK":
                textoTraducidoEspañol += "Z"
                letraAurebesh = ""
            case "CHEREK":
                textoTraducidoEspañol += "CH"
                letraAurebesh = ""
            case "ENTH":
                textoTraducidoEspañol += "AE"
                letraAurebesh = ""
            case "ONITH":
                textoTraducidoEspañol += "EO"
                letraAurebesh = ""
            case "KRENTH":
                textoTraducidoEspañol += "KH"
                letraAurebesh = ""
            case "NEN":
                textoTraducidoEspañol += "NG"
                letraAurebesh = ""
            case "ORENTH":
                textoTraducidoEspañol += "OO"
                letraAurebesh = ""
            case "SHEN":
                textoTraducidoEspañol += "SH"
                letraAurebesh = ""
            case "THESH":
                textoTraducidoEspañol += "TH"
                letraAurebesh = ""
            case " ":
                if textoTraducidoEspañol == ""{
                    
                    break
                    
                }else{
                    
                    textoTraducidoEspañol += " "
                    letraAurebesh = ""
                    
                }
            case "!":
                textoTraducidoEspañol += "!"
                letraAurebesh = ""
            case "¡":
                textoTraducidoEspañol += "¡"
                letraAurebesh = ""
            case "¿":
                textoTraducidoEspañol += "¿"
                letraAurebesh = ""
            case "?":
                textoTraducidoEspañol += "?"
                letraAurebesh = ""
            case ".":
                textoTraducidoEspañol += "."
                letraAurebesh = ""
            case ",":
                textoTraducidoEspañol += ","
                letraAurebesh = ""
            
            //Me obliga a poner un Default, así que pongo codigo que no haga nada.
            default :
                var dummy = true
                if dummy == true{
                    dummy = false
                }
        }
    }
    

    //Traducción del Español al Aurebesh
    if textoTraducidoEspañol == ""{
        
        for word in textoTraducir{
            
            switch word.uppercased(){
                
                case "A":
                    textoTraducidoAurebesh += "Aurek"
                case "B":
                    textoTraducidoAurebesh += "Besh"
                case "C":
                    textoTraducidoAurebesh += "Cresh"
                case "D":
                    textoTraducidoAurebesh += "Dorn"
                case "E":
                    textoTraducidoAurebesh += "Esk"
                case "F":
                    textoTraducidoAurebesh += "Forn"
                case "G":
                    textoTraducidoAurebesh += "Grek"
                case "H":
                    textoTraducidoAurebesh += "Herf"
                case "I":
                    textoTraducidoAurebesh += "Isk"
                case "J":
                    textoTraducidoAurebesh += "Jenth"
                case "K":
                    textoTraducidoAurebesh += "Krill"
                case "L":
                    textoTraducidoAurebesh += "Leth"
                case "M":
                    textoTraducidoAurebesh += "Mern"
                case "N":
                    textoTraducidoAurebesh += "Nern"
                case "O":
                    textoTraducidoAurebesh += "Osk"
                case "P":
                    textoTraducidoAurebesh += "Peth"
                case "Q":
                    textoTraducidoAurebesh += "Qek"
                case "R":
                    textoTraducidoAurebesh += "Resh"
                case "S":
                    textoTraducidoAurebesh += "Senth"
                case "T":
                    textoTraducidoAurebesh += "Trill"
                case "U":
                    textoTraducidoAurebesh += "Usk"
                case "V":
                    textoTraducidoAurebesh += "Vev"
                case "W":
                    textoTraducidoAurebesh += "Wesk"
                case "X":
                    textoTraducidoAurebesh += "Xesh"
                case "Y":
                    textoTraducidoAurebesh += "Yirt"
                case "Z":
                    textoTraducidoAurebesh += "Zerek"
                default:
                    textoTraducidoAurebesh += String(word)
                
            }
        }
        
        print("\(textoTraducidoAurebesh)")
        textoTraducido = textoTraducidoAurebesh
        
    }else{
        
        print("\(textoTraducidoEspañol)")
        textoTraducido = textoTraducidoEspañol
        
    }
    
    return textoTraducido
    
}


Aurebesh(texto:"HerfOskLethAurek QekUskEsk TrillAurekLeth?")
