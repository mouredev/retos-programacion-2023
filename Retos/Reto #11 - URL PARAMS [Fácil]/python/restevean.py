"""
Exercise
"""


def get_url_parameters(url):
    # Split the URL into the base part and the query string
    parts = url.split('?')

    # If there are no parameters, return an empty list
    if len(parts) < 2:
        return []

    # Get the query string part
    query_string = parts[1]

    # Split the query string into key-value pairs
    pairs = query_string.split('&')

    # Extract the values from the key-value pairs
    values = []
    for pair in pairs:
        key_value = pair.split('=')
        if len(key_value) == 2:
            values.append(key_value[1])
        else:
            values.append('')

    return values


if __name__ == '__main__':
    url = "https://retosdeprogramacion.com?year=2023&challenge=0"
    parameters = get_url_parameters(url)
    print(parameters)
