# ChirpBox - A Python Tweet Application Project

## Overview

**ChirpBox** is a console-based tweet application where users can register, login, post tweets, and view tweets from other users. This project will help you apply everything you learned in Core Python in a real-world scenario.

This project is divided into **3 Parts** - each part builds upon the previous one, making it easier to understand and implement step by step.

---

## What Will You Build?

A complete console application where:
- Users can register with their details
- Users can login securely
- Logged-in users can post tweets
- Users can view their own tweets
- Users can see all registered users and their tweets
- Users can change their password
- Users can reset forgotten passwords

---

## Project Structure: 3 Parts

### Part 1: Single User with Hardcoded Data
You will create a basic version where only one user exists in the system. User data is stored directly in variables (hardcoded).

### Part 2: Multiple Users with Collections
You will upgrade the app to handle multiple users using Python collections like lists, dictionaries, and sets.

### Part 3: File-Based Storage
You will make the app persistent by storing user data in files, so data remains even after the program closes.

---

## Part 1: Single User Registration and Login

### Objective
Build a simple console application where:
- A single user can register
- The same user can login
- User data is stored in variables (no file, no database)

### Features to Implement

#### 1. Guest User Menu
When the app starts, show this menu:
```
========== Welcome to ChirpBox ==========
1. Register
2. Login
3. Exit
```

#### 2. User Registration
When user selects "Register":
- Ask for:
  - First Name (required)
  - Email (required, will be used as login ID)
  - Password (required)
- Store these details in variables like:
  - `user_first_name = ""`
  - `user_email = ""`
  - `user_password = ""`
- Show a success message: "Registration successful! Please login."

**Validation Rules:**
- First name cannot be empty
- Email must contain "@" symbol
- Password must be at least 6 characters long

#### 3. User Login
When user selects "Login":
- Ask for email and password
- Check if entered email and password match the stored values
- If match: Show "Login Successful! Welcome [First Name]"
- If not match: Show "Invalid email or password"

#### 4. After Successful Login
Once logged in, show a new menu:
```
========== ChirpBox Dashboard ==========
1. Post a Tweet
2. View My Tweets
3. Change Password
4. Logout
```

#### 5. Post a Tweet
- Ask user to enter a tweet (text message)
- Store the tweet in a list (example: `my_tweets = []`)
- Show confirmation: "Tweet posted successfully!"

#### 6. View My Tweets
- Display all tweets posted by the user
- If no tweets: Show "You haven't posted any tweets yet"

#### 7. Change Password
- Ask for current password
- If current password is correct, ask for new password
- Update the password
- Show "Password changed successfully"

#### 8. Logout
- Show "Logged out successfully"
- Return to Guest User Menu

---

## Part 2: Multiple Users with Collections

### Objective
Upgrade the app to support multiple users using Python collections (lists, dictionaries, sets).

### Features to Implement

#### 1. Store Multiple Users
Instead of single variables, use a list of dictionaries to store multiple users:
```python
users = []
```

Each user should be a dictionary like:
```python
{
    'first_name': 'Suresh',
    'email': 'suresh@gmail.com',
    'password': 'suresh123',
    'tweets': []
}
```

#### 2. Enhanced Guest User Menu
```
========== Welcome to ChirpBox ==========
1. Register
2. Login
3. Forgot Password
4. Exit
```

#### 3. User Registration (Multiple Users)
- Ask for first name, email, and password
- Check if email already exists in the users list
- If email exists: Show "Email already registered. Please login."
- If not: Add new user to the users list
- Show "Registration successful! Please login."

#### 4. User Login (Multiple Users)
- Ask for email and password
- Search through the users list to find matching email and password
- If found: Login successful, store current logged-in user
- If not found: Show "Invalid credentials"

**Hint:** Keep track of the currently logged-in user using a variable like `current_user = None`

#### 5. Logged-In User Menu
```
========== ChirpBox Dashboard ==========
1. Post a Tweet
2. View My Tweets
3. View All Tweets
4. View All Users
5. Change Password
6. Logout
```

