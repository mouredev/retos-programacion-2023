def url_mod(url):
    url = url.split('?')
    if len(url) < 2:
        return f'no hay parametros'
    return [params.split('=')[1] for params in url[1].split('&')  ]
