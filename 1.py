import os
os.system("cls")

file = open("product_material.txt", "r")

lst = file.readlines()

for i in range(len(lst)):
    lst[i] = lst[i].split(",")
    if 500 < float(lst[i][3][1:]) and float(lst[i][3][1:]) < 1000 and lst[i][4] == "true\n":
        print(lst[i][0], lst[i][2])

file.close()