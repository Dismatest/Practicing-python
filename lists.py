numbers = []
my_numbers = int(input("please enter the number to iterate: "))
for x in range(my_numbers):
    number = int(input("enter the first number: "))
    numbers.append(number)
print("the sum of the numbers is: ", sum(numbers))

def mysum():
    number = []
    my_numbers = int(input("please enter the number to iterate: "))
    for iterarable in range(my_numbers):
      num = int(input("enter the first num"))
      number.append((num))
      print("the sum is ", sum(number))
mysum()



