import os
os.system("cls")

def func(line):
    return float(line[3][1:])

file = open("product_material.txt", "r")

lst = file.readlines()

material = input("material: ")

    
for i in range(len(lst)):
    lst[i] = lst[i].split(",")
    

lst.sort(key = func)

for i in range(len(lst)):
    if lst[i][2] == material and lst[i][4] == "true\n":
        print(lst[i][3])
        
file.close()