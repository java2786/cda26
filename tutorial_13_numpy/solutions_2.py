import numpy as np

# -------------------------------------------------------
# STEP 1: Generate random marks
# 20 students, 5 subjects, marks between 40 and 100
# -------------------------------------------------------
np.random.seed(200)
marks = np.random.randint(40, 101, (20, 5))

subjects = ['Physics', 'Chemistry', 'Mathematics', 'Computer Science', 'English']

# Using Indian names for our students (more relatable!)
student_names = [
    'Suresh', 'Ramesh', 'Mahesh', 'Dinesh', 'Mukesh',
    'Kamlesh', 'Nitesh', 'Hitesh', 'Ratnesh', 'Himesh',
    'Gukesh', 'Jitesh', 'Priya', 'Sneha', 'Kavita',
    'Anjali', 'Pooja', 'Ravi', 'Amit', 'Vikram'
]

# Maximum marks per subject (used to calculate percentage)
MAX_MARKS_PER_SUBJECT = 100
TOTAL_SUBJECTS = 5
MAX_TOTAL = MAX_MARKS_PER_SUBJECT * TOTAL_SUBJECTS  # 500

print("=" * 65)
print("         SEMESTER MARKS ANALYSIS - CLASS REPORT")
print("=" * 65)

# -------------------------------------------------------
# STEP 2: Calculate total marks and percentage for each student
# axis=1 means we sum across all 5 subjects (row-wise)
# -------------------------------------------------------
student_totals = np.sum(marks, axis=1)           # Total marks out of 500
student_percentage = (student_totals / MAX_TOTAL) * 100  # Percentage

print("\n--- Student-wise Total and Percentage ---")
print(f"  {'Name':<12} {'Total':>8} {'Percentage':>12} {'Grade':>8}")
print("  " + "-" * 45)

for i in range(20):
    pct = student_percentage[i]
    # Simple grading logic
    if pct >= 90:
        grade = 'A+'
    elif pct >= 75:
        grade = 'A'
    elif pct >= 60:
        grade = 'B'
    elif pct >= 50:
        grade = 'C'
    else:
        grade = 'D'

    print(f"  {student_names[i]:<12} {student_totals[i]:>8} "
          f"{pct:>11.2f}% {grade:>8}")

# -------------------------------------------------------
# STEP 3: Find subject-wise class average
# axis=0 means we calculate average down each column (subject)
# Each column = one subject, so we get average per subject
# -------------------------------------------------------
subject_avg = np.mean(marks, axis=0)

print("\n--- Subject-wise Class Average ---")
for i, subject in enumerate(subjects):
    print(f"  {subject:<20}: {subject_avg[i]:.2f} / 100")

# -------------------------------------------------------
# STEP 4: Find students who scored above 90 in ANY subject
# marks > 90 gives a (20 x 5) boolean matrix
# np.any(..., axis=1) checks if ANY subject has True for each student
# -------------------------------------------------------
above_90 = np.any(marks > 90, axis=1)   # True/False for each student

print("\n--- Students Who Scored Above 90 in at Least One Subject ---")
found = False
for i in range(20):
    if above_90[i]:
        # Find which subjects they scored above 90 in
        high_subjects = [subjects[j] for j in range(5) if marks[i][j] > 90]
        print(f"  {student_names[i]}: {', '.join(high_subjects)}")
        found = True
if not found:
    print("  No student scored above 90 in any subject.")

# -------------------------------------------------------
# STEP 5: Count how many students passed (>=40) in each subject
# marks >= 40 gives a True/False matrix
# np.sum(..., axis=0) counts True values per column (per subject)
# True = 1, False = 0, so summing gives the count of passed students
# -------------------------------------------------------
passed_matrix = marks >= 40                     # Boolean matrix
pass_count = np.sum(passed_matrix, axis=0)      # Count per subject

print("\n--- Pass Count per Subject (out of 20 students) ---")
for i, subject in enumerate(subjects):
    fail_count = 20 - pass_count[i]
    print(f"  {subject:<20}: {pass_count[i]} Passed, {fail_count} Failed")

# -------------------------------------------------------
# STEP 6: Find the class topper (highest total marks)
# np.argmax returns the index of the maximum value
# -------------------------------------------------------
topper_index = np.argmax(student_totals)

print("\n--- Class Topper ---")
print(f"  Name       : {student_names[topper_index]}")
print(f"  Total Marks: {student_totals[topper_index]} / {MAX_TOTAL}")
print(f"  Percentage : {student_percentage[topper_index]:.2f}%")
print(f"  Subject Scores:")
for j, subject in enumerate(subjects):
    print(f"    {subject:<20}: {marks[topper_index][j]}")

print("\n" + "=" * 65)
print("               END OF CLASS REPORT")
print("=" * 65)