def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    left_count = 0
    right_count = 0

    for p in parens:
        if p == '(':
            left_count += 1
        elif p == ')':
            right_count += 1

        if left_count < right_count:
            return False
    return left_count == right_count
print(valid_parentheses("((())")) 
print(valid_parentheses("(()())"))

