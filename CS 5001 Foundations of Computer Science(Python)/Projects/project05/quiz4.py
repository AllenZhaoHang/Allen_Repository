'''
    Module 6 Quiz question 4
    Write a function that has a list as
    its parameter and prints out 5 times each element
    in the list.
'''
import numpy as np


def mutiple(list):
    '''
    a function that has a list as
    its parameter and prints out 5 times each element
    Input: a list
    Output: None
    '''
    for i in range(len(list)):
        list[i] *= 3
    return list

def print_locations(board):
    for x in board:
        for y in x:
            print(y, end=' ')
        print() 

def main():
    '''
    main function
    Input:None
    Output:None
    '''
    # num_list = [1, 2, 3, 4, 5]
    # num_list = mutiple(num_list)
    # print(num_list)
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_locations(board)

if __name__ == '__main__':
    main()
