
class Sample:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def view(self):
        print(f"say hello {self.name}-{self.age}")

s1=Sample("bala",23)
s1.view()

