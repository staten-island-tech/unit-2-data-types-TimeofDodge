num = int(input("What number would you like to factor"))

def num_factor():
    for jonkler in range(1, num + 1):
        if num % jonkler == 0:
            print(jonkler)

num_factor()
