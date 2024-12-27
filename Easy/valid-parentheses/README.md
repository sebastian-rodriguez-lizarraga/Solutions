# Valid Parentheses

This repository contains the solution to the **Valid Parentheses** problem.

## Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

An input string is considered valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

### Example 1:

**Input:**
```plaintext
s = "()"
```

**Output:**
```plaintext
true
```

### Example 2:

**Input:**
```plaintext
s = "()[]{}"
```

**Output:**
```plaintext
true
```

### Example 3:

**Input:**
```plaintext
s = "(]"
```

**Output:**
```plaintext
false
```

### Example 4:

**Input:**
```plaintext
s = "([])"
```

**Output:**
```plaintext
true
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only: `'()[]{}'`.

## Solution Approach

The solution involves using a **stack** to keep track of open brackets and verifying if each closing bracket corresponds to the most recent open bracket. The algorithm ensures that all conditions for a valid string are met efficiently.

## Usage

Clone the repository and run the solution code using any Python interpreter. Ensure you have Python 3 installed.

```bash
git clone <repository-url>
cd <repository-folder>
python valid_parentheses.py
