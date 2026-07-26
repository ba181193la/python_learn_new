
# trip_summery=("ubergo","chennai","airport",450.00,"cmpleted","chennai")

# print(trip_summery)
# print(trip_summery[0])
# print(trip_summery[1])

# for item in trip_summery:
#     print(item)
# for index, item in enumerate(trip_summery):
#     print(f"index-{index}-item-{item}" )

# print(len(trip_summery))

# print("counting chennai",trip_summery.count("chennai"))
# print("find index",trip_summery.index("airport"))


# ************slice ****************
numbers = (10, 20, 30, 40, 50)
# print(numbers[1:4]) #start- end( before index)
print(numbers[:3]) #(10,20,30)
print(numbers[2:]) #(30,40,50)
print(numbers[::2]) #(10,30,50)
print(numbers[::-1]) #(50,40,30,20,10)




# fruits = ("apple", "banana")
# fruits[0] = "mango"

#************** Tuple unpacking **************
person = ("Bala", 25, "Developer")
name, age, job = person
print(name)
print(age)
print(job)

