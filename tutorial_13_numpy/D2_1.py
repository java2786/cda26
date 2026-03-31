import numpy as np
marks = [78,81,92,83]
np_marks = np.array(marks)

print(np_marks)


print(f"Max: {np.max(np_marks)}")
print(f"Min: {np.min(np_marks)}")
print(f"Median: {np.median(np_marks)}")
print(f"Total: {np.sum(np_marks)}")
print(f"Average: {np.mean(np_marks)}")


# Read
print(f"First mark: {np_marks[0]}")
