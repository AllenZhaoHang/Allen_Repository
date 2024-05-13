'''
    Hang Zhao
    9/19/2023
    return a lyric
'''


def old_macdonald(animal, sound):
    return (f"Old MacDonald had a farm, ee-igh, ee-igh, oh!\nAnd on that farm he had a {animal}, ee-igh, ee-igh, oh!\nWith a {sound}, {sound} here and a {sound}, {sound} there.\nHere a {sound}, there a {sound}, everywhere a {sound}, {sound}.\nOld MacDonald had a farm, ee-igh, ee-igh, oh!\n")


def main():
    animals = ["cow", "duck", "pig", "horse", "sheep"]
    sounds = ["moo", "quack", "oink", "neigh", "baa"]
    for i in range(5):
        verse = old_macdonald(animals[i], sounds[i])
        print(verse)


if __name__ == "__main__":
    main()
