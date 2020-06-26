#Python program to find binary of a decimal number two method

def binary(n):
    if n > 1:
        binary(n // 2) # we must give floor division here else cause decimal value
    print(n % 2 ,end="")
    
x = int(input("Enter the decimal number to find binary : "))

print("\n The binary of the decimal number ",x," is ",end="")

binary(x) # calling the function


# Another method to find binary of a number

print("\n\n Binary number using bin function is " + bin(x)) # by bin()