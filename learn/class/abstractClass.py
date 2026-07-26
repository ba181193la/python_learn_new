
from abc import ABC,abstractmethod

class FeaturePlan(ABC):

    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
    # @abstractmethod
    def checkout(self):
        pass

class Subclass(FeaturePlan):
    def login(self):
        print("login")
    def logout(self):
        print("logout")
    def checkout(self):
        print("checkout")

sub=Subclass()
sub.logout()
sub.login()
sub.checkout()

