class Agent():

    origin = "USA"

    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

x = Agent('Jose', 183, 75)
print(x.name)
print(x.weight)
x.weight = 180
print(x.weight)
