# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
second_list = ["bill", "clinton", "ogot"]
my_list = []

for item in second_list:
    if "o" in item:
        my_list.append(item)
print("the saved new list is", my_list)

# list comprehension
third_list = ["solomon", "matilda", "bill", "mwelusi"]
fouth_list = [x.upper() for x in third_list if "m" in x]
print(fouth_list)


def sort_mylist(number):
    return number-200
m_list = [5,10,15,20,25,30,35,40,50,55,60,56,100]
m_list.sort(key=sort_mylist)
print(m_list)


# unpacking lists and tuple
m_lists = [1,2,3,4,5,6]
[q,w,e,r,t,x] = m_lists
print(e)


