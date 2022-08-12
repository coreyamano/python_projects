# Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

# Ground Shipping

# Weight of Package	Price per Pound	Flat Charge
# 2 lb or less	$1.50	$20.00
# Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
# Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
# Over 10 lb	$4.75	$20.00

# Ground Shipping Premium

# Flat charge: $125.00

# Drone Shipping

# Weight of Package	Price per Pound	Flat Charge
# 2 lb or less	$4.50	$0.00
# Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
# Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
# Over 10 lb	$14.25	$0.00

# Ground Shipping:
# 1. First things first, define a weight variable and set it equal to any number.

weight = 8
# 2. Next, we need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table above.

# Write a comment that says “Ground Shipping”.
# Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.

# Ground Shipping


def ground_shipping(weight):
    if weight <= 2:
        cost = weight * 1.50 + 20
    elif weight > 2 and weight <= 6:
        cost = weight * 3.00 + 20
    elif weight > 6 and weight <= 10:
        cost = weight * 4.00 + 20
    else:
        cost = weight * 4.75 + 20
    return cost


# 3.  A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:

# 8.4\ lb \times \$4.00 + \$20.00 = \$53.608.4 lb×$4.00 +$20.00 =$53.60
# Test that your ground shipping function gets the same value.
print(ground_shipping(8.4))

# Ground Shipping Premium:
# 4.
# We’ll also need to make sure we include the price of premium ground shipping in our code.

# Create a variable for the cost of premium ground shipping.
ground_shipping_premium = 125.00
# Note: This does not need to be an if statement because the price of premium ground shipping does not change with the weight of the package.

# 5.
# Print it out for the user just in case they forgot!
print(ground_shipping_premium)
# Drone Shipping:
# 6. Write a comment for this section of the code, “Drone Shipping”.

# Create an if/elif/else statement for the cost of drone shipping. This statement should check against weight and print the cost of shipping a package of that weight.

# 7. A package that weighs 1.5 pounds should cost $6.75 to ship by drone:

# 1.5\ lb \times \$4.50 + \$0.00 = \$6.751.5 lb×$4.50 +$0.00 =$6.75
# Test that your drone shipping function gets the same value.

# 8. Great job! Now, test everything one more time!

# What is the cheapest method of shipping a 4.8 pound package and how much would it cost?

# What is the cheapest method of shipping a 41.5 pound package and how much would it cost?

# (See hint for answers)
