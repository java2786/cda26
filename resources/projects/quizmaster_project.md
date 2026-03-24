# QuizMaster - A Python Quiz Application with Score Tracker

## Overview

**QuizMaster** is a console-based quiz application where users can register, login, attempt quizzes by category, view their scores, and compete on a leaderboard. This project will help you apply everything you learned in Core Python in a real-world scenario.

This project is divided into **3 Parts** - each part builds upon the previous one, making it easier to understand and implement step by step.

---

## What Will You Build?

A complete console application where:
- Users can register and login securely
- Users can choose a quiz category and attempt questions
- Each question is multiple choice with 4 options
- The app tracks the score for every quiz attempt
- Users can view their personal score history
- A leaderboard shows the top scorers across all users
- Users can change their password
- Questions are stored and loaded from a file (Part 3)

---

## Project Structure: 3 Parts

### Part 1: Single User with Hardcoded Questions
You will create a basic version where one user exists and quiz questions are hardcoded directly in the program.

### Part 2: Multiple Users with Collections
You will upgrade the app to support multiple users, multiple categories, and store all data using Python collections like lists, dictionaries, and sets.

### Part 3: File-Based Storage
You will make the app fully persistent by storing user data and questions in files, so everything remains even after the program closes.

---

## Part 1: Single User with Hardcoded Questions

### Objective
Build a simple console quiz application where:
- A single user can register and login
- The user can attempt a hardcoded quiz of 5 questions
- The app shows the score at the end
- User data is stored in variables (no file, no database)

### Features to Implement

#### 1. Guest Menu
When the app starts, show this menu:
```
========== Welcome to QuizMaster ==========
1. Register
2. Login
3. Exit
```

#### 2. User Registration
When user selects "Register":
- Ask for:
  - Full Name (required)
  - Email (required, will be used as login ID)
  - Password (required)
- Store these details in variables like:
  - `user_name = ""`
  - `user_email = ""`
  - `user_password = ""`
- Show a success message: "Registration successful! Please login."

**Validation Rules:**
- Full name cannot be empty
- Email must contain "@" symbol
- Password must be at least 6 characters long

#### 3. User Login
When user selects "Login":
- Ask for email and password
- Check if entered email and password match the stored values
- If match: Show "Login Successful! Welcome [Full Name]"
- If not match: Show "Invalid email or password. Try again."

#### 4. After Successful Login
Once logged in, show the user dashboard:
```
========== QuizMaster Dashboard ==========
1. Start Quiz
2. View My Score
3. Change Password
4. Logout
```

#### 5. Start Quiz
- Display 5 hardcoded multiple choice questions one by one
- Each question should have 4 options (A, B, C, D)
- Accept user's answer for each question
- After all 5 questions, show the final score
- Example format:
  ```
  Question 1: What is the capital of India?
  A. Mumbai
  B. Pune
  C. New Delhi
  D. Chennai
  Your answer: C
  Correct!
  ```
- Store the latest score in a variable like `user_score = 0`
- Show: "Quiz completed! Your score: 4 out of 5"

**Sample Hardcoded Questions (General Knowledge - India):**
```python
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Pune", "C. New Delhi", "D. Chennai"],
        "answer": "C"
    },
    {
        "question": "Which company runs the IRCTC railway booking platform?",
        "options": ["A. BSNL", "B. Indian Railways", "C. Air India", "D. ONGC"],
        "answer": "B"
    },
    {
        "question": "What does LIC stand for?",
        "options": ["A. Life Insurance Corporation", "B. Loan Insurance Company", "C. Legal Insurance Council", "D. Life Investment Corp"],
        "answer": "A"
    },
    {
        "question": "Which city is known as the IT capital of India?",
        "options": ["A. Pune", "B. Mumbai", "C. Bangalore", "D. Hyderabad"],
        "answer": "C"
    },
    {
        "question": "Flipkart was founded in which Indian city?",
        "options": ["A. Delhi", "B. Bangalore", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    }
]
```

