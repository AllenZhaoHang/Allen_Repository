"""
    HANG ZHAO
    09/17/2023
    Write a program that completes and prints out
    the following truth table.
"""
# Write a program that completes and prints out
# the following truth table.


def main():
    t = True
    f = False
    p = t
    q = t
    r = t
    wordA = ""
    wordB = ""
    print("+---+---+---+---+---+")
    print("| p | q | r | A | B |")
    print("+---+---+---+---+---+")
    # print second line
    p = f
    q = f
    r = f
    A = (p and q) or not r
    B = not (p and (q or not r))
    if A == t:
        wordA = 'T'
    else:
        wordA = 'F'
    if B == t:
        wordB = 'T'
    else:
        wordB = 'F'
    print("| F | F | F | " + wordA + " | " + wordB + " |")
    print("+---+---+---+---+---+")
    # print third line
    p = f
    q = f
    r = t
    A = (p and q) or not r
    B = not (p and (q or not r))
    if A == t:
        wordA = 'T'
    else:
        wordA = 'F'
    if B == t:
        wordB = 'T'
    else:
        wordB = 'F'
    print("| F | F | T | " + wordA + " | " + wordB + " |")
    print("+---+---+---+---+---+")
    # print fourth line
    p = f
    q = t
    r = f
    A = (p and q) or not r
    B = not (p and (q or not r))
    if A == t:
        wordA = 'T'
    else:
        wordA = 'F'
    if B == t:
        wordB = 'T'
    else:
        wordB = 'F'
    print("| F | T | F | " + wordA + " | " + wordB + " |")
    print("+---+---+---+---+---+")
    # print fiveth line
    p = f
    q = t
    r = t
    A = (p and q) or not r
    B = not (p and (q or not r))
    if A == t:
        wordA = 'T'
    else:
        wordA = 'F'
    if B == t:
        wordB = 'T'
    else:
        wordB = 'F'
    print("| F | T | T | " + wordA + " | " + wordB + " |")
    print("+---+---+---+---+---+")
    # print sixth line
    p = t
    q = f
    r = f
    A = (p and q) or not r
    B = not (p and (q or not r))
    if A == t:
        wordA = 'T'
    else:
        wordA = 'F'
    if B == t:
        wordB = 'T'
    else:
        wordB = 'F'
    print("| T | F | F | " + wordA + " | " + wordB + " |")
    print("+---+---+---+---+---+")
    # print seventh line
    p = t
    q = f
    r = t
    A = (p and q) or not r
    B = not (p and (q or not r))
    if A == t:
        wordA = 'T'
    else:
        wordA = 'F'
    if B == t:
        wordB = 'T'
    else:
        wordB = 'F'
    print("| T | F | T | " + wordA + " | " + wordB + " |")
    print("+---+---+---+---+---+")
    # print eighth line
    p = t
    q = t
    r = f
    A = (p and q) or not r
    B = not (p and (q or not r))
    if A == t:
        wordA = 'T'
    else:
        wordA = 'F'
    if B == t:
        wordB = 'T'
    else:
        wordB = 'F'
    print("| T | T | F | " + wordA + " | " + wordB + " |")
    print("+---+---+---+---+---+")
    # print nineth line
    p = t
    q = t
    r = t
    A = (p and q) or not r
    B = not (p and (q or not r))
    if A == t:
        wordA = 'T'
    else:
        wordA = 'F'
    if B == t:
        wordB = 'T'
    else:
        wordB = 'F'
    print("| T | T | T | " + wordA + " | " + wordB + " |")
    print("+---+---+---+---+---+")


if __name__ == "__main__":
    main()
