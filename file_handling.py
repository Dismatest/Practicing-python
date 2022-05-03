def read_file():
    try:
     f = open("readMe.txt", "r")
     for i in f:
       if "work" in i:
           print("work experience")
       elif():
           print("No work experience found")
    except Exception as e:
        print(e)
    f.close()
read_file()

# class My_file:
#     def __init__(self):
#
#     def read_file(self):
#         try:
#             f = open(self, "readMe.txt")
#             for i in f:
#                 print(self, i)
#         except Exception as e:
#             print(self, e)
# read_instance = My_file()
# read_instance.read_file()
