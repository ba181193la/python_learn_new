
# *****************for****************
# name_list=["bala","murugan"]

# for index, name in enumerate (name_list):
#     print("name",name)

# range_no=range(10)
# print(range_no) #range(0, 10)

# for number in range_no:
#     if number==5:
#         break
#     print(number)


# number=[1,-2,-3,-4,2,3,4,5-6]
# positive_num=[]
# for num in number:
#     if num <0:
#         continue
#         # break
#     positive_num.append(num)
# print(positive_num)

# *********************while loop*************
# correct_pin="12345"
# enter_pin="123"

# while enter_pin!=correct_pin:
#     print("eneter pin")
#     enter_pin=input("eneter your pin"+" ")
# print("pin is correct")
name_list=[]
while True:
    input_name=input("eneter name"+":")
    if input_name.lower()=="bala":
        break
    name_list.append(input_name)

print("name_list",name_list)




