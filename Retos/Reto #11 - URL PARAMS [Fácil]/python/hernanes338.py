# Example URL with 2 key=value pairs
url = 'https//www.domain.com/page?key1=value1&key2=value2&key3=value3&key4=value4'

## 1. Get the url string after the '?' with split("?")[1]
## 2. Get the different key=value pairs with split("&")
## 3. For each key=value pair, get the string after the '=' with split("=")[1]

def get_parameter_values(url):
    return list(key_value.split("=")[1] for key_value in url.split("?")[1].split("&"))

## Start program execution ##

print(get_parameter_values(url)) # Result: ['value1', 'value2', 'value3', 'value4']

## End program execution ##