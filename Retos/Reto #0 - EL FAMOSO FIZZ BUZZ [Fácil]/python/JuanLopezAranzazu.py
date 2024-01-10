
def solution(num,word1,word2):
    for i in range(1,num+1):
        if(i%3==0 and i%5==0):
            print(word1+word2)
        elif(i%3==0):
            print(word1)
        elif(i%5==0):
            print(word2)
        else:
            print(i)

solution(100,"fizz","buzz")
