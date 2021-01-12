print("привет введите строку символов")
Строк=input()
print("введите число повторений")
цело=int(input())

def возвраща(a,b):
    data=''
    for i in range(b):
        data=data+a
    print("вот ваш ответ",data)

возвраща(Строк,цело)
