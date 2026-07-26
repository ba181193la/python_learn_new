# a=input("enter number: ")
# b=input("enter another number: ")
import sys;

''''
if len(sys.argv)==2:
    print("eneter name properly")
    sys.exit()

first_name=sys.argv[1]
last_name=sys.argv[2]

email=first_name.lower().replace("_",".")+"@gmail.com"
email_with_last_name=first_name.lower()+"."+last_name.lower()+"@gmail.com"

print(first_name)
print(email)
print(email_with_last_name)

'''

# first_name=sys.argv[1:]
# print(first_name) #  print ['bala', 'murugan', 'a', 'b', 'c']

firt_name=" ".join(sys.argv[1:])
print(firt_name)
email=firt_name.lower().replace(" ",".")+"@gmail.com"
print(email)





# run command
# python3 ./terminal/system.py bala_murugan
