# Assignment 2: Lexical Analyzer (Finite Automata)
**Formal Languages - EAFIT University (2026)**

## Author
* **Samuel Posada Londoño** - Systems Engineering Student.

---

## Project Description
This project implements a Lexical Analyzer focused on recognizing two specific types of tokens based on the **Figure 3.14** from the reference book *"Compilers: Principles, Techniques, & Tools"* (Aho, Lam, Sethi, & Ullman).

The program evaluates user-input strings through two Finite Automata (FA):
1. **Keyword Recognizer ("then"):** Follows states 12 through 17.
2. **Identifier Recognizer:** Follows states 9 through 11.

---

## Logistics and Requirements
* **Operating System:** Windows 10 / Windows 11.
* **Programming Language:** Python 3.10 or higher.
* **Tools Used:** * VS Code (Code Editor).
    * Windows PowerShell / CMD (Execution environment).
    * ANSI escape sequences for terminal coloring.

---

## Algorithm Explanation
The implementation simulates the behavior of transition diagrams using a state-based approach:

### 1. Finite Automaton for "then" (States 12-17)
The function `automata_then` processes the string character by character. It strictly follows the path `t -> h -> e -> n`. 
* **The "Other" transition:** To comply with State 17 (acceptance by a non-alphanumeric character), the code internally appends a space to the input. This triggers the transition to the final state without losing the "lookahead" logic.

### 2. Finite Automaton for Identifiers (States 9-11)
The function `automata_id` ensures the string follows the rule: `letter (letter | digit)*`.
* **State 9:** Validates the first character is a letter.
* **State 10:** Remains in this state as long as alphanumeric characters are read.
* **State 11:** Reached when a non-alphanumeric character is encountered (simulated via the internal padding).

### 3. Priority Logic
Since "then" could also be interpreted as a valid identifier, the program implements **Keyword Priority**. It first attempts to validate the string against the keyword automaton; if it fails, it proceeds to check the identifier automaton.

---

## How to Run the Program

1. Ensure you have **Python** installed on your Windows machine. You can check this by running `python --version` in your terminal.
2. Download the source file: `Assignment2.py`.
3. Open **PowerShell** or **Command Prompt** in the folder where the file is located.
4. Run the script using the following command:
   ```bash
   python Assignment2.py
