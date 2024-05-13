import time
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev_prev = 0
        prev = 1
        for i in range(2, n+1):
            current = prev + prev_prev
            prev_prev = prev
            prev = current
        return current
def main():
    # Test the performance of the two functions
    start_time = time.time()
    print(fibonacci(30))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(fibonacci_iterative(30))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
