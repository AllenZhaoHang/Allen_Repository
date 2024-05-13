"""
    HANG ZHAO
    09/17/2023
     reads in a word from the keyboard and prints
     "Hi, how are you" and "Done" if someone enters
     the word "Hi" (capitalization matters). Otherwise
     it just prints "Done".
"""
#  reads in a word from the keyboard and prints
# "Hi, how are you" and "Done"


def main():
    word = input("")
    if (word == 'Hi'):
        print("Hi, how are you?")
        print("Done")
    else:
        print("Done")


if __name__ == "__main__":
    main()
