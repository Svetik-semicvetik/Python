# Задание 1 Сделать int такой, что 2+2=5
a = 1
class NewInt(int):
    def __add__(self,a):
        return super().__add__(a+1)

b = NewInt(2)
print(b+2)


# Задание 2 Сделать лист такой, что больше 10 нельзя
с = [1]
class NewList(list):
    def __init__(self,c):
        if len(c) > 10:
            raise ValueError('Лист содержит больше 10 элементов')
        else:
            super().__init__(c)
    def append(self,c):
        if len(self) == 10:
            raise ValueError('Лист содержит больше 10 элементов')
        else:
            super().append(c)

d = NewList([1,2,3,4,5,6,7,8,9,10])
print(d)
d.append(11)
print(d)


# Задание 3 Сделать уникальный список
class UniqueList(set):
    pass

e = UniqueList([4,3,6,3,4,3,2,1,2,6])
print(e)
