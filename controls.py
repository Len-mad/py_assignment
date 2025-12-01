#chek the number is even or odd

# #get the number
number=int(input("Enter a number: "))

#conditional statement to check the number is even or odd.

if number%2==0:
    print(number,"is an even number")

else:
    print(number,"is an odd number")


#sumb of integers from 1 to 50 using a loop

total =0
for i in range(1,51):
    total += i
print("The sum of numbers from 1 to 50 is : ", total)

print("The sum of numbers from 1 to 50 is : ", sum(range(1,51)))