#### 6. Post a Tweet
- Ask user to enter tweet text
- Add the tweet to current user's tweets list
- Show "Tweet posted successfully!"

#### 7. View My Tweets
- Display all tweets of the current logged-in user
- Show tweet number and text
- If no tweets: "You haven't posted any tweets yet"

#### 8. View All Tweets
- Display tweets from all registered users
- Format: Show username and their tweets
- Example:
  ```
  Suresh's Tweets:
  - Learning Python is fun!
  - Just posted my first tweet!
  
  Ramesh's Tweets:
  - Hello ChirpBox community!
  ```

#### 9. View All Users
- Display list of all registered users
- Show first name and email
- Example:
  ```
  Registered Users:
  1. Suresh (suresh@gmail.com)
  2. Ramesh (ramesh@gmail.com)
  3. Mahesh (mahesh@gmail.com)
  ```

#### 10. Change Password
- Ask for old password
- Verify old password
- If correct, ask for new password
- Update password in the users list
- Show "Password changed successfully"

#### 11. Forgot Password
Available in Guest Menu:
- Ask for registered email
- If email exists, ask for first name for verification
- If first name matches, allow user to set new password
- Show "Password reset successful! Please login."

---

## Part 3: File-Based Storage (Persistent Data)

### Objective
Make your app persistent by storing user data in text files so that data remains even after closing the program.

### Features to Implement

#### 1. File Structure
Create and use these files:
- `users.txt` - Store all user information
- `current_session.txt` - Store currently logged-in user's email (if any)

#### 2. Save Users to File
After every registration or password change:
- Write all user data to `users.txt`
- Format: Each line represents one user
- Example line in file:
  ```
  Suresh,suresh@gmail.com,suresh123,Learning Python is fun!|Just posted my first tweet!
  ```
- Use `,` to separate user fields
- Use `|` to separate multiple tweets

#### 3. Load Users from File
When the program starts:
- Read `users.txt`
- Load all users into a list of dictionaries
- If file doesn't exist, create an empty file

#### 4. Session Management
- When user logs in: Save their email to `current_session.txt`
- When program starts: Check if `current_session.txt` has an email
  - If yes: Auto-login that user
  - If no: Show guest menu
- When user logs out: Clear `current_session.txt`

#### 5. Enhanced Features

**Auto-Login on Restart:**
- If user was logged in and program crashed or closed
- Next time program starts, automatically log them in
- Show: "Welcome back, [First Name]!"

**All Menus and Features from Part 2:**
- Keep all features from Part 2
- But now data persists across program restarts

---

## Real-World Scenarios to Test

### Scenario 1: First Time User
- Ramesh opens ChirpBox for the first time
- He registers with email: ramesh@gmail.com
- He logs in and posts: "Hello from Pune!"
- He closes the program
- He opens ChirpBox again - his data should still be there

### Scenario 2: Multiple Users
- Suresh registers and posts tweets
- He logs out
- Mahesh registers and posts tweets
- Both users' tweets should be saved
- Either can login anytime and see their tweets

### Scenario 3: Forgot Password
- Dinesh forgets his password
- He uses "Forgot Password" option
- Verifies his email and first name
- Sets a new password
- Logs in successfully with new password

### Scenario 4: Session Recovery
- Mukesh logs in and posts tweets
- Program crashes suddenly
- Next time he opens ChirpBox, he should auto-login
- He can continue from where he left

---

## Important Points to Remember

### 1. Input Validation
Always validate user inputs:
- Check if inputs are not empty
- Check if email format is correct
- Check if password is strong enough
- Handle invalid menu choices

### 2. Exception Handling
Use try-except blocks for:
- File operations (reading/writing)
- Invalid user inputs
- Menu option selection
- Password verification

**Example:**
```python
try:
    # File operation or user input
except FileNotFoundError:
    # Handle file not found
except ValueError:
    # Handle invalid input
except Exception as e:
    # Handle any other error
```