#### 6. View My Score
- Display the user's last quiz score
- If no quiz taken yet: Show "You have not attempted any quiz yet."
- If score is available: Show "Your last score: X out of 5"

#### 7. Change Password
- Ask for current password
- If current password is correct, ask for new password
- Validate: New password must be at least 6 characters
- Update the password variable
- Show "Password changed successfully."

#### 8. Logout
- Show "Logged out successfully. See you again!"
- Return to Guest Menu

---

## Part 2: Multiple Users with Collections

### Objective
Upgrade the app to support multiple users, multiple quiz categories, and a leaderboard using Python collections (lists, dictionaries, sets).

### Features to Implement

#### 1. Store Multiple Users
Instead of single variables, use a list of dictionaries to store multiple users:
```python
users = []
```

Each user should be a dictionary like:
```python
{
    'name': 'Suresh',
    'email': 'suresh@gmail.com',
    'password': 'suresh123',
    'scores': []
}
```

Each entry in `scores` should itself be a dictionary:
```python
{
    'category': 'General Knowledge',
    'score': 4,
    'total': 5
}
```

#### 2. Store Questions by Category
Use a dictionary of lists to store questions grouped by category:
```python
question_bank = {
    "General Knowledge": [...],
    "Python Basics": [...],
    "Indian Railways": [...]
}
```

**Hint:** Each category should have at least 5 questions in the same format as Part 1.

#### 3. Enhanced Guest Menu
```
========== Welcome to QuizMaster ==========
1. Register
2. Login
3. View Leaderboard
4. Exit
```

#### 4. User Registration (Multiple Users)
- Ask for full name, email, and password
- Check if email already exists in the users list
- If email exists: Show "Email already registered. Please login."
- If not: Add new user to the users list
- Show "Registration successful! Please login."

#### 5. User Login (Multiple Users)
- Ask for email and password
- Search through the users list to find matching email and password
- If found: Login successful, store current logged-in user
- If not found: Show "Invalid credentials. Try again."

**Hint:** Keep track of the currently logged-in user using a variable like `current_user = None`

#### 6. Logged-In User Dashboard
```
========== QuizMaster Dashboard ==========
Welcome, Suresh!
1. Start Quiz
2. View My Scores
3. View Leaderboard
4. Change Password
5. Logout
```

#### 7. Start Quiz
- Show available categories to the user:
  ```
  Select a Category:
  1. General Knowledge
  2. Python Basics
  3. Indian Railways
  ```
- After category is selected, load questions for that category
- Ask questions one by one with 4 options each
- Track correct answers
- At the end, show score and save it to the current user's `scores` list
- Show: "Quiz completed! Your score: 4 out of 5"

**Randomise question order** using Python's `random` module:
```python
import random
random.shuffle(questions)
```

#### 8. View My Scores
- Display all quiz attempts by the current logged-in user
- Show category, score, and total for each attempt
- Example:
  ```
  Your Score History:
  1. General Knowledge  - 4 out of 5
  2. Python Basics      - 3 out of 5
  3. Indian Railways    - 5 out of 5
  ```
- If no quiz taken: "You have not attempted any quiz yet."

#### 9. View Leaderboard
- Available from both Guest Menu and Dashboard
- Calculate the best score percentage for each user across all attempts
- Display top 5 users sorted by their best score percentage
- Example:
  ```
  ===== QuizMaster Leaderboard =====
  Rank  Name        Best Score
  1     Ramesh      100%
  2     Suresh       80%
  3     Mahesh       60%
  ```
- If no scores exist: "No scores yet. Be the first to attempt a quiz!"

#### 10. Change Password
- Ask for old password
- Verify old password matches the stored value
- If correct, ask for new password
- Validate new password length (minimum 6 characters)
- Update password in the users list
- Show "Password changed successfully."

