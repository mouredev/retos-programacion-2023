def get_params(url: str) -> dict:
    params = url.split("?")[1].split("&")
    return [param.split("=")[1] for param in params]


print(get_params("http://example.com?product=1234&utm_source=google"))
print(get_params("https://retosdeprogramacion.com?year=2023&challenge=0"))
