# read a mathematic expression with parentessis
# analise and show if the expression has parentesis in the correct order(open and clossed correctely)

expression = input('Type a math expression: ')
stack = []

for symbol in expression:
    if symbol == '(':
        stack.append('(')

    elif symbol == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print('the expression is valid')

else:
    print('the expression is invalid')