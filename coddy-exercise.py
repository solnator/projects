x = [2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(x)):
    print(x[i] * 2, x[i] ** 2, x[i] ** 3)


n = int(input())
for i in range(n):
    print("*" * n(i + 1))


def prod(lst):
    product = 1
    for number in lst:
        product *= number
    return product


def is_valid(username, password):
    if username == "admin":
        return True  # Any password is valid for "admin"
    elif username == "user" and password == "qweasd":
        return True  # Only this password is valid for "user"
    else:
        return False  # Invalid username or password


def reverse(numbers):
    return numbers[::-1]


phy = eval(input())
che = eval(input())
bio = eval(input())
mat = eval(input())
subject = (phy, che, bio, mat)
print("average =", sum(subject) / len(subject))
