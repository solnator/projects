nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = eval(input())
if x in nums:
    print("Your list have contains.")
else:
    print("There is no contains on your list")


x = input("Enter a numbers: ")
print("The first number is: ", x[0])


def reverse():
    # Prompt the user to input numbers separated by spaces
    numbers = input("Enter numbers separated by spaces: ")

    # Convert the input string into a list of numbers
    numbers = list(map(int, numbers.split()))

    # Return the reversed list
    return numbers[::-1]


# Example usage
reversed_numbers = reverse()
print("Reversed list:", reversed_numbers)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nums.append(16)  ####### .append = add on the end of the list.
average = sum(nums) / len(nums)
print("Sum = ", sum(nums))
print("Number = ", len(nums))
print("Average = ", average)

#### Methode             ##### Description
## append(x)             adds x to the end of the list
## sort()                sorts the list
## count(x)              returns the number of times x occurs in the list
## index(x)              returns the location of the first occurrence of x
## reverse()             reverses the list
## remove(x)             removes first occurrence of x from the list
## pop(p)                removes the item at index p and returns its value
## insert(p,x)           inserts x at index p of the list

####### help(list)    is show some help methode

from random import randint

L = []
for i in range(50):
    L.append(randint(1, 100))
print(L)

count = 0
for item in L:
    if item > 50:
        count = count + 1
print(count)

####### Example ########
num_right = 0
# Question 1
print("What is the capital of France?", end=" ")
guess = input()
if guess.lower() == "paris":
    print("Correct!")
    num_right += 1
else:
    print("Wrong. The answer is Paris.")
print("You have", num_right, "out of 1 right")
# Question 2
print("Which state has only one neighbor?", end=" ")
guess = input()
if guess.lower() == "maine":
    print("Correct!")
    num_right += 1
else:
    print("Wrong. The answer is Maine.")
print("You have", num_right, "out of 2 right,")


questions = ["What is the capital of France? ", "Which state has only one neighbor? "]
answers = ["Paris", "Maine"]
num_right = 0
for i in range(len(questions)):
    guess = input(questions[i])
    if guess.lower() == answers[i].lower():
        print("Correct")
        num_right = num_right + 1
    else:
        print("Wrong. The answer is", answers[i])
    print("You have", num_right, "out of", i + 1, "right.")
