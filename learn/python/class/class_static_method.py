
# class Method
# class Emmployee:
#     companyName="Open Ai"
#     @classmethod
#     def getName(cls,myName):
#         cls.companyName=myName
# print(Emmployee.companyName)
# Emmployee.getName("google")
# print(Emmployee.companyName)

# static method:

class Emmployee:
    companyName="Open Ai"
    @classmethod
    def change_company_name(cls,myName):
        cls.companyName=myName
    @staticmethod
    def try_change_company_name(myName):
        companyName=myName

print(Emmployee.companyName)
Emmployee.change_company_name("google")
print("after company name chnage- class method",Emmployee.companyName)

Emmployee.try_change_company_name("META")
print("after company name chnage- static method",Emmployee.companyName)





