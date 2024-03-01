def LRU(strInput):
    ds=[]
    for char in strInput:
        if char in ds:
            ds.remove(char)
        ds.append(char)
    
    if len(ds) > 5:
        ds=ds[-5:]
    
    ds='-'.join(ds)
    return ds
    
print(LRU(["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]))
print(LRU(["A", "B", "A", "C", "A", "B"]))
print(LRU(["A", "B", "C", "D", "A", "E", "D", "Z"]))

#tokenize version:
def ArrayChallenge(strArr):
    cache = []
    result = []

    for char in strArr:
        if char in cache:
            # Move the character to the front if it exists in the cache
            cache.remove(char)
        cache.append(char)
        
    if len(cache) > 5:
        cache=cache[-5:]

    # Join the final state of the cache into a string separated by hyphens
    final_output = '-'.join(cache)

    # ChallengeToken interspersed with the final output
    # interspersed_output = ''.join([a + b for a, b in zip(final_output, "j4qx61iv9de")])
    
    token="j4qx61iv9de"
    out=[]
    for a,b in zip(final_output,token):
        out.append(a+b)
    index=token.index(b) 
    if index < len(token)-1:
        out.append(token[index + 1 : ])
    
    # return interspersed_output
    return ''.join(out)

# Test cases
print(ArrayChallenge(["A", "B", "A", "C", "A", "B"]))  # Output: Cj-4Aq-xB61iv9de
print(ArrayChallenge(["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]))  # Output: Ej-4Dq-xQ6-1Zi-vC9de

