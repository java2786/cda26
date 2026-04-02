import pandas as pd
import numpy as np
bookings = pd.DataFrame({
	"Train_No": [12345, 12345, 43021, 43021, 12123, 12406],
	"Class": ["Sleeper", "1AC", "2AC", "2AC", "GEN", "Sleeper"],
	"Passengers": [64, 33, 82, 71, 44, 99],
	"Fare": [500, 1300, 1100, 1050, 350, 550],
	"From": ["Jaipur", "Jaipur", "Delhi", "Delhi", "Indore", "Patna"],
	"To": ["Delhi", "Delhi", "Pune", "Pune", "Patna", "Indore"]
})

# 1. Total Revenue
print(np.array(bookings["Fare"]*bookings["Passengers"]).sum())
# 2. Total Revenue of 12345 (Revenue by Train)
print(bookings.groupby("Train_No")["Fare"].sum())
# 3. Analysis by Class
analysis = bookings.groupby("Class").agg({
    "Fare": ["sum", "mean"],
    "Passengers": ["sum"]
})
print(analysis)
# 4. Busiest Route