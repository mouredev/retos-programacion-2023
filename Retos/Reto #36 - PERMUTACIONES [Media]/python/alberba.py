def permutations(chars: list, currentIndex: int):
    if currentIndex == len(chars)-1:
        print(''.join(chars))

    for i in range(currentIndex, len(chars)):
        chars[currentIndex], chars[i] = chars[i], chars[currentIndex]
        permutations(chars, currentIndex+1)
        chars[currentIndex], chars[i] = chars[i], chars[currentIndex]

def find_permutations(chars: str):
    if chars is None or len(chars) == 0:
        return None
    permutations(list(chars), 0)

find_permutations("Lucas")