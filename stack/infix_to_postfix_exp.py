"""
Convert an infix(human readable) exp to postfix(machine executable ready) format 
"""
def postfix(exp: str) -> str:
    '''
    Algo: At a there could be 4 option while iteration over the input exp:
    1. it is opening brancket (): Push to stack
    2. it is an operand: Print it or add to output list.
    3. Closing bracket: Pop from stack untill you get opening bracket(included) and print or add it to output list
    4. Operator:
        if Stack is empty: Push to stack
        else:
            compare the precedence of top of stack with current item:
            if its top of stack has higher precedence than current, pop the top of stack and print or add ot to output list
            and push current item to stack
            else: push current operator to stack.
    '''
    
    my_stack = []
    ret = []
    precedence = {"+": 1, "-": 1, "/": 2, "*": 2}
    
    for i in exp:
        if i == "(":
            my_stack.append(i)
        elif i in ("+-*/"):
            # If stack is empty
            if not my_stack:
                my_stack.append(i)
            else:
                top = my_stack[-1]
                # Compare precedence of current operator
                if top in precedence and precedence[top] >= precedence[i]:
                    ret.append(my_stack.pop())
                    my_stack.append(i)
                else:
                    my_stack.append(i)
        elif i == ")":
            while my_stack[-1] != "(":
                ret.append(my_stack.pop())
            # Removeing "(" as well
            my_stack.pop()
        else:
            ret.append(i)
    while my_stack:
        ret.append(my_stack.pop())
    return "".join(ret)


if __name__ == "__main__":
    assert postfix("a+b*(d+e)") == "abde+*+"
    assert postfix("a*b/(d+c)*e") == "ab*dc+/e*"
    