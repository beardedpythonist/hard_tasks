
# что то поменял 18/11
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 == x2 or y1 == y2):  # ЛАДЬЯ
    print("YES")
elif (x2 == x1 + 1 or x2 == x1 - 1) and (y2 == y1 + 1 or y2 == y1 - 1):   # СЛОН ДАЛЬШЕ
    print("YES")
elif (x2 == x1 + 2 or x2 == x1 - 2) and (y2 == y1 + 2 or y2 == y1 - 2):
    print("YES")
elif (x2 == x1 + 3 or x2 == x1 - 3) and (y2 == y1 + 3 or y2 == y1 - 3):
    print("YES")
elif (x2 == x1 + 4 or x2 == x1 - 4) and (y2 == y1 + 4 or y2 == y1 - 4):
    print("YES")
elif (x2 == x1 + 5 or x2 == x1 - 5) and (y2 == y1 + 5 or y2 == y1 - 5):
    print("YES")
elif (x2 == x1 + 6 or x2 == x1 - 6) and (y2 == y1 + 6 or y2 == y1 - 6):
    print("YES")
elif (x2 == x1 + 7 or x2 == x1 - 7) and (y2 == y1 + 7 or y2 == y1 - 7):
    print("YES")
elif (x2 == x1 + 8 or x2 == x1 - 8) and (y2 == y1 + 8 or y2 == y1 - 8):
    print("YES")
else:
    print('NO')