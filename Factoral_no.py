# number = int(input("Enter the number: "))
# fact = 1
# for num in range(1,number+1) :
#     fact *= num
#     print(f"Factoral of number {number} is : {fact}")


number = int(input("Enter the number: "))
fact = 1
i = 1
while i <= number:
    fact = i *fact
    i += 1

print(f"Factoral of number {number} is : {fact}")
