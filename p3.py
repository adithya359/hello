# Function to calculate the sum of n natural numbers 
def sum_of_natural_num(n):
    return n * (n+1)//2

#Input the value of n 
n = int(input("Enter a natural number : "))

#function call
result = sum_of_natural_num(n)

#print the result
print(f"The sum of  the first {n} natural number is : {result}")

