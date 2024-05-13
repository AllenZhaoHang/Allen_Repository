'''
    Test all the functions from LotteryAndWealth.py and tests 
    the results to see if the function works as expected.
    Hang Zhao
    10/12/2023
'''
from LotteryAndWealth import generateLotteryNumbers
from LotteryAndWealth import countMatches
from LotteryAndWealth import playLottery
from LotteryAndWealth import getDisparityMessage
from LotteryAndWealth import awardScholarship

def test_generateLotteryNumbers():
    '''
    test generateLotteryNumbers function
    Input:None
    Output: print the results
    '''
    # print random list first time
    print("first random 5 numbers: ", generateLotteryNumbers())
    # print random list second time
    print("second random 5 numbers: ", generateLotteryNumbers())


def test_countMatches():
    '''
    test countMatches function
    Input:None
    Output: print the results
    '''
    # first time execute
    guess_list = [29, 23, 20, 39, 32]
    random_list = generateLotteryNumbers()
    count_match = countMatches(guess_list, random_list)
    print("first random list is: ", random_list)
    print("first guess list is : ", guess_list)
    print("first countMatches is : ", count_match)

    # second time execute
    guess_list = [35, 23, 31, 22, 24]
    random_list = generateLotteryNumbers()
    count_match = countMatches(guess_list, random_list)
    print("second random list is: ", random_list)
    print("second guess list is : ", guess_list)
    print("second countMatches is : ", count_match)


def test_playLottery():
    '''
    test playLottery function
    Input:None
    Output: print the results
    '''
    # first test
    print("first test play lottery: ", playLottery())
    # second test
    print("second test play lottery: ", playLottery())

def test_getDisparityMessage():
    '''
    test getDisparityMessage function
    Input:None
    Output: print msg
    '''
    # first test
    highIncomeList = [5, 6, 10, 14]
    lowIncomeList = [1, 5, 7, 2]
    msg = getDisparityMessage(highIncomeList, lowIncomeList, 2020)
    print("first test msg is : ", msg)
    # second test
    highIncomeList = [4, 10, 2, 5, 8]
    lowIncomeList = [2, 7, 12]
    msg = getDisparityMessage(highIncomeList, lowIncomeList, 2020)
    print("second test msg is : ", msg)


def test_awardScholarship():
    '''
    test awardScholarship function
    Input:None
    Output: None
    '''
    # first test
    incomeList = [10, 15, 20, 25, 30]
    awardTotal = 10
    wealth_after_award = awardScholarship(incomeList, awardTotal)
    print("Wealth of Income Group after Awarding Scholarships:", wealth_after_award)
    # second test
    incomeList = [4, 5, 10, 15, 20]
    awardTotal = 8
    wealth_after_award = awardScholarship(incomeList, awardTotal)
    print("Wealth of Income Group after Awarding Scholarships:", wealth_after_award)


def main():
    '''
    main function, execute test functions
    Input:None
    Output:None
    '''
    # execute test_generateLotteryNumbers function
    #test_generateLotteryNumbers()
    # execute test_countMatches function
    #test_countMatches()
    # execute test_playLottery function
    #test_playLottery()
    # execute test_getDisparityMessage function
    #test_getDisparityMessage()
    # execute test_awardScholarship function
    test_awardScholarship()

if __name__ == '__main__':
    main()
