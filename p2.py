# Input dictionary of people and their ages
people = {
    "alexa": 18,
    "ray": 16,
    "mikey": 37,
    "levi":22,
    "light": 16 
    }
#count the naumber of people above the age of 18
count = 0
for age in people.values():
    if age > 18:
        count += 1
        
print(f"The total number of people above the age of 18 is :{count}")
        