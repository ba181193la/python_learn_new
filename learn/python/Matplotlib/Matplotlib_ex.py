
# import matplotlib.pyplot as plt


# months = ["Jan", "Feb", "Mar", "Apr"]
# sales = [10000, 15000, 12000, 18000]

# plt.plot(months, sales)

# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")

# plt.show()

#****************** bar******************************

# import matplotlib.pyplot as plt

# employees = ["Bala", "Kumar", "Ravi", "Arun"]
# salary = [15000, 20000, 18000, 25000]

# plt.bar(employees, salary)

# plt.title("Employee Salary")
# plt.xlabel("Employee")
# plt.ylabel("Salary")

# plt.show()

# *******************scatter********************

# import matplotlib.pyplot as plt

# experience = [1, 2, 3, 4, 5]
# salary = [15000, 18000, 22000, 28000, 35000]

# plt.scatter(experience, salary)

# plt.title("Experience vs Salary")
# plt.xlabel("Experience (Years)")
# plt.ylabel("Salary")

# plt.show()


import csv
import matplotlib.pyplot as plt

dates = []
sales = []

with open("sales.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        dates.append(row["date"])
        sales.append(int(row["sales"]))

print(dates)
print(sales)

plt.plot(dates, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.show()