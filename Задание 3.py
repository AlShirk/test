print("Введите Число")
A=int(input())
print("Ответ:")
chetnie=[]
nechetnie=[]
while A/10>0:
    if (A%10)%2==0:
        chetnie.append(A%10)
    if (A%10)%2!=0:
        nechetnie.append(A%10)
    A=A//10
print("Чётные:", chetnie)
print("Нечётные:", nechetnie)