#### 11. Track Attempted Categories
Use a **set** to track which categories a user has already attempted:
```python
attempted_categories = set()
```
- Before showing the category menu, show which ones the user has already tried
- Example: "You have already attempted: General Knowledge"
- Users can reattempt any category - all attempts are saved in score history

---

## Part 3: File-Based Storage (Persistent Data)

### Objective
Make your app fully persistent by storing user data and questions in files so that all data remains even after closing the program.

### Features to Implement

#### 1. File Structure
Create and use these files:
- `users.txt` - Store all registered user information and their scores
- `questions.txt` - Store all quiz questions and answers by category
- `session.txt` - Store the currently logged-in user's email (if any)

#### 2. Save Users to File
After every registration, quiz attempt, or password change:
- Write all user data to `users.txt`
- Format: Each line represents one user
- Example line in file:
  ```
  Suresh,suresh@gmail.com,suresh123,General Knowledge:4:5|Python Basics:3:5
  ```
- Use `,` to separate user fields
- Use `|` to separate multiple score entries
- Use `:` to separate category, score, and total within each score entry

#### 3. Load Users from File
When the program starts:
- Read `users.txt`
- Load all users into a list of dictionaries in memory
- If file does not exist, start with an empty users list and create the file

#### 4. Save Questions to File
Store questions in `questions.txt` in this format:
```
CATEGORY:General Knowledge
Q:What is the capital of India?
A:Mumbai|Pune|New Delhi|Chennai
ANS:C

CATEGORY:Python Basics
Q:Which keyword is used to define a function in Python?
A:func|define|def|function
ANS:C
```
- Use `Q:` prefix for question text
- Use `A:` prefix for options separated by `|`
- Use `ANS:` prefix for the correct option letter
- Leave a blank line between questions
- Use `CATEGORY:` prefix to mark the start of a new category

#### 5. Load Questions from File
When the program starts:
- Read `questions.txt`
- Parse and load all questions into the `question_bank` dictionary grouped by category
- If the file does not exist, load a default set of hardcoded questions and save them to the file automatically

#### 6. Session Management
- When user logs in: Save their email to `session.txt`
- When program starts: Check if `session.txt` has an email stored
  - If yes: Auto-login that user and show dashboard
  - If no: Show guest menu
- When user logs out: Clear `session.txt`

#### 7. Enhanced Features

**Auto-Login on Restart:**
- If the user was previously logged in and closed the program without logging out
- Next time the program starts, automatically log them in
- Show: "Welcome back, [Full Name]! Ready for another quiz?"

**All Menus and Features from Part 2:**
- Keep all features from Part 2
- But now all data — users, scores, and questions — persists across program restarts

---

## Real-World Scenarios to Test

### Scenario 1: First Time User
- Ramesh opens QuizMaster for the first time
- He registers with name: Ramesh, email: ramesh@gmail.com
- He logs in and attempts the "General Knowledge" quiz
- He scores 4 out of 5
- He closes the program
- He opens QuizMaster again — his score should still be visible

### Scenario 2: Multiple Users and Leaderboard
- Suresh registers and scores 5 out of 5 in "Python Basics"
- He logs out
- Mahesh registers and scores 3 out of 5 in "Python Basics"
- Dinesh registers and scores 4 out of 5 in "General Knowledge"
- The leaderboard should show: Suresh (100%), Dinesh (80%), Mahesh (60%)

### Scenario 3: Reattempting a Quiz
- Nitesh attempts "Indian Railways" and scores 2 out of 5
- He attempts the same category again and scores 5 out of 5
- Both attempts should appear in his score history
- His best score (100%) should appear on the leaderboard

### Scenario 4: Session Recovery
- Kamlesh logs in and attempts a quiz
- The program closes suddenly (power cut or crash)
- Next time QuizMaster opens, Kamlesh is automatically logged in
- He can see his previous scores and continue from where he left off

