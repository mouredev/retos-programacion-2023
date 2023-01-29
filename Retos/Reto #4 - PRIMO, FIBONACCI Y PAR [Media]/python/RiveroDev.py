#! bin/python3


class fibo_primo_par():

    def __init__(self, numero):

        self.numero = numero

    def num_primo(self) -> bool:
        valor = False
        for i in range(2,self.numero):
            if self.numero % i == 0 :
                valor = True
        return valor 

    def num_par(self) -> bool:
        valor = False
        if self.numero % 2 == 0:
            valor = True
        return valor
    
    def num_fibo(self) -> bool:
        
        valor = False

        self.numero
        a = 1
        b = 1
        c = 0 
        if self.numero == 1:
            valor = True
        while self.numero > c:
            c = b + a
            if c == self.numero:
                valor = True   
            a,b = b , c

        return valor

    def que_es(self):
        pass




if __name__=="__main__":
    
    fibo = fibo_primo_par(7)
    #print(fibo.num_par())
    #print(fibo.num_primo())
    print(fibo.num_fibo())