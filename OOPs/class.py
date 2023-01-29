class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def move(self,num):
        print("move"+num)

    def draw(self):
        print("draw")
    
    def points(self):
        print(self.x)
        print(self.y)

point1 = Point(10,20)
point1.move("hi")
point1.points()