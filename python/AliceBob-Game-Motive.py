
# def winner(numbers):
#     stack=[]
#     win=0
#     for i in numbers:
#         if len(stack)==0 or stack[-1]!=i:
#              stack.append(i)
#         else:
#             stack.pop()
#             win+=1
#     if win%2 ==0:
#         return 'Bob'
#     else:
#         return 'Alice'

# print(winner([4,2,3,3,2,4]))

#second method

def winner(numbers):
    win=0
    i=0
    while(i < len(numbers)-1):
        # print(numbers)
        # print(i)
        if numbers[i]==numbers[i+1]:
            numbers.pop(i)
            numbers.pop(i)
            win+=1
            if i == 0:
                i=-1
            else:
                i=i-2
        i+=1
        # print(i)
                
    if win%2==0:
        return 'Bob'
    else:
        return 'Alice'
        
print(winner([4,2,3,3,2,1]))

                
                
            
            
            
