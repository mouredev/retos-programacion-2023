import datetime


def viernes_trece(year, month):

    date = datetime.date(year, month, 13)

    if date.weekday() == 4:
        return True
    else:
        return False


# se espera un resultado falso de la fecha datetime.MAXYEAR(9999) y el mes 1(enero)
def test_invalid_year_1():
    assert not viernes_trece(datetime.MAXYEAR, 1)


# se espera un resultado falso de la fecha 1900 de enero
def test_no_viernes_trece():
    assert not viernes_trece(1900, 1)


# se espera un resultado verdadero de la fecha 2023 de enero
def test_si_viernes_trece():
    assert viernes_trece(2023, 1)

# --!! run: pytest pyramsd.py
