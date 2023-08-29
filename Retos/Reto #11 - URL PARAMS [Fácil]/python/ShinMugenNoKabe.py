def get_paramteres(url: str) -> list[str]:
    if not "?" in url:
        return []
    
    query = url.split("?")[1]
    params = query.split("&")
    
    return [param.split("=")[1] for param in params]
    
    
if __name__ == "__main__":
    result = get_paramteres("https://retosdeprogramacion.com?year=2023&challenge=0")
    assert result == ["2023", "0"]
    print(result)