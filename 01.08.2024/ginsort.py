n=input()
u=""
o=""
e=""
l=""
for i in sorted(n,reverse=False):
    if i>='a' and i<='z':
        l+=i
    elif i>='A' and i<='Z':
        u+=i
    elif i.isdigit()==1: 
        if int(i)%2==0:
            e+=i
        else:
            o+=i

print(l+u+o+e)
    
