# 🎮 Project 01 — Snake, Water, Gun Game

A simple command-line Snake, Water, Gun game built in Python.

This is **Project 1** from the *Ultimate Python Programming Handbook*, which asks the learner to write a Python program capable of playing Snake, Water, Gun with the user. fileciteturn14file0

## 📌 Project Overview

The game allows the user to choose one of three options:

- `s` → Snake
- `w` → Water
- `g` → Gun

The computer randomly selects one of the three options.

The program then compares the user's choice with the computer's choice and displays whether:

- The game is a **tie**
- **You win**
- **Computer wins**

## 🎯 Game Rules

The project uses the following relationships:

- Snake beats Water
- Water beats Gun
- Gun beats Snake
- Same choice → Tie

## 🧠 How the Program Works

### 1. Random Computer Choice

The program imports the `random` module and randomly selects:

```python
computer = random.choice([-1, 0, 1])
```

The numeric values represent:

```text
1  → Snake
-1 → Water
0  → Gun
```

### 2. User Input

The user enters:

```text
s → Snake
w → Water
g → Gun
```

The program converts the user's choice into the same numeric representation used for the computer.

### 3. Dictionaries

The project uses two dictionaries:

```python
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
```

`youDict` converts the user's letter choice into a number.

`reverseDict` converts the number back into the readable game choice.

### 4. Result Checking

The program first checks:

```python
if computer == you:
    print("It's a tie!")
```

If the choices are different, the program checks the possible winning combinations using `if` / `elif`.

## ▶️ How to Run

Open the project directory in VS Code or a terminal and run:

```powershell
python main.py
```

Then enter one of:

```text
s
w
g
```

## 💡 Example

```text
Enter your choice : s
You chose Snake
Computer chose Water
You win!
```

Another possible result:

```text
Enter your choice : g
You chose Gun
Computer chose Gun
It's a tie!
```

## 📂 Project Structure

```text
Project01/
└── main.py
```

## 🛠️ Concepts Practiced

- `import`
- `random.choice()`
- User input with `input()`
- Dictionaries
- Key-value mapping
- `if / elif / else`
- Comparison operators
- Conditional game logic
- String formatting with f-strings

## 📚 Source

This project appears immediately after Chapter 8 in the *Ultimate Python Programming Handbook* as:

**Project 1: Snake, Water, Gun Game**

The handbook describes it as a program that plays Snake, Water, Gun with the user. fileciteturn14file0

## ✅ Status

**Project 01 — Implemented**
