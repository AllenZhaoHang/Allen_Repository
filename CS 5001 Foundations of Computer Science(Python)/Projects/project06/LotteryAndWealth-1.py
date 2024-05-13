'''
    Project 6: Lottery and Wealth
    The CS purpose of this project is to give you more
    experience with for loops, lists and functions.  Also,
    to look at how you can simulate real world experiences
    and draw conclusions from it.
    Hang Zhao
    10/12/2023
'''
import random
import numpy as np
import numpy as numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib


# ----------------- THE SIMULATION ----------------- #

def generateLotteryNumbers():
    """
    Returns a list of 5 random ints between 1 and 42, inclusive, with no
    duplicates.
    """
    # YOUR CODE HERE
    pass


def countMatches(my_list, lottery_list):
    """
    Returns the number of matches between my_list and lottery_list.
    Inputs: * my_list: A list of your lottery numbers.
            * lottery_list: A list of the winning numbers.
    """
    # YOUR CODE HERE
    pass


def playLottery():
    """
    Returns the reward after one lottery play.
    """
    # YOUR CODE HERE
    pass


def getDisparityMessage(highIncomeList, lowIncomeList, decade):
    """
    Returns a string that describes the percentages of wealth possessed by the
    higher income half and lower income half for any given year.
    Inputs: *highIncomeList: The list containing wealth values for the high
             income group.
            *lowIncomeList: The list containing wealth values for low income
             group.
            *decade: The current decade as an integer.
    """
    # YOUR CODE HERE

    lowIncomePercent =  # ???
    highIncomePercent =  # ???

    message = "Decade " + str(decade) + ": The high income group possesses " +\
        str(highIncomePercent) + "% of the community's wealth, while the low"\
        "income group possesses " + str(lowIncomePercent) +\
        "% of the community's wealth."

    return message


def simLottery(incomeList, numPlayers):
    """
    Simulates lottery play for a number of players from a given income group.
    Inputs: *incomeList: The list containing wealth values for the given
             income group.
            * numPlayers: The number of players who will play the lottery.
    """
    for i in range(numPlayers):
        # YOUR CODE HERE
        pass


def awardScholarship(incomeList, awardTotal):
    """
    Redistributes funds from the lottery in the form of a $1 scholarship.
    Inputs: *incomeList: The list containing wealth values for the given
             income group.
            *awardTotal: The total amount of lottery funds to be rewarded
             to members of this income group.
    """
    for i in range(awardTotal):
        # YOUR CODE HERE
        pass


def simCommunity(years, communitySize):
    """
    Simulates the movement of money between high income and low income
    communities via the Georgia lottery and scholarship system over several
    years. Half of the community is from low income backgrounds, and half from
    high income backgrounds. The resulting wealth disparity is printed as a
    message and displayed as a scatter plot indicating overall wealth per
    person per year.
    Inputs: *years: The number of years the simulation should be run.
            *communitySize: The number of people in the community.
    """

    # ---- PART 1: Populate Wealth Lists
    # Fill highIncomeList and lowIncomeList with starting wealth values.

    highIncomeList = []
    lowIncomeList = []

    # ---- PART 2: Populate Record Lists
    # Fill highIncomeRecord and lowIncomeRecord with the starting ("year 0")
    # values from highIncomeList and lowIncomeList.

    highIncomeRecord = []
    lowIncomeRecord = []

    # simulation loop
    for i in range(years):

        # ---- PART 3: Play the Lottery
        # Use the simLottery() function to simulate community
        # wealth interactions.

        # ---- PART 4: Award Scholarships
        # Use the awardScholarship() function to redistribute lottery funds
        # as scholarships.

        # ---- PART 5: Update Record Lists
        # Update the income records every year.

        if i % 10 == 0:
            # ---- PART 6: Display Wealth Distribution
            # Use getDisparityMessage() to display the wealth distribution
            # every decade.
            pass
    # ---- PART 7: Visualize the Simulation
    # Uncomment the next line to plot the simulation.
    # plotSim(highIncomeRecord, lowIncomeRecord)


# ----------------- HELPER FUNCTIONS ----------------- #
# These functions are provided for you to use.
# You do not need to change them, but feel free to explore what they do.

def plotSim(highIncomeRecord, lowIncomeRecord):
    """
    Helper function for simCommunity() to generate a scatterplot displaying
    the wealth of each person in the simulation over 8 decades. High income
    values are plotted in red. Low income values are plotted in blue.
    Inputs: *highIncomeRecord: A list of all high income wealth lists
            from each year.
            *lowIncomeRecord: A list of all low income wealth lists
             from each year.
    """
    x = np.arange(len(highIncomeRecord))

    # plot wealth records
    plotWealthRecord(x, highIncomeRecord, '#882255', '.')
    plotWealthRecord(x, lowIncomeRecord, '#44AA99', '*')

    # plot labels/legend
    plt.xlabel("Year")
    plt.ylabel("Wealth Value")
    magenta_patch = mpatches.Patch(color='#882255', label='High Income')
    teal_patch = mpatches.Patch(color='#44AA99', label='Low Income')
    plt.legend(handles=[magenta_patch, teal_patch])

    # display the plot
    plt.show()


def plotWealthRecord(x, record, markerColor, markerShape):
    """
    Helper function for plotSim(). Plots each individual wealth group.
    Inputs: *x: List of x-axis values.
            *record: The income record to be plotted.
            *markerColor: String defining the color of markers.
            *markerShape: String defining marker shape.
    """
    for i in range(len(record[0])):
        plotData = []
        for j in range(len(record)):
            plotData += [record[j][i]]
        plt.scatter(x, plotData, color=markerColor, marker=markerShape)


def simManyPlays(n):
    """
    Function to graph the total winnings of a player who plays the lottery
    n times.
    Inputs: *n: The number of times the player enters the lottery.
    """
    winnings = []
    reward = 0
    for i in range(n):
        reward += playLottery()
        winnings.append(reward)
    plt.xlabel("Number of Lottery Plays")
    plt.ylabel("Winnings")
    plt.plot(winnings)
    plt.legend()
    plt.show()

# ----------------- MAIN FUNCTION ----------------- #


def main():
    # Simulate 1000 plays by one person and plot the winnings.
    simManyPlays(1000)

    # Simulate a community playing Lottery 5 with 30 people for 80 years.
    # simCommunity(80, 30)

if __name__ == "__main__":
    main()
