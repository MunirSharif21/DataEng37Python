def add_plus_one(num1, num2):
    return num1 + num2 + 1


print(add_plus_one(3, 7))

# lambda (anonymous) functions

addition = lambda num1, num2: num1 + num2 + 1

print(addition(5, 8))

# map

savings = [234.00, 555.00, 647.25, 839.00]
# bonus = savings with 10% added on
# loops are slow and computationally heavy
bonus = []
for saving in savings:
    bonus.append(saving * 1.1)
print(bonus)


def apply_bonus(savings):
    return savings * 1.1


bonus_map = list(map(apply_bonus, savings))  # make it a list
print(bonus_map)

bonus_lambda = list(map(lambda x: x * 1.1, savings))
squared_bonus = map(lambda x: x ** 2, bonus_lambda)
print(list(squared_bonus))

# total = sum(bonus_lambda)
# print(total)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use lambda to create a list of each number squared plus 3
ans = map(lambda x: (x ** 2) + 3, numbers)
# print(list(ans))

evens = filter(lambda x: x % 2 == 0, ans)
print(list(evens))
# printing list(ans) once will not allow you to do it again

jobs = ["Data Analyst", "C# Developer", "Data Engineer", "DevOps Engineer", "Data Architect"]
# using map and filter with lambdas
# produce a list of data based roles
# without the word data in there
data_lambda = filter(lambda role: "Data" in role, jobs)  # find roles with data in the name
data_map = map(lambda title: title.replace("Data ", ""), data_lambda)  # remove the word data
print(list(data_map))  # print the list
