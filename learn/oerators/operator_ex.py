
amount=1000
tax=0.10
total=amount+tax
print(total)

if total>=1000:
    print(f"Total is greater than 1000 and total={total}")
    discount=total*0.10
    total-=discount


print(f"Final total - {total}")

mark=1

if mark>=50 and mark<=60:
    print("your grade c")
elif mark>=61 and mark<=70:
    print("your grade b")
elif mark>=71 and mark<=80 or mark>=81 and mark<=100:
    print("your grade a")
else:
    print("your grade is fail")


    