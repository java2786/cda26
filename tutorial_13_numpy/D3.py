# Ticket Analysis System

# Data: [Booking_Id, Distance_KM, Base_Price, Class_Multiplier]

import numpy as np
import time

count = 5

booking_ids = np.arange(1001,1001+count) # [1001, 1002, 1003, 1004, 1005]
distances = np.random.randint(50,500,count) # [243, 87, 171, 499, 101]

# for i in range(20):
#     # distances = np.random.randint(5)
#     distances = np.random.randint(5,50,count)
#     print(distances)
#     time.sleep(1)

base_price = 2.5
# Gen, SL, 3AC, 2AC, 1AC 
class_multiplier = np.random.choice([1, 1.5, 3, 4, 6], count) # [1.5, 3, 3, 6, 1.5]

print(class_multiplier)

ticket_price = distances * base_price * class_multiplier
final_price = ticket_price * 1.08 # with 8% gst
# print(ticket_price)

# Data: [Booking_Id, Distance_KM, Base_Price, Class_Multiplier]

booking_data = np.column_stack((booking_ids,distances, ticket_price, final_price))

print(booking_data)

print("===========Booking Analysis Report===========")
print(f"Total Bookings: {len(booking_ids)}")
print(f"Average Distance: {np.mean(distances)}")
print(f"Average Ticket Price: Rs.{np.mean(final_price):.2f}/-")
print(f"Max Fare: Rs.{np.max(final_price):.2f}/-")
print(f"Min Fare: Rs.{np.min(final_price):.2f}/-")
print(f"Total Fare: Rs.{np.sum(final_price):.2f}/-")

long_distance = distances > 200

print(distances)
print(long_distance)
print(final_price)

print(f"Sum Ticket Price: Rs.{np.sum(final_price[long_distance]):.2f}/-")