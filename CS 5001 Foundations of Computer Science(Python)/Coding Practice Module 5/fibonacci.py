'''
    Coding Practice Module 5
    takes a single positive integer value
    and returns a list that contains the first
    n Fibonacci numbers. The Fibonacci sequences
    starts 1, 1, 2, 3, 5, 8, ...
    Hang Zhao
    10/07/2023
'''


def fibonacci(n):
    '''
    takes a single positive integer value
    and returns a list that contains the first
    n Fibonacci numbers. The Fibonacci sequences
    starts 1, 1, 2, 3, 5, 8, ...
    Input: a integer
    Output: a list
    '''
    listt = [1, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    while len(listt) < n:
        next_fib = listt[-1] + listt[-2]
        listt.append(next_fib)
    return listt


def main():
    '''
    main function
    Input: None
    Output: None
    '''
    re_list = fibonacci(10)
    print(re_list)


if __name__ == "__main__":
    main()
