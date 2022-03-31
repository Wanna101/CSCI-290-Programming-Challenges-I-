
def digit(n):
    if n == 0:
        return 0
    return (n % 10 + digit(int(n / 10)))


number = int(input())
for i in range(number):
    first, second = input().split(' ')
    total = 0
    for j in range(int(first), int(second) + 1):
        total += digit(j)
    print(total)
    
    
