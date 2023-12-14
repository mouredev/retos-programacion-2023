import requests
import pandas as pd


def web_request(url: str):

    data = None

    url = url.replace(' ', '%20').replace('#', '%23').replace('[', '%5B').replace(']', '%5D')

    request = requests.get(url)
    if request.status_code == 200:
        try:
            data = request.json()["payload"]["tree"]["items"]
        except Exception:
            pass
    return data


def load_data_from_excel(nombre_fichero: str) -> pd.DataFrame:

    try:
        fichero = pd.ExcelFile(nombre_fichero)
        with fichero as f:
            tabla = pd.read_excel(f, "Sheet1")
    except Exception:
        tabla = pd.DataFrame.from_dict({})

    return tabla


def load_data_from_web() -> pd.DataFrame:

    data_dict = {"Reto": [], "Lenguaje": [], "Usuario": []}
    avance = 0

    retos = web_request(URL_BASE)
    if retos:
        for reto in retos:
            url_reto = URL_BASE + reto['path'][5:]
            lenguajes = web_request(url_reto)
            if lenguajes:
                for lenguaje in lenguajes:
                    if lenguaje['name'] != "ejercicio.md":
                        url_lenguaje = url_reto + "/" + lenguaje['name']
                        usuarios = web_request(url_lenguaje)
                        if usuarios:
                            for usuario in usuarios:
                                avance += 1
                                print(avance, end='\r')
                                data_dict["Reto"].append(reto['name'])
                                data_dict["Lenguaje"].append(lenguaje['name'])
                                data_dict["Usuario"].append(usuario['name'].rsplit('.')[0])
        tabla = pd.DataFrame.from_dict(data_dict)
        tabla.to_excel("Retos.xlsx")
    else:
        tabla = pd.DataFrame.from_dict({})

    return tabla


def select_input_type() -> str:

    entrada = "x"

    while entrada not in ("w", "web", "e", "excel"):

        entrada = input("Carga de datos desde Web o Excel? [W|E]: ").lower()

    print("\n")

    return entrada


def print_results(data: pd.DataFrame) -> None:
    print(f"\nTotal de entradas: {data['Reto'].count()}",end="\n" + "-" * 30 + "\n" )

    print("Reto con más entradas:")
    filtro = data.groupby(["Reto"]).count().sort_values("Lenguaje").groupby(level=0).tail(1).iloc[[-1]]
    print(pd.DataFrame(filtro["Lenguaje"]), end="\n" + "-" * 30 + "\n")      # así NO parece la fila de dtype

    print("Lenguaje con más entradas:")
    filtro = data.groupby(["Lenguaje"]).count().sort_values("Reto").groupby(level=0).tail(1).iloc[[-1]]
    print(pd.DataFrame(filtro["Reto"]), end="\n" + "-" * 30 + "\n")

    print("Usuario con más entradas:")
    filtro = data.groupby(["Usuario"]).count().sort_values("Reto").groupby(level=0).tail(1).iloc[[-1]]
    print(pd.DataFrame(filtro["Reto"]), end="\n" + "-" * 30 + "\n")

    print("Usuario con más aportes por Reto:")
    filtro = data.groupby(["Usuario", "Reto"]).count().sort_values("Lenguaje").groupby(level=0).tail(1).iloc[[-1]]
    print(pd.DataFrame(filtro["Lenguaje"]), end="\n" + "-" * 30 + "\n")

    print("Usuario con más aportes por Lenguaje")
    filtro = data.groupby(["Usuario", "Lenguaje"]).count().sort_values("Reto").groupby(level=0).tail(1).iloc[[-1]]
    print(pd.DataFrame(filtro["Reto"]), end="\n" + "-" * 30 + "\n")

    print("Reto con más entradas por Lenguaje:")
    filtro = data.groupby(["Reto", "Lenguaje"]).count().sort_values("Usuario").groupby(level=0).tail(1).iloc[[-1]]
    print(pd.DataFrame(filtro["Usuario"]), end="\n")


URL_BASE = "https://github.com/mouredev/retos-programacion-2023/tree/main/Retos"
pd.set_option('display.max_rows', None)      # Solo para probar el retorno con print(df)
pd.set_option('display.max_columns', None)   # Solo para probar el retorno con print(df)
pd.set_option('expand_frame_repr', False)

retos_mouredev = load_data_from_web() if select_input_type() == "w" else load_data_from_excel("Retos.xlsx")
if retos_mouredev.__len__() > 0:
    print_results(retos_mouredev)
else:
    print("Oops... no se encontró nada!")
