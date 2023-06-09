

def url_params(url: str) -> list[str] | str:
    try:
        match url:
            case signo if "?" not in signo:
                return f"esta url no tiene parametros: {url}"

            case signo2 if "&" not in signo2:
                params: str = [None if url.split("?")[1].split(
                    "=")[1] == "" else url.split("?")[1].split("=")[1]]
            case _:
                params: str = [None if param.split("=")[1] == ""
                               else param.split("=")[1] for param in url.split("?")[1].split("&")]
    except (IndexError) as error:
        print(f"revisa bien tu url: {error}")
        return []

    else:

        result = [param for param in params if param != None]
        #result = list(filter(lambda param: param != None, params))

        if not result:
            return "los parametros de la url no tiene valores asociados"
        return result


if __name__ == "__main__":
    print(url_params(
        url="https://retosdeprogramacion.com?year=2023&challengue=0&age=25"))
