print("привет введите строку символов")
Строк=input()
print("введите символ поиска")
цело=input()


def аналог(a,b):
    count=0
    for i in range(len(a)):
        if a[i]==b:
            count=count+1   
    print("этот символ существует ",count,"раз(a) в",a)

аналог(Строк,цело)
