def batonPass(friends, time):
  # Calculate total cycle time (forward + backward)
  cycle_time = friends * 2 - 2

  # Find position within the cycle (1-based indexing)
  position = time % cycle_time

  # Determine direction (forward or backward)
  if  position ==0:
      return [2,1]
  elif position < friends:
    passer = position
    receiver = position + 1
    return [passer, receiver]
  else:
    passer = friends - 1 - (position - friends)
    receiver = passer - 1
    return [passer + 1, receiver + 1]


# def batonPass(friends,time):
#     i=0
#     j=0
#     while(True):
#         for i in range(1,friends):
#             time=time-1
#             if time==0:
#                 return [i,i+1]
            
#         for j in range(friends,1,-1):
#             time=time-1
#             if time==0:
#                 return[j,j-1]


