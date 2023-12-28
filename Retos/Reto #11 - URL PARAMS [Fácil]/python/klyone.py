#!/usr/bin/env python3

def add_new_parameter(parameters, param, value):
    parameters.append({param : value})

def search_parameter_delimiter(url):
    delimiter_index = -1
    if url == "":
        return delimiter_index

    for i in range(len(url)):
        c = url[i]
        if c == "?":
            delimiter_index = i
            break

    return delimiter_index

def is_parameter_valid(name, value, filling):
    return (name != "" and ((not filling) or (filling and value != "")))

def extract_url_parameters(url):
    parameters = []

    delimiter_index = search_parameter_delimiter(url)
    if delimiter_index == -1:
        return []

    parameter_name = ""
    parameter_value = ""
    filling_parameter_value = False

    for i in range(delimiter_index+1, len(url)):
        c = url[i]
        if c == "=":
            parameter_value = ""
            filling_parameter_value = True
        elif c == "&":
            if is_parameter_valid(parameter_name, parameter_value, filling_parameter_value):
                add_new_parameter(parameters, parameter_name, parameter_value)
            filling_parameter_value = False
            parameter_name = ""
            parameter_value = ""
        else:
            if filling_parameter_value:
                parameter_value = parameter_value + c
            else:
                parameter_name = parameter_name + c

    if is_parameter_valid(parameter_name, parameter_value, filling_parameter_value):
        add_new_parameter(parameters, parameter_name, parameter_value)

    return parameters

if __name__ == "__main__":
    print(extract_url_parameters(""))
    print(extract_url_parameters("http://myweb.com"))
    print(extract_url_parameters("https://www.myweb.com"))
    print(extract_url_parameters("http://myweb.com?"))
    print(extract_url_parameters("http://myweb.com?a"))
    print(extract_url_parameters("http://myweb.com?a="))
    print(extract_url_parameters("http://myweb.com?a=hello"))
    print(extract_url_parameters("http://myweb.com?a=hello&"))
    print(extract_url_parameters("http://myweb.com?a=hello&b"))
    print(extract_url_parameters("http://myweb.com?a=hello&b="))
    print(extract_url_parameters("http://myweb.com?a=hello&b=bye"))
    print(extract_url_parameters("http://myweb.com?a=hello&b=bye&"))
    print(extract_url_parameters("http://myweb.com?a=hello&b=bye&c"))
    print(extract_url_parameters("http://myweb.com?a=hello&b=bye&c="))
    print(extract_url_parameters("http://myweb.com?a=hello&b=bye&c=hey"))
    print(extract_url_parameters("http://myweb.com?a=hello&b&c=hey"))
    print(extract_url_parameters("http://myweb.com?a=hello&b=&c=hey"))
    print(extract_url_parameters("http://myweb.com?a=hello&&c=hey"))
