import requests

def api_call():
    
    resp = requests.get("http://api.open-notify.org/iss-now.json")
    #print(resp.json())
    return resp.json()
                                              
if __name__ == "__main__":

    resp = api_call()
    print(resp)