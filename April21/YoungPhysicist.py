
def test(t):
    x=0
    y=0
    z=0
    for i in range(t):
        v = list(map(int, input().split()))
        x=x+v[0]
        y=y+v[1]
        z=z+v[2]
    if x == 0 and y == 0 and z == 0:
        print("YES")
    else:
        print("NO")

t = int(input())
test(t)