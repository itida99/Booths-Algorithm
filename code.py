def binary(n):
    if(n==0):
        return [0]
    if(n>0):
        l=[]
        while(n>1):
            l.append(n%2)
            n=n//2
        l.append(1)
        l.append(0)
        l.reverse()
        return l
    if(n<0):
        k = abs(n)
        l = binary(k)
        l = twos_compliment(l)
        return l

def ones_compliment(l):
    for i in range(0,len(l)):
        l[i]=1-l[i]//1
    return l

def add(a,b):
    i = len(a)-1
    j = len(b) - 1
    res = []
    carry = 0
    while(i>-1 or j>-1):
        k=0
        if(i>-1):
            k+=a[i]
            i-=1
        if(j>-1):
            k+=b[j]
            j-=1
        k+=carry
        # print(k,"***")
        carry = k//2
        k = k%2
        # print(k)
        res.append(k) 
    if (carry==1 and a[0]==b[0]):
        res.append(1)
    res.reverse()
    return res
    

def twos_compliment(l):
    l = ones_compliment(l)
    l = add(l,[0,1])
    return l

def right_shift(a,q,q_not):
    q_not[0] = q[-1]
    q[1:] = q[0:-1]
    q[0] = a[-1]
    a[1:] = a[0:-1]
    
def decimal(l):
    if(l[0]==0):
        ans = 0
        j = 0
        for i in l[::-1]:
            ans+=i*(2**j)
            j+=1
        return ans
    else:
        l = twos_compliment(l)
        ans = decimal(l)
        return -1*ans

def make_n_bits(l,n):
    if(l[0]==0):
        l.reverse()
        while(len(l)<n):
            l.append(0)
        l.reverse()
    else:
        l.reverse()
        while(len(l)<n):
            l.append(1)
        l.reverse()
    return l

m = int(input("Enter the multiplicand: "))
q = int(input("Enter the multiplier: "))
m = binary(m)
q = binary(q)
q_not = [0]
n= max(len(q),len(m))
q = make_n_bits(q,n)
m = make_n_bits(m,n)
print("The multiplicand in binary form is:",m,"\nThe multiplier in binary form is:",q)
a = [0 for i in range(n)]
print("step"+" "*(n//2)+"  Accumulator"+" "*(5*n//2)+"Q"+" "*(5*n//2)+"Q_not")
g = 1
while(n!=0):
    print(g,"  ",a,"  ",q,"  ",q_not)
    if(q_not[0]==q[-1]):
        right_shift(a,q,q_not)
        # print(a,q,q_not,"after work 1")
    elif(q[-1]==1 and q_not[0]==0):
        m = twos_compliment(m)
        a = add(a,m)
        m = twos_compliment(m)
        # print(a,q,q_not)
        right_shift(a,q,q_not)
        # print(a,q,q_not,"after work 2")
    elif(q[-1]==0 and q_not[0]==1):
        a = add(a,m)
        # print(a,q,q_not)
        right_shift(a,q,q_not)
        # print(a,q,q_not,"after work 3")
    n-=1
    g+=1
print(g,"  ",a,"  ",q,"  ",q_not)
ans = a+q
print("The answer in its binary form is:", ans)
print("The answer inr its decimal form:", decimal(ans))
