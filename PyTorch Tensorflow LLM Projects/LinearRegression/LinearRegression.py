# this file implements a simple linear regression algorithm
# utilizes gradient descent and two features to yield the optimal linear
# function for a given randomly selected set of data
# uses matplotlib plotting library to visualize data set and function that is fitted to it

from random import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")


# global variable holds value of learning rate
# convergence threshold determines when the iterations of regression end
ALPHA = .01
CONVERGENCE_THRESHOLD = .00001

# contains global variable for size of data set and maximum value in data set
DATA_SET_SIZE = 20
MAXIMUM_RANDOM_VALUE = 10

# stores number of iterations that the main loop executes
ITERATIONS = 100000

# contains sets of values for which function is being fitted
# below list is the data set for linear regression
x_values = []
y_values = []

# populates x_values and y_values lists
# obtains DATA_SET_SIZE random values for data set


def getDataSet():
	for x in range(1, DATA_SET_SIZE):
		# appends value into x and random correponding value into y
		x_values.append(x)
		y_values.append(x + x*(random() - .5))

# hypothesis for linear regression: h(x) = theta0 + theta1*x
# function used to calculate the error for a given hypothesis


def obtainOutput(theta0, theta1, x):
	return theta0 + theta1*x

# finds update value for theta0 at each step of regression
# this value is subtracted from theta0 to find next value


def getThetaZeroCost(theta0, theta1):
	sum = 0
	for index in range(len(x_values)):
		# find difference between predicted value and actual value
		sum += (obtainOutput(theta0, theta1, x_values[index]) - y_values[index])
	# return sum of differences mulitplied learning rate divided by size of data set
	return (ALPHA*sum)/float(len(x_values))

# finds update value for theta1 at each step of regression
# this value is subtracted from theta1 to find next value


def getThetaOneCost(theta0, theta1):
	sum = 0
	for index in range(len(x_values)):
		# find difference between predicted value and actual value
		# multiply each difference by current x_value in data set
		sum += (obtainOutput(theta0, theta1,
		        x_values[index]) - y_values[index])*x_values[index]
	# return sum multiplied by learning rate and divided by size of data set
	return (ALPHA*sum)/float(len(x_values))

# main loop of linear regression algorithm
# finds optimal line to fit to the given data set
# implements batch gradient descent for linear regression
# return values of theta0 and theta1 that are obtained from the regression loop


def mainLoop():
	# intialize theta0 and theta1 to 0 at beginning of loop
	theta0 = 0
	theta1 = 0
	# update values are changes to features during each iteration of regression
	theta1_update = 1
	theta0_update = 1  # Initialize theta0_update
	# repeat iterations until convergence
	while (np.fabs(theta1_update) > CONVERGENCE_THRESHOLD or np.fabs(theta0_update) > CONVERGENCE_THRESHOLD):
		# must calculate cost for both variables before updating
		theta0_update = getThetaZeroCost(theta0, theta1)
		theta1_update = getThetaOneCost(theta0, theta1)
		theta0 -= theta0_update
		theta1 -= theta1_update
	# return final values of theta0 and theta1
	return (theta0, theta1)

# main driver function for linear regression


def main():
	# populate data set with random values
	getDataSet()
	# show data to user before running regression algorithm
	plt.title("Data Set")
	plt.xlabel("Input Values")
	plt.ylabel("Output Values")
	plt.scatter(x_values, y_values)
	plt.show()
	input("Enter anything to run linear regression and obtain result.")
	# obtain result for given data set and graph for user
	result_x = x_values
	result_y = []
	featureVals = mainLoop()
	# obtain all values to graph result of linear regression
	for currInput in result_x:
		result_y.append(obtainOutput(featureVals[0], featureVals[1], currInput))
	plt.title("Linear Regression Result")
	plt.xlabel("Input Values")
	plt.ylabel("Output Values")
	plt.scatter(x_values, y_values)
	plt.plot(result_x, result_y)
	plt.show()
	input("Enter anything to end program.")


# run main function if the program is run from terminal
if __name__ == "__main__":
	# run main function
	main()
