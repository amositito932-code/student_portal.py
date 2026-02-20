# Student Portal System (Python)

## Description

This project is a simple Python program that simulates a student portal login and academic result analyzer.
The system first verifies a student’s identity using a generated password and then processes the student's marks to calculate average, grade, and final academic remark.

The program was developed as practice to understand basic programming concepts such as loops, conditions, casting, and string manipulation.



## How the System Works

### 1. Login System

The student enters:

* Full name
* Birth year

The system automatically generates a password using:

* First 3 letters of the name (in uppercase)
* Last 2 digits of the birth year

Example:
Name: Tito Felix
Birth Year: 2001
Generated Password: **TIT01**

The student is given only **3 attempts** to enter the correct password.
If the student fails 3 times, the account is locked.

---

### 2. Marks Processing

After successful login, the student enters marks for:

* Mathematics
* Economics
* Geography

The program converts the marks into integers and calculates:

* Total marks
* Average

---

### 3. Grading System

| Average      | Grade |
| ------------ | ----- |
| 75 and above | A     |
| 65 – 74      | B     |
| 45 – 64      | C     |
| 30 – 44      | D     |
| Below 30     | F     |

---

### 4. Final Remark

* Average ≥ 50 → PASS
* Average < 50 → SUPPLEMENTARY EXAM

---

## Programming Concepts Used

* Input and Output
* Type Casting
* If / Else Conditions
* While Loop
* String Substring
* Logical Operators

---

## Purpose of the Project

The goal of this project is to practice beginner programming skills and understand how real systems like school portals and ATM logins work.

---

## Author

Tito Amos Felix
Aspiring Data Scientist | Python Learner | Amotech
