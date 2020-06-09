class Rectangles:
    def __init__(self, width, length):
        self.width = int(width)
        self.length = int(length)

    def introduce_self(self):
        return (f"The area of the rectangle is {self.width * self.length} ")

rectangle1 = Rectangles(8, 9)
rectangle2 = Rectangles(12, 5)

introduce_rectangle1 = rectangle1.introduce_self()
print (introduce_rectangle1)