### Scenario 5: Viewing Leaderboard as a Guest
- Gukesh has not registered yet
- He selects "View Leaderboard" from the guest menu
- He can see the top scorers without logging in
- Impressed by the scores, he decides to register and compete

---

## Important Points to Remember

### 1. Input Validation
Always validate user inputs:
- Check if name and email fields are not empty
- Check if email contains the "@" symbol
- Check if password is at least 6 characters long
- Check if the user enters a valid option from the menu (A, B, C, or D for quiz answers)
- Handle invalid menu number choices gracefully

### 2. Exception Handling
Use try-except blocks for:
- File operations (reading and writing)
- Invalid or unexpected user inputs
- Menu option selection errors
- Score calculation when no attempts exist

**Example:**
```python
try:
    # File operation or user input
except FileNotFoundError:
    # Handle file not found
except ValueError:
    # Handle invalid input like entering letters instead of numbers
except Exception as e:
    # Handle any other unexpected error
    print("Something went wrong:", e)
```

### 3. User Experience
- Always show clear messages after every action
- Display the menu again after each operation so the user knows what to do next
- Confirm actions (like "Quiz completed! Your score: 4 out of 5")
- If the user enters a wrong answer, show the correct answer before moving to the next question
- Handle errors gracefully with helpful messages instead of crashing

### 4. Code Organisation
- Use separate functions for each feature
- Keep your code clean, readable, and well-commented
- Group related functions together (all quiz functions together, all user functions together)
- Follow consistent naming conventions throughout the project

---

## Suggested Functions to Create

Here are the functions you will need (you can always add more based on your ideas):

### Part 1 Functions:
- `show_guest_menu()`
- `register_user()`
- `login_user()`
- `show_dashboard()`
- `start_quiz()`
- `view_my_score()`
- `change_password()`
- `logout()`

### Part 2 Functions (add these):
- `is_email_registered(email)`
- `find_user_by_email(email)`
- `select_category()`
- `load_questions(category)`
- `calculate_leaderboard()`
- `view_leaderboard()`
- `view_my_scores()`
- `save_score(category, score, total)`

### Part 3 Functions (add these):
- `save_users_to_file()`
- `load_users_from_file()`
- `save_questions_to_file()`
- `load_questions_from_file()`
- `save_session(email)`
- `load_session()`
- `clear_session()`

---

## Tips for Implementation

### Tip 1: Start Simple
- First, make Part 1 work completely with all 5 hardcoded questions
- Test every feature — registration, login, quiz, score view, password change, and logout
- Only then move to Part 2

### Tip 2: Test Frequently
After implementing each feature:
- Run the program and test that specific feature
- Fix bugs before moving to the next feature
- Do not wait until the end to test everything

### Tip 3: Handle Edge Cases
Think about unusual situations:
- What if the user enters "a" instead of "A" as their answer?
- What if the file is empty or corrupted?
- What if the user enters a category number that does not exist?
- What if no one has taken a quiz yet and someone views the leaderboard?

### Tip 4: Use Meaningful Variable Names
Instead of:
```python
u = []
q = []
s = 0
```

Use:
```python
users = []
questions = []
current_score = 0
```

### Tip 5: Use the `random` Module Wisely
Shuffle questions so the quiz feels different every time:
```python
import random
shuffled = questions.copy()
random.shuffle(shuffled)
```
Always shuffle a **copy** of the original list so the original question bank is not changed.

### Tip 6: Break Down Complex Features
If a feature seems difficult:
- Break it into smaller steps
- For example, the leaderboard: first collect all users with scores, then sort them, then display the top 5
- Implement one step at a time and test before moving forward

---

## Indian Context Examples

Use these realistic examples while testing and building your question bank:

### User Names:
- Suresh Kumar from Chennai
- Ramesh Patil from Pune
- Mahesh Sharma from Delhi
- Dinesh Reddy from Hyderabad
- Mukesh Gupta from Mumbai
- Kamlesh Joshi from Ahmedabad
- Nitesh Verma from Nagpur
- Gukesh Iyer from Chennai

