void main(){
     
    String palabra = 'fizzbuzz';
    //Para fizz
    String p3= palabra.substring(0,4);
    //Para buzz
    String p5= palabra.substring(4);
    
    //contador
    int i=1;
    while (i<=100){
      
      if(i % 3 == 0){
        print(p3);
      } else if(i % 5 == 0){
        print(p5);
      } else if(i % 5 ==0 && i% 3==0){
        print(palabra);
      } else{
        print(i);
      }
      
      i++;
    }
}