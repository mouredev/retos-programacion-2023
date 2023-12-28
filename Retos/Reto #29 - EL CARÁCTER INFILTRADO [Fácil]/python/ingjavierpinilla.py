def check_2_strings(a:str,b:str):
    return [v for i, v in enumerate(b) 
            if len(a)==len(b) and 
            v is not a[i]]

if __name__=="__main__":
    a="testa"
    b="testb"
    print(check_2_strings(a,b))