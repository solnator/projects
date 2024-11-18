########## Exercise 7.7 ###########
###### Question 1 ########
x = eval(input("Enter a list of integers separet by comma? "))
print("The total number of integers: ", sum(x))
print("The last item of the list: ", x[-1])
print("Reverse of the list: ", x[::-1])
print("The first and last strings are: ", x[0], "and", x[-1])
print("Without the first and last strings :", x[1:-1])

if 5 in x:
    print("Yes")
else:
    print("No")

count_of_fives = x.count(5)
print("There are ", count_of_fives, "five")
###################### Question 1(g)
less = sum(1 for x in x if x < 5)
print("There are ", less, "numbers less than 5.")


########### Question 2 #############
from random import randint

x = []
for i in range(50):
    x.append(randint(1, 100))
print(x)  ### Question_A
print("Average of the list", sum(x) / len(x))  ### Question_B
print("Smallest value is:", min(x), "and largest value is:", max(x))  ### Question_C
sorted_list = sorted(set(x))
second_smallest = sorted_list[1]
second_largest = sorted_list[-2]
print(second_largest, "and", second_smallest)  ### Question_D
even_numbers = sum(1 for y in x if y % 2 == 0)
print(even_numbers)  ### Question_E


######## Question 3 #############
num = [8, 9, 10]
num[1] = 17  ### Question_A
num = num + [4, 5, 6]  ### Question_B
num.remove(8)  ### Question_C
num.sort()  ### Question_D
num = num * 2  ### Question_E
num.insert(3, 25)  ### Question_F
print(num)


###### Question 4 ###########
user_input = input("Enter a list of numbers between 1 and 12, separated by spaces: ")

# Convert the input string into a list of integers
user_list = [int(num) for num in user_input.split()]

# Replace entries greater than 10 with 10
modified_list = [min(num, 10) for num in user_list]

print("Modified list:", modified_list)


######### Question 5 ############
user_input = input("Enter a list of strings, separated by spaces: ")
user_list = user_input.split()
# Create a new list with the first character removed from each string
modified_list = [s[1:] for s in user_list]
print("Modified list:", modified_list)


######### Question 6 ############
numbers = []
squares = []
for i in range(1, 51):
    numbers.append(i)  ### Question_A
    squares.append(i**2)  ### Question_B
print(numbers)
print("\n")
print(squares)

letter = []
for i in range(26):
    letter.append(chr(97 + i) * (i + 1))  ### Question_C
print(letter)

###### Question 7 ######
n = []
l = [3, 1, 4]
m = [1, 5, 9]
for i in range(len(l)):
    n.append(l[i] + m[i])
print(n)
