# multilevel
class Grandpha:
    def car(self):
        print ("red color")


class Dad(Grandpha):
    def house(self):
        print ("bule color")


class Son(Dad):
    def factory(self):
        print ("son factory")

son=Son()
son.car()
son.house()
son.factory()


# hierarky
class Dady():
    def house(self):
        print ("bule color")


class Son1(Dady):
    def factory(self):
        print ("son1 factory")
class Son2(Dady):
    def market(self):
        print ("son2 market")
               

son1=Son1()
son1.house()
son1.factory()

son2=Son2()
son2.house()
son2.market()

# multiple inheritence
class Dady():
    def house(self):
        print ("dad house  color")
class Mom():
    def money(self):
        print ("Mom money")
class Daughter(Dady,Mom):
    def market(self):
        print ("Daughter market")

daughter=Daughter()
daughter.house()
daughter.money()
daughter.market()