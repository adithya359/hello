# Input the number of elements
n = int(input("Enter the number of elements in the list: "))

# Input the elements from the user
elements = []
for i in range(n):
    value = int(input("Enter the elements : "))
    elements.append(value)
    
#calculate the average and print the values
avg = sum(elements) / n
print(f"The average of the list elements is : {avg}")