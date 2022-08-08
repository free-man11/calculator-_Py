#Write a program that produces the sum of all prime numbers less than a given number say n
#Prime numbers are numbers that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).
#So let's start with the coding.

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
