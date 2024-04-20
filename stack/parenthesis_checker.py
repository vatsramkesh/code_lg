"""
Given an expression string exp, write a program to examine whether
 the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.

"""

def is_balances(input_str: str) -> bool:

    # mapping = {"}": "{", ")": "(", "]", "["}

    my_stack = []

    for i in input_str:
        if i == '(':
            my_stack.append(')')
        elif i == '{':
            my_stack.append('}')
        elif i == '[':
            my_stack.append(']')
        else:
            if not my_stack or my_stack.pop() != i:
                return False
    return True if not my_stack else False


if __name__ == "__main__":

    assert is_balances("(({}))") == True
    assert is_balances("[()]]") == False