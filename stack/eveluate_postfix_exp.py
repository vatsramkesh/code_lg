"""
Eveluate the postfix expression or postfix to infix
"""

def eveluate_postfix(exp: str) -> str:
    '''
    if operand: push to stack
    if operator: pop top as second and opp again as first and apply
    eval(first operator second) and push result back to stack
    return top of stack as result.
    '''
    pass