class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*self.pi
    
    def perimeter(self):
        return 2*self.radius*self.pi

mycircle = Circle(radius = 4)

print(mycircle.area())
print(mycircle.perimeter())