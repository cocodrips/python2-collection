"""
snake_case => camelCase
camelCase => snake_case
"""

def is_snake_case(word):
    if "_" in word :
        return True
    return False

def translate(word):
    new_word = ""
    if is_snake_case(word):
        is_next_upper = False
        for c in word:
            if c == "_":
                is_next_upper = True
            else:
                if is_next_upper:
                    is_next_upper = False
                    new_word += c.upper()
                else:
                    new_word += c
    else:
        for c in word:
            if c.upper() == c:
                new_word += "_"
            new_word += c.lower()

    return new_word


if __name__ == '__main__':
    while True:
        word = raw_input().strip()
        print translate(word)
