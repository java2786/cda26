marks = [56, 76, 43]
marks[2] = 71

print(marks)


items = (100, 200, 300)
print(items)
print(items[1])

# items[1] = 5





# LIC policy numbers
policy_numbers = (12345, 67890, 12345, 54321, 12345)

# Count occurrences
count_12345 = policy_numbers.count(12345)  # Returns 3

# Find index of first occurrence
index_67890 = policy_numbers.index(67890)  # Returns 1

# Length of tuple
total_policies = len(policy_numbers)  # Returns 5



# Flipkart order details
order = ("Laptop", 45000, "Electronics", "Delivered")

# Unpacking
product, price, category, status = order

print(f"Product: {product}")
print(f"Price: Rs. {price}")
print(f"Category: {category}")
print(f"Status: {status}")