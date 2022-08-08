num = input("Enter the ending value")
num = int(num)
sum = 0

#print numbers from 2 to n
for i in range(2, num):
    for j in range(2, i):
#checks whether number i%j is equivalent to 0
        if (i % j == 0):
            break
    else:
        print(i)
        sum = sum + i

print("Sum of prime number is", sum)
