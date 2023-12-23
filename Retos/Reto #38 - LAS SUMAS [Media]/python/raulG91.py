def sum_array(array): 
    sum = 0
    for element in array:
        sum+=element
    return sum

def sum(array,result_list,target):
    if sum_array(array) == target:
        result_list.append(array)
    if(len(array) == 1):
       return     
    else:
        for i,n in enumerate(array):
            sum(array[0:i]+array[i+1:],result_list,target)
            
lista = [1,5,2,3]

result_list = []
sum(lista,result_list,6)
#Removing duplicates
res = []
[res.append(x) for x in result_list if x not in res]
print(res)