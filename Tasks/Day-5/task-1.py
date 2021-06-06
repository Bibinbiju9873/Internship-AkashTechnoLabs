class cal1:
    def setdata(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def display(self):
        ans1 = self.a + self.b + self.c
        print("{}+{}+{}={}".format(self.a, self.b, self.c, ans1))


obj1 = cal1()
obj1.setdata(10, 20, 30)
obj1.display()
