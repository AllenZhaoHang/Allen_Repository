'''
    Tower of Hanoi
    Hang Zhao
    10/21/2023
'''


def tower_of_hanoi(disks, from_rod, to_rod):
    '''tower'''
    move_disk(disks, from_rod, to_rod)


def move_disk(disks, from_rod, to_rod):
    if disks == 1:
        move_one_disk(1, from_rod, to_rod)
    else:
        spare_rod = find_spare_rod(from_rod, to_rod)
        move_disk(disks-1, from_rod, spare_rod)
        move_one_disk(1, from_rod, to_rod)
        move_disk(disks-1, spare_rod, to_rod)


def move_one_disk(disks, from_rod, to_rod):
    print("Move disk ", disks, "from ", from_rod, " to ", to_rod)


def find_spare_rod(from_rod, to_rod):
    return 6 - (from_rod + to_rod)


def main():
    '''main'''
    tower_of_hanoi(5, 1, 3)


if __name__ == '__main__':
    main()
