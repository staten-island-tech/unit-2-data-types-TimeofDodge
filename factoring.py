num = int(input("What number would you like to factor"))

def num_factor():
    for jonkler in range(num):
        if num % jonkler == 0:
            print(num)

num_factor()
