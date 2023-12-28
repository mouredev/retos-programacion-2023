You can use any online brainfuck interpreter 
I use my own interpreter/compiler: CarlosEduardoL/headache
++++++++++[>+++++++<-]>++ . Prints 'H' (72)             Memory: (0 |  72 |  0)
<++++++[>+++++<-]>- .       Prints 'e' (101)            Memory: (0 | 101 |  0)
+++++++ ..                  Prints 'l' (108) 'l' (108)  Memory: (0 | 108 |  0)
+++ .                       Prints 'o' (111)            Memory: (0 | 111 |  0)
<++++++[>>+++++<<-]>>++ .   Prints ' '                  Memory: (0 | 111 | 32)
<<++++++[>----<-]> .        Prints 'W' (87)             Memory: (0 |  87 | 32)
<++++++[>++++<-]> .         Prints 'o' (111)            Memory: (0 | 111 | 32)
+++ .                       Prints 'r' (114)            Memory: (0 | 114 | 32)
------ .                    Prints 'l' (108)            Memory: (0 | 108 | 32)
-------- .                  Prints 'd' (100)            Memory: (0 | 100 | 32)
>+.                         Prints '!' (100)            Memory: (0 | 100 | 33)