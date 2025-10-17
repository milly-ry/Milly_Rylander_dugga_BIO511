#Make list for input data
numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]

#a) Identify numbers with absolute value over 10. Print sum.
sum_over_ten = 0 #Make a sum variable that starts at 0
for n in numbers: #iterate over all numbers
    if abs(n) >= 10: #if abs(n), the absolute value of n, is higer or equal to 10...
        sum_over_ten += n #we add the number to the sum variable 
#I print the sum of the numbers
print(f"Sum of numbers with absolute value >=10: {sum_over_ten}")

#b) cubes of negative numbers
cubes_negative = [] #make an empty list of cubes of negative values
for n in numbers:#iterate over all numbers
    if n <0: #If the number is less than 0, it is negative and we want to cube it
        cube_n = n**3 #I get the cube of the negative number and assign to a variable
        cubes_negative.append(cube_n) #I append the cube to the list of negative cubes
#I print the list of negative cubes
print(f"List of negative number cubes: {cubes_negative}")

#c) first repeated absolute value
unique_n = [] #I create an empty list for unique absolute values of numbers in "numbers" list
duplicate_n = False #I set the value of duplicate_n to False, because we havent found a duplicate yet.

for n in numbers: #Iterate over all numbers 
    abs_n = abs(n) #I create a variable that represent the absolute value of the number
    if abs_n not in unique_n: # if the value is not in the list of unique values i add it with append
        unique_n.append(abs_n)
    elif abs_n in unique_n: #If the value already is in the list we have found a duplicate
        print(f"Found first duplicate! {abs_n} was found more than once")
        duplicate_n = True #I set the duplicate_n variable to True when we find a duplicate
        break #I only want the first duplicate so I break out of the loop when I've found it

if duplicate_n == False: #If we never found a duplicate the duplicate_n variable should still be set to false
    print("No repeats") #we print that no repeats were found
