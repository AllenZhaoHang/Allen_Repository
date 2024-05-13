'''
'''


def numJewelsInStones(self, jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    jewel_set = set()
    for jewel in jewels:
        jewel_set.add(jewel)
    count = 0
    for stone in stones:
        if stone in jewel_set:
            count += 1
    return count

