package main

import (
    "fmt"
    "errors"
    )

// metodos para resolver el ejercicio
type Infiltrate interface{
    IsSame() (bool,error)
    FindInfilters()
}

// tipo de dato para trabajar
type Format struct{
    Text1 string
    Text2 string
}

// metodo para saber si ambos textos tienen la misma longitud
func (f *Format) IsSame() (bool,error){
    if len(f.Text1) != len(f.Text2){
        return false,errors.New("the texts must have the same length")
    }
    return true,nil
}

// metodo para encontrar las diferencias convirtiendo los textos a char o rune 
func (f *Format) FindInfilters(){
    var formatErrors []string
    text2:=[]rune(f.Text2)
    
    for indx,t1:= range f.Text1{
          if string(t1)!= string(text2[indx]){
              formatErrors= append(formatErrors,string(text2[indx]))
          }
      }        
    
    fmt.Printf("%v / %v -> %v \n",f.Text1,f.Text2,formatErrors)
}


func main() {
    var infl Infiltrate=&Format{Text1:"Me llamo mouredev ",Text2:"Me llemo mouredov "}
    same,err:=infl.IsSame()
    if err!=nil{
        panic(err)
    }
    if same{
      infl.FindInfilters()    
    }
}
