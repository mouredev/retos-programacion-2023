URL = 'https://retosdeprogramacion.com?year=2023&challenge=0'

def extractParams(url: str) -> list:
    is_param = False
    element = []
    params = []

    for ch in url:
        if ch == '=':
            is_param = True
            continue

        if ch == '&':
            params.append(''.join(element))
            element = []
            is_param = False

        if is_param:
            element.append(ch)

    params.append(''.join(element))
    print(params)

    return params

if __name__ == '__main__':
    params = extractParams(url=URL)
