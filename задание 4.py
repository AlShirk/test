
print("Введите Число")
A=int(input())
print("Ответ:")
def prostoe(x):
    c=2
    while x%c!=0:
        c+=1
    return x==c
if prostoe(A)==True:
    print("простое")
else:
    print("составное")

        

