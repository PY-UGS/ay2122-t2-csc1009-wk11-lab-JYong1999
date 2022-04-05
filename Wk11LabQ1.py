class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adder(self):
        value = self.x + self.y
        print("Addition =",value)

    def subtractor(self):
        value = self.x - self.y
        print("Subtraction =",value)

    def multiplier(self):
        value = self.x * self.y
        print("Multiply =",value)

    def divider(self):
        value = self.x / self.y
        print("Divide =",value)

    def clear(self):
        self.x = 0
        self.y = 0

val1 = input("Enter 1st value: ")
val2 = input("Enter 2nd value: ")
test = Calculator(int(val1),int(val2))
test.adder()
test.subtractor()
test.multiplier()
test.divider()
test.clear()
