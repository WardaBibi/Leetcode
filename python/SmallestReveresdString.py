def reveredStrings(word):
    smallest=word
    for i in range(len(word)):
        newWord=word[:i][::-1]+word[i:]
        if newWord < smallest:
            smallest=newWord
    
    for i in range(1,len(word)+1):
        newWord=word[:-i] +word[-i:][::-1]
        if newWord < smallest:
            smallest=newWord
            
    return smallest

print(reveredStrings("dbaca"))
    
    
