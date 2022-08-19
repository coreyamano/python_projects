# 1. Every Three Numbers
# Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3 starting from a number that is passed to the function as an input parameter. Here is what we need to do:

# Define the function to accept one parameter for our starting number
# Calculate the numbers between the starting number and 100 while incrementing by 3
# Store the numbers in a list
# Return the list

# 2. Remove Middle
# Our next function will remove all elements from a list with an index within a certain range. The function will accept a list, a starting index, and an ending index. All elements with an index between the starting and ending index should be removed from the list. Here are the steps:

# Define the function to accept three parameters: the list, the starting index, and the ending index
# Get all elements before the starting index
# Get all elements after the ending index
# Combine the two partial lists into the result
# Return the result

# 3. More Frequent Item
# Let’s go back to our factory example. We have a conveyor belt of items where each item is represented by a different number. We want to know, out of two items, which one shows up more on our belt. To solve this, we can use a function with three parameters. One parameter for the list of items, another for the first item we are comparing, and another for the second item. Here are the steps:

# Define the function to accept three parameters: the list, the first item, and the second item
# Count the number of times item1 shows up in our list
# Count the number of times item2 shows up in our list
# If item1 shows up more, return item1. Otherwise, return item2

# 4. Double Index
# Our next function will double a value at a given position. We will provide a list and an index to double. This will create a new list by replacing the value at the index provided with double the original value. If the index is invalid then we should return the original list. Here is what we need to do:

# Define the function to accept two parameters, one for the list and another for the index of the value we are going to double
# Test if the index is invalid. If its invalid then return the original list
# If the list is valid then get all values up to the index and store it as a new list
# Append the value at the index times 2 to the new list
# Add the rest of the list from the index onto the new list
# Return the new list

# 5. Middle Item
# For the final code challenge, we are going to create a function that finds the middle item from a list of values. This will be different depending on whether there are an odd or even number of values. In the case of an odd number of elements, we want this function to return the exact middle value. If there is an even number of elements, it returns the average of the middle two elements. Here is what we need to do:

# Define the function to accept one parameter for our list of numbers
# Determine if the length of the list is even or odd
# If the length is even, then return the average of the middle two numbers
# If the length is odd, then return the middle number
