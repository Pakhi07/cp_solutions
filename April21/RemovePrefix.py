def remove(n,a,output):
    flag=-1
    for i in range(n):
        if a[i] in a[i+1:]:
            flag=i
    
    output.append(flag+1)

def test(t):
    output=[]
    for i in range(t):
        n=int(input())
        a=[]
        a = list(map(int, input().split()))
        remove(n,a,output)
    for i in output:
        print(i)

        
t=int(input())

test(t)
