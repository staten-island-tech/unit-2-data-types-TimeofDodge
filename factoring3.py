num1 = int(input("num1"))
num2 = int(input("num2"))
gcf = 1

for i in range(1, max(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        gcf = i
print(f"{gcf} is the greatest common factor.")