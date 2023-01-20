for num in range(1, 101):
    es_multiplo_tres = num % 3 == 0
    es_multiplo_cinco = num % 5 == 0

    if es_multiplo_tres and es_multiplo_cinco:
        print(f"{num} fizzbuzz")
    elif es_multiplo_tres:
        print(f"{num} fizz")
    elif es_multiplo_cinco:
        print(f"{num} buzz")
    else:
        print(f"{num}")
