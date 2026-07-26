age=19
have_license="lr"

if age>=18 :
    if have_license=="yes" :
        print("yes you have license")
    elif have_license=="lr" :
        print("u have lr only")
    else :
        print("no license")
else:
    print("ur not eligible for driving")

amount=1000
days="mon"
membership="no"

if (amount>=1000 and days in ['sat','sun']) or membership=="yes" :
    print("ur eligible membership")
else :
    print("ur not eligible membership")