### Email Examples:
- suresh.kumar@gmail.com
- ramesh.patil@yahoo.in
- mahesh.sharma@outlook.com
- nitesh.verma@rediffmail.com

### Sample Questions for Each Category

**General Knowledge (India):**
- What is the national animal of India? (Answer: Tiger)
- In which year did India gain independence? (Answer: 1947)
- Which river is the longest in India? (Answer: Ganga)
- What is the currency of India? (Answer: Rupee)
- Which city is home to the Taj Mahal? (Answer: Agra)

**Python Basics:**
- Which keyword is used to define a function in Python? (Answer: def)
- What data type is used to store True or False in Python? (Answer: bool)
- Which symbol is used to add a comment in Python? (Answer: #)
- What does len() function do in Python? (Answer: Returns the length of a sequence)
- Which collection type does NOT allow duplicates? (Answer: set)

**Indian Railways:**
- What does PNR stand for in railway ticketing? (Answer: Passenger Name Record)
- Which is the longest railway platform in India? (Answer: Gorakhpur)
- What does IRCTC stand for? (Answer: Indian Railway Catering and Tourism Corporation)
- Which train was India's first bullet train corridor planned between? (Answer: Mumbai and Ahmedabad)
- What colour is the Rajdhani Express train? (Answer: Red and Grey)

---

## Common Mistakes to Avoid

1. **Not shuffling a copy of the list** - Shuffling the original list permanently changes your question bank. Always shuffle a copy using `questions.copy()`
2. **Comparing answers with wrong case** - Convert both user input and correct answer to uppercase before comparing: `user_answer.upper() == correct_answer.upper()`
3. **Not saving scores after every quiz** - In Part 3, save data to file immediately after every quiz attempt, not just at the end of the session
4. **Not handling file errors** - Always use try-except for all file read and write operations
5. **Calculating leaderboard incorrectly** - Use best score percentage, not total score, so users are fairly compared across different total marks
6. **Not clearing session on logout** - In Part 3, always clear `session.txt` when the user logs out
7. **Overcomplicating the question format** - Keep question storage simple and consistent so loading and saving works without errors
8. **Not testing with multiple users** - Always test the leaderboard and score history with at least 3 different users before calling it complete

---

## Success Criteria

Your QuizMaster project is complete when:

- Users can register with a unique email and login securely
- Logged-in users can select a quiz category and attempt questions
- Each question displays 4 options and accepts A, B, C, or D as input
- The correct answer is shown if the user answers wrong
- The final score is displayed at the end of each quiz
- All quiz attempts are saved in the user's score history
- The leaderboard correctly shows top 5 users by best score percentage
- Users can change their password successfully
- Auto-login works when the program restarts (Part 3)
- Questions are loaded from a file (Part 3)
- All user data and scores persist across program restarts (Part 3)
- The program handles all invalid inputs and file errors gracefully
- Code is clean, organised, and well-commented

---

## Quiz - Test Your Understanding

Answer these questions before you start coding. This will help you think through the design:

**Q1.** In Part 1, where are the quiz questions stored?
- A. In a file
- B. In a database
- C. Directly in the program as a list of dictionaries
- D. In a separate Python file

**Q2.** Which Python module will you use to shuffle the question order?
- A. `os`
- B. `random`
- C. `math`
- D. `sys`

**Q3.** In Part 2, what data structure is used to store all users?
- A. A tuple of strings
- B. A set of names
- C. A list of dictionaries
- D. A single dictionary

**Q4.** What is the correct way to compare the user's quiz answer without case issues?
- A. `user_answer == correct_answer`
- B. `user_answer.lower() == correct_answer`
- C. `user_answer.upper() == correct_answer.upper()`
- D. `user_answer != correct_answer`

**Q5.** In Part 3, what is the purpose of `session.txt`?
- A. To store all quiz questions
- B. To remember which user is currently logged in so they are auto-logged in on restart
- C. To store the leaderboard rankings
- D. To keep a backup of all passwords

**Q6.** Which separator is suggested for storing multiple score entries in `users.txt`?
- A. Comma (`,`)
- B. Semicolon (`;`)
- C. Pipe (`|`)
- D. Hyphen (`-`)

**Q7.** In the leaderboard, how is the best score for each user calculated?
- A. Sum of all scores
- B. Average of all scores
- C. The score from the first quiz attempt
- D. The highest score percentage across all attempts

**Q8.** What Python collection type is used to track which categories a user has already attempted?
- A. List
- B. Tuple
- C. Set
- D. Dictionary

**Answers:** Q1-C, Q2-B, Q3-C, Q4-C, Q5-B, Q6-C, Q7-D, Q8-C

---

## Mini Assignments

Complete these tasks to practice each concept before building the full project:

### Assignment 1: Question Display (Part 1 Warm-up)
Write a Python program that:
- Stores 3 questions as a list of dictionaries (use any topic you like)
- Loops through each question and displays it with its 4 options
- Accepts the user's answer and checks if it is correct
- Prints the final score at the end

Do not worry about login or file handling yet. Just get the quiz logic working.

### Assignment 2: Score Percentage Calculator (Part 2 Warm-up)
Write a function called `calculate_percentage(score, total)` that:
- Takes the score and total as input
- Returns the percentage rounded to 2 decimal places
- Test it with values like (4, 5), (3, 5), (5, 5), and (0, 5)

Expected output:
```
4 out of 5 = 80.0%
3 out of 5 = 60.0%
5 out of 5 = 100.0%
0 out of 5 = 0.0%
```

### Assignment 3: Leaderboard Sort (Part 2 Warm-up)
Given the following list of users with their best scores, write a program that:
- Sorts them in descending order of best score percentage
- Displays the top 3 users in a ranked format

```python
users = [
    {'name': 'Suresh', 'best_score': 60},
    {'name': 'Ramesh', 'best_score': 100},
    {'name': 'Mahesh', 'best_score': 80},
    {'name': 'Dinesh', 'best_score': 40},
    {'name': 'Mukesh', 'best_score': 90}
]
```

Expected output:
```
Rank 1: Ramesh  - 100%
Rank 2: Mukesh  -  90%
Rank 3: Mahesh  -  80%
```

### Assignment 4: File Read and Write (Part 3 Warm-up)
Write a Python program that:
- Creates a file called `scores.txt`
- Writes 3 user score records in the format: `Name,Category,Score,Total`
- Reads the file back and prints each record in a readable format

Example file content:
```
Suresh,Python Basics,4,5
Ramesh,General Knowledge,3,5
Mahesh,Indian Railways,5,5
```

Expected output when reading:
```
Suresh scored 4 out of 5 in Python Basics
Ramesh scored 3 out of 5 in General Knowledge
Mahesh scored 5 out of 5 in Indian Railways
```

### Assignment 5: Full Part 1 Challenge
Build the complete Part 1 of QuizMaster:
- Registration and login for one user
- 5 hardcoded questions with 4 options each (use the Indian Railways or Python Basics category)
- Score display at the end
- View last score from the dashboard
- Change password feature
- Logout that returns to the guest menu

Test it completely before moving to Part 2.

---

## Final Words

This project brings together everything you learned in Core Python:
- Variables and data types
- Conditional statements
- Loops
- Lists, dictionaries, and sets
- Functions
- The `random` module
- File handling
- Exception handling

Take your time, implement one feature at a time, and test thoroughly. Every bug you fix teaches you something new, so do not get discouraged when things go wrong — that is exactly how real developers learn.

Remember: The goal is not just to complete the project, but to understand how each Python concept works together inside a real application that you can proudly show in any interview.

**Happy Coding! All the best for your QuizMaster project!**

---
