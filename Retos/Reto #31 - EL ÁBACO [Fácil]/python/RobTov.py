# One line solution

def read_abbacus(abbacus: list) -> str:
    return ''.join(f'{len(r[:r.index("-")])}.' if abbacus.index(r) == 0 or abbacus.index(r) == 3 else str(len(r[:r.index('-')])) for r in abbacus)


if __name__ == '__main__':
    print(read_abbacus(
        [
            'O---OOOOOOOO',
            'OOO---OOOOOO',
            '---OOOOOOOOO',
            'OO---OOOOOOO',
            'OOOOOOO---OO',
            'OOOOOOOOO---',
            '---OOOOOOOOO'
        ]
    ))
