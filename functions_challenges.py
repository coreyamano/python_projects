# 1. Tenth Power
# Let’s create some functions which can help us solve math problems! For this first function, we are going to take the tenth power of a number. In order to do this we need to do three things:

# Set up the function header for tenth_power which accepts one parameter
# Take the tenth power of the input value
# Return the result

def tenth_power(num):
    return num ** 10

# 2. Square Root
# Another useful function for solving math problems is the square root function. We can create this using similar steps from the last problem. The code will look very similar. We need to:

# Set up the function header for square_root which accepts one parameter
# Take the square root of the input value
# Return the result


def square_root(num):
    return num ** .5

# 3. Win Percentage
# Next, we will create a function which calculates the percentage of games won. In order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games. For this function, there will be two input parameters, the number of wins and the number of losses. We also need to make sure that we return the result as a percentage (in the range of 0 to 100). In order to create this method we need the following steps:

# Define the function header with two parameters, wins and losses
# Calculate the total number of games using the number of wins and losses
# Get the ratio of winning using the number of wins out of the total number of games.
# Convert the ratio to a percentage
# Return the percentage


def win_percentage(wins, losses):
    return wins/(wins+losses) * 100

# 4. Average
# Let’s create a function which takes the average of two numbers. These two numbers will be the input of the function and the output will be the average of the two. In order to do this, we need to do a few steps:

# Define the function with two input parameters, num1 and num2
# Calculate the sum of the two numbers
# Divide the sum by the number of inputs to the function
# Return the answer


def average(num1, num2):
    return (num1 + num2)/2

# 5. Remainder
# For the final challenge in this group, we are going to take the remainder of two numbers while performing other mathematical operations on them. We are going to multiply the numerator by 2 and divide the denominator by 2. After the two values have been modified, we will divide them and return the remainder. In order to do this we will need to:

# Define the function to accept two parameters
# Multiply the first input value by 2
# Divide the second input value by 2
# Calculate the remainder of the modified first input value divided by the modified second input value (using modulus)
# Return the answer


def remainder(num1, num2):
    return (2*num1) % (num2/2)
