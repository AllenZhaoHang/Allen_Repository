"""
    Hang Zhao
    9/18/2023
    caculate volume of the sphere
"""
# caculate volume of the sphere


def volume_sphere(radius):
    volume = (4 / 3) * 3.14159 * (radius ** 3)
    return volume


def main():
    radius = float(input())
    print(volume_sphere(radius))


if __name__ == "__main__":
    main()
