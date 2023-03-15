def parametros_url(url):
    if url.find("?") == -1:
        print("parametros: None")

    else: 
        params = url.split("?")[1].split("&")
        list_params = []

        for param in params:
            p = param.split("=")[1]
            list_params.append(p)

        print(f"parametros: {list_params}")
    
parametros_url("https://retosdeprogramacion.com?year=2023&challenge=0")
parametros_url("https://www.youtube.com/watch?v=aNep_aklBEI")
parametros_url("https://www.youtube.com/watch?v=9y5EJYJ81zc")
parametros_url("https://rickandmortyapi.com/api/character/?page=2")
parametros_url("https://rickandmortyapi.com/api/character/?name=rick&status=alive")
parametros_url("https://www.google.com/")
