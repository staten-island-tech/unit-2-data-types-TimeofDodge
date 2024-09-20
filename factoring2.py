def num_factor(x):
    for jonkler in range(1, x + 1):
        if x % jonkler == 0:
            print(jonkler)




num = int(input("What number would you like to factor"))
y = int(input("sigma"))

gcf1 = num_factor(num)
gcf2 = num_factor(y)
