
# name="balamurugan"

# print("name-lower",name.lower())
# print("name-upper",name.upper())
# print("name-capitalize",name.capitalize())

# **********Tittle******************

# name='myname balamurugan'
# formatted=f"{name.title()}"
# print("format-",formatted)

# song="shape OF you"
# print("format-",f"{song.title()}")

# *******************************
# print("first two",name[:2])
# print("last Two",name[-2:])
# masked_phone_no="7397636240"
# print(masked_phone_no[:2]+"******"+masked_phone_no[-2:])

# ****************split*****************
# order_message="you have got order on : USB12345"
# split_message=order_message.split(":")

# print("split_message",split_message)
# print("split_message [0]",split_message[0])
# print("split_message [1]",split_message[1])

#*********** strip******************
# ID=split_message[1].strip()
# ID1=order_message.split(":")[1].strip()
# print("split_message [1]-strip ID",ID1)

# *************JOIN***********************
# name="bala murugan"
# join_name="_".join( name.split(" "))
# print(join_name)

# ************check string use "in" ************************
# result="Kit college anounced ths result id 101 and 102 is top"

# if "101" in result:
#     print("101 is balamurugan")
# else:
#     print("your name is not here")

# *************check find position **************************
# feedback="the student is good and name balamurugan"
# print("name position is",feedback.find("student"))

#************* example of strin using for loop *****************
# full_name = "Bala Murugan"

# for index, word in enumerate(full_name.split(" ")):
#     print("index",index, "word", word)

# for word in full_name.split(" "):
#     print("word",word)

# initail=([word[0].upper() for word in full_name.split(" ")])
# finish="".join([word[0].upper() for word in full_name.split(" ")])
# print("initail",initail)
# print("initail",finish)

# **************Strinhg lenth************************

message="India won the match the 2011"
print("before split",len(message))
print("after then split message",len(message.split("the")))
print("after then split message",len(message.split()))

