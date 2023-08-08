import requests

def extract_params(url):
    
    mixed_params = url.split("?")[1]
    mixed_params_sep = mixed_params.split("&")
    params_dict = dict()
    for param in mixed_params_sep:
        param_sep = param.split("=")
        params_dict[param_sep[0]] = param_sep[1]
        
    return params_dict

                                              
if __name__ == "__main__":

    url = "https://retosdeprogramacion.com?year=2023&challenge=0"
    params_dict = extract_params(url)
    params_values = list(params_dict.values())
    print(params_dict)
    print(params_values)