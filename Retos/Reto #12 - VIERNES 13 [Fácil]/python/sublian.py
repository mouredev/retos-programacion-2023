from datetime import datetime


def have_friday13(year: int, month: int,):
    """Esta funcion retorna una cadena indicando la existencia de un viernes 13 en el mes

    Args:
        year (int): 
        month (int): 

    Returns:
        _type_: none
    """
    date=datetime(year, month, 13)    
    if date.weekday() == 4:
        return (print("This month have a Friday 13"))          
    return(print("This month dont have a Friday 13"))
        

if __name__=="__main__":
    print("Please enter Year and month to calculate if this month have a Friday 13")
    year=int(input("Year: "))
    month=int(input("Month: "))
    have_friday13(year, month)
