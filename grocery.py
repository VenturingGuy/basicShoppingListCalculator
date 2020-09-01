# This section initializes the prices of certain groceries such as water, chips, and milk.
# Additionally, the total price is initialized to 0, but its value will change shortly.
water_price = 2
chips_price = 2
milk_price = 5
price_total = 0

# This section asks the user for input while telling them the price of each item.
water_count = int(input("Water is $2. How many gallons would you like? "))

chips_count = int(input("Chips are also $2. How many bags would you like? "))

milk_count = int(input("A gallon of milk is $5. How many would you like? "))

# The total cost of each item is calculated based on unit price and item quantity.
water_total = water_price * water_count
chips_total = chips_price * chips_count
milk_total = milk_price * milk_count

# The total cost is calculated based on the combined previous totals.
price_total = water_total + chips_total + milk_total

# The user is informed of the total cost.
print("Your total comes out to $" + str(price_total) + ".") 