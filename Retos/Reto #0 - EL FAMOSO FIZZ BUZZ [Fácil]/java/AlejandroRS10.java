public class AlejandroRS10 {
    public static void main(String[] args) {

        for (int i=1;i<101;i++){
        if (i%3==0 && i%5==0){
            System.out.println("Por el culo te la hinco");
        } else if (i%5==0) {
            System.out.println("te la hinco");
        } else if (i%3==0) {
            System.out.println("Por el culo");
        }else System.out.println(i);
        }
    }
}

//public class Reto_0 {
//    public Reto_0() {
//    }
//
//    public static void main(String[] args) {
//        for(int i = 1; i < 101; ++i) {
//            if (i % 3 == 0 && i % 5 == 0) {
//                System.out.println("Por el culo te la hinco");
//            } else if (i % 5 == 0) {
//                System.out.println("te la hinco");
//            } else if (i % 3 == 0) {
//                System.out.println("Por el culo");
//            } else {
//                System.out.println(i);
//            }
//        }
//
//    }
//}



/*WHILE n<101, entramos:
BUCLE
n++
Si n%3=0, f=1
Si n%5=0, b=1
Si f+b>2, fb=1

Si fb=1, println(t3)
 else si b=1, println(t2)
    else si f=1, println(t1)
        else println (n)
f=0, b=0; fb=0
BUCLE

 */