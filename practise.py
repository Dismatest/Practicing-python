# const = [1,2,3]
# x,y,z = const
# print(x,y,z)
x = 5
def name(weight):
    return(weight + x)
print(name(92))

import random
from random import randint

print(randint(2,90))

numbers = [2,3,5,6,78,898,122]
print(random.choice(numbers))

all_names = []
name = input("please enter your name ")
if "bill" in name:
    all_names.append(name)
    print(all_names)
elif "bill" not in name:
    print("not me try again")

my_list = ["elizabeth", "joan", "bill", "ogot"]
my_list.insert(2, "odiwuor")
print(my_list)