### 3. User Experience
- Always show clear messages
- Display menus after each operation
- Confirm actions (like "Tweet posted successfully!")
- Handle errors gracefully with helpful messages

### 4. Code Organization
- Use functions for each feature
- Keep your code clean and readable
- Add comments where necessary
- Follow naming conventions

---

## Suggested Functions to Create

Here are some functions you might need (you can add more):

### Part 1 Functions:
- `show_guest_menu()`
- `register_user()`
- `login_user()`
- `show_user_menu()`
- `post_tweet()`
- `view_my_tweets()`
- `change_password()`
- `logout()`

### Part 2 Functions (add these):
- `is_email_registered(email)`
- `find_user_by_email(email)`
- `view_all_tweets()`
- `view_all_users()`
- `forgot_password()`

### Part 3 Functions (add these):
- `save_users_to_file()`
- `load_users_from_file()`
- `save_current_session(email)`
- `load_current_session()`
- `clear_session()`

---

## Tips for Implementation

### Tip 1: Start Simple
- First, make Part 1 work completely
- Test every feature thoroughly
- Then move to Part 2

### Tip 2: Test Frequently
After implementing each feature:
- Run the program
- Test that specific feature
- Fix bugs before moving forward

### Tip 3: Handle Edge Cases
Think about unusual situations:
- What if user enters empty text?
- What if file doesn't exist?
- What if user enters wrong menu option?
- What if two users try to register with same email?

### Tip 4: Use Meaningful Variable Names
Instead of:
```python
u = []
t = []
```

Use:
```python
users = []
tweets = []
```

### Tip 5: Break Down Complex Features
If a feature seems difficult:
- Break it into smaller steps
- Implement one step at a time
- Test each step before moving forward

---

## Indian Context Examples

Use these realistic examples while testing:

### User Names:
- Suresh Kumar from Chennai
- Ramesh Patil from Pune
- Mahesh Sharma from Delhi
- Dinesh Reddy from Hyderabad
- Mukesh Gupta from Mumbai

### Email Examples:
- suresh.kumar@gmail.com
- ramesh.patil@yahoo.in
- mahesh.sharma@outlook.com

### Tweet Examples:
- "Just booked my train ticket on Indian Railways app!"
- "Ordered lunch from Swiggy, loving the biryani!"
- "Celebrating Diwali with family in Pune!"
- "Finally completed my LIC premium payment online!"
- "Flipkart sale is amazing this year!"
- "Learning Python at my college in Chennai!"

---

## Common Mistakes to Avoid

1. **Not validating inputs** - Always check if user entered valid data
2. **Forgetting to save to file** - In Part 3, save data after every change
3. **Not handling file errors** - Always use try-except for file operations
4. **Overcomplicating logic** - Keep your code simple and readable
5. **Not testing edge cases** - Test with empty inputs, wrong passwords, etc.
6. **Hardcoding values** - Use variables and functions instead
7. **Ignoring user feedback** - Always show confirmation messages
8. **Not clearing session on logout** - In Part 3, clear session file when user logs out

---

## Success Criteria

Your ChirpBox project is complete when:

✓ Users can register with unique emails
✓ Registered users can login successfully
✓ Users can post multiple tweets
✓ Users can view their own tweets
✓ Users can view tweets from all users
✓ Users can see list of all registered users
✓ Users can change their password
✓ Users can reset forgotten password
✓ All data persists in files (Part 3)
✓ Session is maintained (Part 3)
✓ Program handles all errors gracefully
✓ Code is clean, organized, and well-commented

---

## Final Words

This project brings together everything you learned in Core Python:
- Variables and data types
- Conditional statements
- Loops
- Lists, dictionaries, sets
- Functions
- File handling
- Exception handling

Take your time, implement one feature at a time, and test thoroughly. Don't worry if you face challenges - that's how learning happens!

Remember: The goal is not just to complete the project, but to understand how each Python concept works in a real application.

**Happy Coding! All the best for your ChirpBox project!**

---

