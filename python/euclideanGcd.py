def gcd(a,b):
    rem=a%b
    if rem ==0 :
        return b
    return gcd(b,rem)
    
a=10
b=16
first=max(a,b)
second=min(a,b)

print(gcd(first,second))
