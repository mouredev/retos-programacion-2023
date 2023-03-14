import requests  # pip3 install requests
from datetime import datetime

BASE_URL: str = "https://rickandmortyapi.com/api"


def call_rick_and_morty_api(endpoint: str = "/character") -> dict:
    """This function return all characters on rick and morty"""

    try:

        print(f"fecha de consulta: {datetime.now()}")

        if endpoint is not None:
            endpoint: str = "/character"
            response_data = requests.get(f"{BASE_URL}/{endpoint}")

        assert response_data.status_code == 200

        return response_data.json()

    except requests.RequestException as request_error:
        raise requests.RequestException(
            f"error request produced: {request_error}")
    except ConnectionError as connection_error:
        raise ConnectionError(f"error of connection: {connection_error}")
    except TimeoutError as time_out:
        raise TimeoutError(f"request time out{time_out}")
    except Exception as exception:
        raise Exception(f"error produces: {exception}")


if __name__ == "__main__":
    print(call_rick_and_morty_api(endpoint=""))
