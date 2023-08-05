def get_params(url: str) -> list:
    params_string = url.split("?")[1]
    return [param.split("=")[1] for param in params_string.split("&")]


print(get_params("https://retosdeprogramacion.com?year=2023&challenge=0"))
