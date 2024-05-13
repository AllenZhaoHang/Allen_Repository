'''
    Recursion
    Hang Zhao
    10/17/2023
'''


def iter_factorial(x):
    ''' '''
    answer = 1
    for i in range(1, x+1):
        answer *= i
    return answer


def recur(x):
    if x==1:
        return 1
    else:
        return recur(x-1)*x

def recur_add(x):
    ''''''
    if x == 1 or x == 2:
        return 1
    else:
        return recur_add(x-1) + recur_add(x-2)

def recur_sum_up(start, stop):
    ''' '''
    if start == stop:
        return start
    return start + recur_sum_up(start+1, stop)

def recur_sum_down(start, stop):
    ''' '''
    if start == stop:
        return start
    return recur_sum_up(start, stop-1) + stop

def main():
    #print(iter_factorial(5))
    #print(recur(5))
    #print(recur_add(6))
    print(recur_sum_down(10, 15))
    print(recur_sum_up(10, 15))
if __name__ == '__main__':
    main()
