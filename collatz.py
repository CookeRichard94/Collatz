#The Number we will perform the collatz on
n = int(input("Enter a positive number: "))

#Keep looping iuntil we reach 1
#Note: This assumes the collatz conjecture is true
while n != 1:
    # Print the current value of n
    print(n)
    #Check if n is even
    if n % 2 == 0:
        #if even divide by two
        n = n // 2
    else:
        #if n is odd, multiply by 3 and add 1
        n = (3*n) + 1
    
#Print the 1
print(n)