# File which will hold the main function for the IceCreamShoppe project
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by Hang Zhao
# 11/2/2023
import IceCreamShoppe
import Scoop


def main():
    '''main function'''
    # Ask the user for scoop radii and carton dimensions
    scoop_radii = []

    for i in range(2):
        radius = float(
            input(f"What is the radius of your {i + 1}st scooper? "))
        scoop_radii.append(radius)

    carton_radius = float(input("What is the radius of your carton? "))
    carton_height = float(input("What is the height of your carton? "))

    shoppe = IceCreamShoppe.IceCreamShoppe(carton_radius, carton_height)

    cartons_used = 0

    while True:
        more_ice_cream = int(
            input("Would you like more ice cream? (Enter 1 for yes and 0 for no) "))
        if more_ice_cream == 0:
            break

        scoops_2 = int(
            input(f"How many {scoop_radii[0]} scoops would you like? "))
        scoops_3 = int(
            input(f"How many {scoop_radii[1]} scoops would you like? "))
        scooper = Scoop.Scoop(scoop_radii[0])
        shoppe.serve(scoops_2, scooper)
        scooper = Scoop.Scoop(scoop_radii[1])
        shoppe.serve(scoops_3, scooper)
        cartons_used += 1

    print(f"You used {cartons_used} cartons of ice cream.")


if __name__ == "__main__":
    main()
