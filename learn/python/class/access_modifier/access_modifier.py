"""
var a= "public"
var _b="protected"
var __c="private"
"""


"""
var a= "public"
var _b="protected"
var __c="private"
"""

class Parent:
    def __init__(self):
        self.public="public"
        self._protected="protected"
        self.__private="private"
    def access_same_class(self):
        print("i am from parent class start")

        print(self.public)
        print(self._protected)
        print(self.__private)

class Child(Parent):
    def access_from_aubclass(self):
        print("i am from child class start")
        print("public from parent",self.public)
        print("public from parent",self._protected)
        try:
            print("private from parent",self.__private)
        except AttributeError:
            print("private cannot access modifier")



class Stranger:
    def access_other_class(self,obj):
        print("i am from strange class start")
        print(obj.public)
        print(obj._protected)
        try:
            # print("private from parent", obj.__private)
            print("private access in python only parent",  obj._Parent__private)

        except AttributeError:
            print("private cannot access modifier")


parentObj= Parent()
print(parentObj.access_same_class())

child = Child()
child.access_from_aubclass()

stranger = Stranger()
print(stranger.access_other_class(parentObj))
