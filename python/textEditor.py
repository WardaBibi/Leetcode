
def Undo(stack,undoText,k):
    stack.append(undoText)
    print(stack)
    prevLength=len(stack)
    k=k-2
    return prevLength,k
    
def textEditor(instructions):
    stack=[]
    flag=False
    k=-2
    text=""
    for i in instructions:
        if i.startswith('INSERT'):
            currentText=i.split()[1]
            text=text+currentText
            stack.append(text)
        elif i=='BACKSPACE':
            text=text[:-1]
            stack.append(text)
        elif i=='UNDO':
            if not flag:#first time only
                undoText=stack[-2]
                flag=True
            else:
               
                if len(stack)==prevLength:
                    if k*(-1) > len(stack):
                         continue
                    undoText=stack[k]
                    
                else:
                    undoText=stack[-2]
            prevLength,k=Undo(stack,undoText,k)
            
    return stack
            
print(textEditor(['INSERT CODE','INSERT SIGNAL','BACKSPACE','UNDO','UNDO']))
print(textEditor(['INSERT NOTHING','INSERT IS','INSERT PERMANENT','UNDO','UNDO']))
