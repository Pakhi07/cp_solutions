def min_moves(n):
    if n == 1:
        return 0
    elif n % 3 != 0:
        return -1
    else:
        count = 0
        while n > 1:
            if n % 6 == 0:
                n //= 6
            elif (n*2) % 3 == 0:
                n *= 2
            else:
                return -1
            count += 1
        return count

def test(t):
    for i in range(t):
        n=int(input())
        print(min_moves(n))
    
t=int(input())
test(t)