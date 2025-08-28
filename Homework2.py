year = int(input("Введіть рік: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} рік є високосним.")
else:
    print(f"{year} рік не є високосним.")
