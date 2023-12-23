def convert_to_octal_hexadecimal(decimal_number):
    """
    Convert a decimal number to Octal and Hexadecimal.

    Args:
        decimal_number (int): The decimal number to convert.

    Returns:
        tuple: A tuple containing the Octal and Hexadecimal representations.
    """
    octal_result, hexadecimal_result = convert_to_base(decimal_number, 8), convert_to_base(decimal_number, 16)
    return octal_result, hexadecimal_result

def convert_to_base(decimal, base):
    """
    Convert a decimal number to the specified base.

    Args:
        decimal (int): The decimal number to convert.
        base (int): The base to convert to.

    Returns:
        str: The converted number in the specified base.
    """
    digits = "0123456789ABCDEF"
    result = []

    while decimal >= base:
        result.append(digits[decimal % base])
        decimal //= base

    result.append(digits[decimal])
    reversed_result = result[::-1]

    return "".join(reversed_result)

decimal_number = 255
octal, hexadecimal = convert_to_octal_hexadecimal(decimal_number)
print(f"The decimal number {decimal_number} converts to octal as {octal}")
print(f"The decimal number {decimal_number} converts to hexadecimal as {hexadecimal}")
