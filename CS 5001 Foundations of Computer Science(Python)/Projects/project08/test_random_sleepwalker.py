'''
    Test Random Sleepwalker
    Hang Zhao
    10/26/2023
'''
from Lab7RandomSleepwalker import rwpos
from Lab7RandomSleepwalker import rwsteps
from Lab7RandomSleepwalker import rwposPlain
from Lab7RandomSleepwalker import avgSignedDisplacement
from Lab7RandomSleepwalker import avgSquaredDisplacement


def test_rwpos():
    ''' test rwpos() function '''
    expected_result = 42
    result1 = rwpos(40, 20)
    print("test rwpos() function, expected result:",
          expected_result, "actual result: ", result1)


def test_rwsteps():
    ''' test rwsteps() function'''
    expected_result = 216
    result3 = rwsteps(40, 10, 60)
    print("test rwsteps() function, expected result:",
          expected_result, "actual result: ", result3)

def test_rwposPlain():
    ''' test rwposPlain() function '''
    expected_result = 42
    result5 = rwposPlain(40, 4)
    print("test rwposPlain() function, expected result:",
          expected_result, "actual result: ", result5)


def test_avgSignedDisplacement():
    ''' test avgSignedDisplacement() function '''
    expected_result = 0.41
    result7 = avgSignedDisplacement(1000)
    print("test avgSignedDisplacement() function, expected result:",
          expected_result, "actual result: ", result7)


def test_avgSquaredDisplacement():
    '''test avgSquaredDisplacement() function'''
    expected_result = 107.76
    result9 = avgSquaredDisplacement(1000)
    print("test avgSquaredDisplacement() function, expected result:",
          expected_result, "actual result: ", result9)


def main():
    '''main function'''
    # test rwpos() function
    test_rwpos()
    # test rwsteps() function
    test_rwsteps()
    # test rwposPlain() function
    test_rwposPlain()
    # test avgSignedDisplacement() function
    test_avgSignedDisplacement()
    # test avgSquaredDisplacement() function
    test_avgSquaredDisplacement()


if __name__ == '__main__':
    main()
