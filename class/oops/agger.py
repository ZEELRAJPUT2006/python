class sample:
    id = 10
    name = "abc"

    def display(self):
        return f"my name is {self.name} and and it is {self.id}"
    
class Demo:
    s = sample()
    def show(self):
        return "sho calling"
    
d = Demo()
d.s.display()
print(d.s.display())