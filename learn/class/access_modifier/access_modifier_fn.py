
"""
var a= "public"
var _b="protected"
var __c="private"
"""

class Parent:

    def public_method(self):
        print("i am from parent class -public method")

    def _protect_method(self):
            print("i am from parent class -protect method")
    def __private_method(self):
        print("i am from parent class -private method")

    def access_from_same(self):
        print("i am from parent -access method")
        self.public_method()
        self._protect_method()
        self.__private_method()



class Child(Parent):
    def access_from_aubclass(self):
        print("i am from child class start")
        self.public_method()
        self._protect_method()
        try:
            self.__private_method()
        except AttributeError:
            print("private cannot access modifier")



class Stranger:
    def access_other_class(self,obj):
        print("i am from strange class start")
        obj.public_method()
        obj._protect_method()
        try:
            # obj.__private_method()
                        print("private access in python only parent",  obj.__private_method())

        except AttributeError:
            print("private cannot access modifier")


parent= Parent()
print(parent.access_from_same())

child = Child()
child.access_from_aubclass()

stranger = Stranger()
print(stranger.access_other_class(parent))


