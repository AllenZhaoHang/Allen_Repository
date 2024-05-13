"""
    HANG ZHAO
    09/17/2023
    reads in the price of a six-pack of soda
    and the price of a two-liter bottle. The program
    should print out the price per liter for both assuming
    that cans are 12 oz or 0.355 liters.
"""
# reads in the price of a six-pack of soda and the price of a two-liter bottle.


def main():
    per_six_pack = float(input("Price per six-pack: "))
    per_two_liter = float(input("Price per two-liter: "))
    six_pack_per_liter = per_six_pack / (6 * 0.355)
    two_liter_price_per_liter = per_two_liter / 2
    print("Six-pack price per liter: " + str(six_pack_per_liter))
    print("Two-liter price per liter: " + str(two_liter_price_per_liter))


if __name__ == "__main__":
    main()
