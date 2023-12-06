SUPPORTED_OPERATIONS = "+-*/%"


def verify_expression(operation: str) -> bool:
    operation_lst = operation.split()
    if len(operation_lst) % 2 == 0:
        return False
    for i, v in enumerate(operation_lst):
        if i % 2 == 0:
            try:
                int(v)
            except:
                return False
        else:
            if v not in SUPPORTED_OPERATIONS:
                return False
    return True


if __name__ == "__main__":
    operation = input("Ingrese una operacion: ")
    print(verify_expression(operation))
