def check_brackets(s):
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in bracket_map:
            stack.append(char)
        elif not stack or bracket_map[stack.pop()] != char:
            return "Unbalanced delimiters or mismatched delimiter pair"

    return "Balanced delimiters" if not stack else "Unbalanced delimiters"


if __name__ == '__main__': 
    test_cases = [
        "({[]()(){}{}})",
        "(({))",
        "({}"
    ]
    for case in test_cases:
        print(f"{case} is {check_brackets(case)}")
