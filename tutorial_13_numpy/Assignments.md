
  
## Practice Section  
  
### Mini Assignment 1: Sales Target Achievement Analysis  
  
**Scenario:** You are analyzing sales data for a retail chain with 6 stores across India. Create a NumPy program to:  
  
1. Store monthly sales data for each store (6 stores × 12 months)  
2. Calculate which stores met their target of ₹5,00,000 average monthly sales  
3. Find the best and worst performing months across all stores  
4. Calculate quarter-wise performance for each store  
5. Identify stores that need improvement  
  
**Starter Code:**  
```python  
import numpy as np  
  
# Create your sales data here (6 stores, 12 months)  
# Use random values between 400000 and 600000  
np.random.seed(100)  
sales_data = np.random.randint(400000, 600000, (6, 12))  
  
# Your code here  
```  
  
**Expected Output Structure:**  
- Store-wise average sales  
- List of stores meeting target  
- Best and worst months  
- Quarterly performance matrix  
- Improvement recommendations  
  
---  
  
### Mini Assignment 2: Student Marks Analytics  
  
**Scenario:** Analyze semester marks for 20 students across 5 subjects (Physics, Chemistry, Mathematics, Computer Science, English).  
  
**Tasks:**  
1. Generate marks data (20 students × 5 subjects, marks between 40-100)  
2. Calculate each student's total and percentage  
3. Find subject-wise class average  
4. Identify students who scored above 90 in any subject  
5. Calculate how many students passed (≥40) in each subject  
6. Find the topper overall  
  
**Starter Code:**  
```python  
import numpy as np  
  
# Generate random marks  
np.random.seed(200)  
marks = np.random.randint(40, 101, (20, 5))  
  
subjects = ['Physics', 'Chemistry', 'Mathematics', 'Computer Science', 'English']  
student_names = ['Student_' + str(i+1) for i in range(20)]  
  
# Your code here  
```  
  
---  
  
### Mini Assignment 3: Inventory Management  
  
**Scenario:** Manage inventory for a medical store in Pune with 10 products tracked over 30 days.  
  
**Tasks:**  
1. Create opening stock array (10 products, random values 50-200)  
2. Create daily sales array (10 products × 30 days, random 5-20 per day)  
3. Calculate closing stock for each product  
4. Identify products that need reordering (stock < 30)  
5. Calculate total revenue if each product costs ₹150  
6. Find the fastest-moving product  
  
**Starter Code:**  
```python  
import numpy as np  
  
# Opening stock  
np.random.seed(300)  
opening_stock = np.random.randint(50, 201, 10)  
  
# Daily sales (10 products, 30 days)  
daily_sales = np.random.randint(5, 21, (10, 30))  
  
product_names = ['Product_' + str(i+1) for i in range(10)]  
  
# Your code here  
```  
  
