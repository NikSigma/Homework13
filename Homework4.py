num = int(input("Введіть число: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            print(f"{num} не є простим числом")
            break
    else:
        print(f"{num} є простим числом")
else:
    print(f"{num} не є простим числом")
