package main

import (
	"fmt"
	"strconv"
)

/* Hola mundo*/ 

func main(){
  fmt.Println("Hello World!!")
}

/* Tipos de datos */ 
var message string ="Hola como estas?"
var microcode rune ='h' // o byte
var precio int=12 // o  int8 int16 int32 int64
var taxes  float32=12.5
var cost  float64= 135.56
var send  bool = false

/* declaracion de variables */
// constante
const fileName string="Archivo.pdf"
// variable global
var isFriday bool=false

/* estructuras condicionales*/ 
var ninja string ="Naruto"
// tiene que ir dentro de la funcion main
if ninja=="Naruto"{
  fmt.Printf("%v ha usando el Rasenchuriken!!",ninja)
}else{
  fmt.Println("No ninja !!")
}

/* Estructuras de datos */

// slices o array
var hokages []string=[]{"Hashirama","Tobirama","Hiruzen","Minato"}

// diccionarios o mapas 
var ninjaTools map[string]string

ninjaTools["shuriken"]="shuriken"
ninjaTools["papelboom"]="papel bomba"

/*Estructuras de repeticion*/

//for in
for index,hokages:= range hokages{
  fmt.Printf("%v fue el %v hokage de Konoha",hokage,index)
}

// for como while
 var countdown= 10 
 for countdown>0{
   fmt.Println(countdown--)
 }

// for tradicional 

for indx:=0;indx<len(hokages);indx++{
  fmt.Println(hokages[indx])
}

/* funciones */ 

func NinjaJutsu(){
  fmt.Println("Sasuke usa el jutsu bola de fuego")
}

func IsBijuu(name string) bool{
 if name=="Kyubii"{
   return true
 }else if name =="Shukaku"{
   return true
 }
 return false
}

/* go no utliza clases pero hace algo parecido */ 

// la  estructura struct sirve para definir tipos de datos complejos en este caso es como definir los atributos de una clase 
type Shinobi struct{
  Name string
  Clan string
  Jutsu string
}
// las funciones reciben una propiedad extra llamada Reciver  estas le indican que este metodo pertenece a la estruct 
func (s *Shinobi) NewJutsu(jutsu string){
  s.Jutsu=jutsu
}

func (s Shinobi) Attack(){
   fmt.Printf("%v usa el jutsu %v",s.Name,s.Jutsu)
 }

func ejemplo(){
 shikamaru:= &Shinobi{Name:"shikamaru",Clan:"Nara",Jutsu:"atadura de sombra"}
 shikamaru.Attack()
 shikamaru.NewJutsu("Clon de sombra")
 shikamaru.Attack()
 }

 /* Control de errores*/ 
  func ControlError(){
    var price string = "124"
    // convertir variable a entero
    num,err:=strconv.Atoi(price)
    
    // hacer algo en caso de error 
    if err!=nil{
      panic(err)
    }
    fmt.Println(num)
  }













