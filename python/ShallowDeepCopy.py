#list,dict,are mutable, thet get pass by refrence when calling function so  they get chnaged 
# Goal of Shallow and Deep copy is to keep them unchnaged when passed as arguments to fntncs


#shallow copy  #only objects are referenced in 1d array
# import copy
# def append_to(num, target=None):
#     if target is None:
#         target=[]
#     target=copy.copy(target)
#     target.append(num)  , this is fine only new array will be updated original will not be updated because individual objects are refrenced so only chnagng them would make original also change but appending new wlwments woun't affect original_list
#     target[1]=8 , this is not fine  bcz new array as well as original would be updated bcz refrenced object is changed 
#     return target

# original_list = [1, 2, 3]
# new_list = append_to(4, original_list)

# print(original_list) 
# print(new_list) 

#---------------------------------------------------------------------------------------------
# Another shallow copy example for 2d array:
# def append_to(num, target=None):
#     if target is None:
#         target=[]
#     target=copy.copy(target)
#     target[0].append(num) , this is not fine  bcz new array as well as original would be updated bcz refrenced object is changed so we should do deep copy in order to keep original list unchanged
#     target.append(num)  , this is fine only new array will be updated original will not be updated because individual objects are refrenced so only chnagng them would make original also change but appending new wlwments woun't affect original_list
#     target[1]=8 , this is not fine  bcz new array as well as original would be updated bcz refrenced object is changed 
#     return target

# original_list = [[1, 2], 3]
# new_list = append_to(4, original_list)

# print(original_list) 
# print(new_list)









# ----------------------------------------------------------------------
# solution of above problem where shallow copy fails



#deepcopy #individual Objects are referenced recursively in 2d array
import copy
def append_to(num, target=None):
    if target is None:
        target=[]
    target=copy.deepcopy(target)
    target[0].append(num) # this is  fine  bcz only new array  would be updated bcz  refrenced object is appended
    #taget[0][0]=num    , this is not fine again it would change original list too bcz reference recursive object is changed s

    target[0].append(num)
    return target

original_list = [[1, 2], 3]
new_list = append_to(4, original_list)

print(original_list) 
print(new_list) 



#--------------------------------------------------------------------------------
= copy beavuior:

arr=[[1,2],3]
newarr=arr
newarr[1]=5 #change original + new so its showing shallow behavior
newarr[0].append(0) #change original + new s its showing shallow behavior
newarr.append(0) #change original + new so its not shallow behaviour 
 # so this = beahviour is kind of shallow but also changes incase of append

print(newarr)
print(arr)
