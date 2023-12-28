import datetime

def friday_13(year: int, month: int) -> bool:
    try:
        return datetime.date(year, month, 13).weekday() == 4
    except:
        return False

def test_friday_13_true_date():
    assert friday_13(2023, 1)

def test_friday_13_false_date():
    assert not friday_13(2023, 3)

def test_friday_13_invalid_year():
    assert not friday_13("2023", 1)
    assert not friday_13("MoureDev", 1)
    assert not friday_13(-2023, 1)

def test_friday_13_invalid_month():
    assert not friday_13(2023, "1")
    assert not friday_13(2023, "one")
    assert not friday_13(2023, -1)

def test_friday_13_invalid_data():
    assert not friday_13("Brais", "Moure")