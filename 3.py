import os
os.system("cls")

file = open("product_material.txt", "r")

lst = file.readlines()

for i in range(len(lst)):
    lst[i] = lst[i].split(",")
    if lst[i][4] == "false\n" and float(lst[i][3][1:]) < 1000:
        print(lst[i][2])