def get_params(url):
    params = []
    try:
        url_params = url.split("?")[1]
        for param in url_params.split("&"):
            try:
                if param.split("=")[1]:
                    params.append(param.split("=")[1])
            except:
                pass
        if len(params) > 0:
            return "Parámetros encontrados:", params
    except:
        pass
    return "No hay parámetros en la url"

if __name__ == "__main__":
    url = input("Introduce la url: ")
    print(get_params(url))