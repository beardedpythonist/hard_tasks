# Магическим квадратом порядка n называется квадратная таблица размера   n×n, составленная из всех чисел
# так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
# Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы:
# n строк, по  n чисел в каждой, разделённые пробелами.
# Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.


n = int(input())
matrix = [0] * n
for i in range(n):
    matrix[i] = [] * n
s = ''
ls1 = []
x = n ** 2
ls_vsechisla = []
ls_moymatriza = []
for c in range(x):
    y = 1 + c
    ls_vsechisla.append(y)   # создание массива длинной 2 **n
for i in range(n):
    s = str(input())
    ls = s.split()
    ls_moymatriza.extend(ls)    # создание массива из элементов матрицы для проверки
    for j in range(len(ls)):
        ls[j] = int(ls[j])
        matrix[i].append(ls[j])
for c in range(len(ls_moymatriza)):
    ls_moymatriza[c] = int(ls_moymatriza[c])
ls_moymatriza.sort()
if ls_vsechisla == ls_moymatriza:     # проверка на все цифры
    for i in range(n):
        for j in range(n):
            sum1 = sum(matrix[0])      # сумма строк
    fl_stroki = True
    for c in range(1, n):
        if sum1 == sum(matrix[c]):
            fl_stroki = True
        else:
            fl_stroki = False
            break
    total = 0
    ls = []
    fl_stolb = True
    for i in range(len(matrix[0])):
        stolb = 0
        for j in range(len(matrix)):
            stolb += matrix[j][i]  # вывод суммы отдельного столбца
        ls.append(stolb)  # с занесением в одномерный массив
    x = ls[0]
    for c in range(1, len(ls)):
        if ls[0] == ls[c]:
            fl_stolb = True
        else:
            fl_stolb = False
            break
    fl_diag =True
    sum_diag = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                sum_diag = sum_diag + matrix[i][j]    # сумма диагоналей
    if sum_diag == sum1:
        fl_diag =  True
    else:
        fl_diag =  False
    if fl_stroki == True and fl_stolb == True and fl_diag == True:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
