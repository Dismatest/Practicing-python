class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        # self.sides = [i for i in range(no_of_sides)]

    def inputSides(self):
        self.side = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.side[i])


class Triangle(Polygon):
    def __init__(self):
        # can also use supper().__init__() method
        # Polygon.__init__(self,3)
        super().__init__(3)

    def findArea(self):
        a, b, c = self.side
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)


t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()

