def collatz(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1
num = int(input("Enter the number:"))
print(num)
while True:
    num = collatz(num)
    print(num)
    if num == 1:
        break
