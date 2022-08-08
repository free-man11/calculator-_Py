#Write a program that produces the sum of all prime numbers less than a given number say n
#Prime numbers are numbers that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).
#So let's start with the coding.


lower = int(input("enter lower range: "))
upper = int(input("enter upper range: "))
sum = 0
prime = 0

#print numbers from lower range to upper range a user will input
for num in range(lower, upper + 1):
    if num > 1:
        
#checks whether number num % j is equivalent to 0 and that will be even
        for i in range(2, num):
          if (num % i) == 0:
            break

        else:
            print(num)
            sum = sum + num
            prime = prime+1

print("sum of prime numbers", sum)
print("average of prime is",sum/prime)
