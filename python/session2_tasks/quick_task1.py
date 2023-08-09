list = [101, 5, 7, 1, 2, 45, 100, 10, 22, 100]
max = list[0]
for i in list:
    if i > max:
        max = i

print("largest num is " + str(max))
