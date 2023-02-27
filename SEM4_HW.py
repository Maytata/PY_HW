# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
n = int(input("Введите количество элеметов списка: "))
m = int(input("Введите количество элеметов списка 2: "))
lst = [randint(0, 10) for _ in range(n)]
lst2 = [randint(0, 10) for _ in range(m)]
print(lst)
print (lst2)
lst3 = lst + lst2
checked_nums_list = []
for i in lst3:
    if lst3.count(i) > 1 and i not in checked_nums_list:
        checked_nums_list.append(i)
print(sorted(checked_nums_list))

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

U=int(input('Ввеcти количество кустов:'))
listBerries=[]
for i in range(U):
    amount=int(input('Ввеcти количество ягод на кусте:'))
    listBerries.append(amount)
r=0
SumBer=0
maxsum=0
while r<(len(listBerries)-1):
    SumBer = listBerries[r-1] + listBerries[r] + listBerries[r+1]
    r=r+1
    if SumBer>maxsum:
        maxsum=SumBer
SumBer=listBerries[r-1] + listBerries[r] + listBerries[0]
if SumBer>maxsum:
    maxsum=SumBer
print(maxsum)
