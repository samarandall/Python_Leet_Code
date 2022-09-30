tokens = ["2","1","+","3","*"]
def evalRPN(tokens):
    stack = []

    for token in tokens:

        if token == '*': 
            right = stack.pop()
            left = stack.pop()
            stack.append(left*right)
        elif token == '+':
            right = stack.pop()
            left = stack.pop()
            stack.append(left+right)
        elif token == '-':
            right = stack.pop()
            left = stack.pop()
            stack.append(left-right)
        elif token == '/':
            right = stack.pop()
            left = stack.pop()
            stack.append(int(float(left/right)))
        else:
            stack.append(int(token))
   
                
    return stack[0]
        
print(evalRPN(tokens))