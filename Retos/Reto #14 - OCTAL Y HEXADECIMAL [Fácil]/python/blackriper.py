from dataclasses import dataclass,field

"""
 recibimos el numero a convertir y la base a la que queremos convertir como el metodo es el mismo
 tanto para octal o hexadecimal solo le proporcionamos la base a dividir 8 para octal y 16 para hexadecimal
 dividimos el numero a convertir y obtenemo el residuo de la division ojo no es el resultado la lista de residuos nos da el resultado
 solo hay que invertir esta lista y listo.
 
"""

@dataclass
class Converter:
    number_base_10:int
    base_to_convert:int
    list_of_mod:list[int]=field(default_factory=list)
    origin_number:int=0
   
    def convert_to_octal_or_hexadecimal(self)->None:
       self.origin_number = self.number_base_10
       while not self.number_base_10<1:
        num_past = self.number_base_10   
        self.number_base_10=int(self.number_base_10/self.base_to_convert)
        self.list_of_mod.append(int(num_past % self.base_to_convert))  
        
           
    # recorremos la lista de modulos y concatenamos con un string para mostrar el resultado     
    def print_number_octal(self)->None:
       res=""
       #[::1] hacemos un corte de lista pero inverso  para acomodar el resultado
       for num in self.list_of_mod[::-1]:
           res += str(num)     
       print(f"El numero {self.origin_number} es igual a {res} en base octal")      
   
    def print_number_hexadecimal(self)->None:
        # lista de tuplas que contiene que valores son sustituidos por una letra
        letters=[(10,"a"),(11,"b"),(12,"c"),(13,"d"),(14,"e"),(15,"f")]
        res=""
        for num in self.list_of_mod[::-1]:
           # traemos una letra de la lista si esta es igual en su primer elmento a un numero de la lista de modulo 
           letter=[v2 for v1,v2 in letters if v1==num] 
           if letter:
               res += letter[0]
           else:   
             res += str(num)   
               
        print(f"El numero {self.origin_number} es igual a {res} en base hexadecimal")   
        
   

# constantes  de la base numeruca  a convertir este valor no cambia 
BASE_OCTAL = 8
BASE_HEXADECIMAL=16
        

def incial_converter()->None:
    number=int(input("Introduce un numero\n"))   
    opcion=input("¿ A que deseas convertir este numero [OC] octal [HX] hexadecimal\n")
    if opcion.upper() == "OC":
       oc=Converter(number,BASE_OCTAL)
       oc.convert_to_octal_or_hexadecimal()
       oc.print_number_octal() 
    elif opcion.upper() == "HX":
        hx=Converter(number,BASE_HEXADECIMAL)
        hx.convert_to_octal_or_hexadecimal()
        hx.print_number_hexadecimal()  
    
    else:
        print("opcion incorrecta solo se admite HX o OC")     
        exit(1)
   
   
          
def main():
    incial_converter()
   
    
   

if __name__=='__main__':
    main()