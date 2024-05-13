'''
    Simulate a random sleepwalker using recursion. 
    At the end, you will do some mathematical analyses
    on the results to look at how randomness affects the output.
    Hang Zhao
    10/26/2023
'''
import random


def rs():
    ''' rs chooses a random step and returns it
    Note that a call to rs() requires parentheses
    Params: none
    Returns: None
    '''
    return random.choice([-1, 1])


def rwpos(start, nsteps):
    '''Simulate a random walk and return the final position.
    Params: start nsteps
    Return: return the final position
    '''
    if nsteps == 0:
        return start
    print("Start is", start)
    position = rwpos(start + rs(), nsteps - 1)
    print("Start is", position)
    return position


def rwsteps(start, low, hi):
    '''Simulate a random walk until low or hi is reached and return the number of steps taken.
    Params: start low hi
    Return: Returns the number of steps taken until the sleepwalker reaches
    at or beyond our low or hi value
    '''
    def step(position, steps):
        print("Start is", position)
        print("start|" + "-" * (position - low) + "*" + "-" * (hi - position) + "|end")
        if low <= position <= hi:
            new_position = position + rs()
            if low <= new_position <= hi:
                return step(new_position, steps + 1)
        return steps

    steps = step(start, 0)
    return steps


def rwposPlain(start, nsteps):
    '''Simulate a random walk without printing debugging information.
    Params: start nsteps
    Return: return the final position
    '''
    if nsteps == 0:
        return start
    else:
        return rwposPlain(start + rs(), nsteps - 1)


def avgSignedDisplacement(numtrials):
    '''Calculate the average signed displacement for numtrials.
    Params: numtrials
    Return: return the average signed displacement for numtrials.
    '''
    displacements = [rwposPlain(0, 100) for _ in range(numtrials)]
    return sum(displacements) / numtrials


def avgSquaredDisplacement(numtrials):
    '''Calculate the average squared displacement for numtrials.
    Params: numtrials
    Return: return the average of the square of the results.
    '''
    squared_displacements = [(rwposPlain(0, 100))**2 for _ in range(numtrials)]
    return sum(squared_displacements) / numtrials


def main():
    '''main function'''
    print(rs())


if __name__ == '__main__':
    main()
