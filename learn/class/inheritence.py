
# method overwriting        
class Dad:
    def house(self):
        print("red color")

class Son(Dad):
    def house(self):
        print("blue color")

s1=Son()
s1.house()