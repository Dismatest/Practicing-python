def fruits(food, **kwargs):
    for x in food:
        print(x)


sample_food = ["banana", "oranges", "coco"]
fruits(sample_food)

# Define `plus()`
def plus(a,b):
  sum = a + b
  return (sum, a)

# Call `plus()` and unpack variables
sum, a= plus(3,4)

# Print `sum()`
print(sum)


def summation(*args):
    total = 0
    for num in args:
        total += num
    return total


def prompt():
    num = int(input("pleas enter the number "))
    num_total = []
    for n in range(num):
        add = int(input("please enter the numbers you wish to add "))
        num_total.append(add)
        my_sum = summation(tuple(num_total))
        print(my_sum)


prompt()
