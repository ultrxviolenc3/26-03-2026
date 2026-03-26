f=open("input.txt", "r")

data = f.read()

f.close()

num=data.split()

count=0

totsum=0

maximum=float(num[0])
minimum=float(num[0])

for i in num :
    x=float(i)
    count+=1
    totsum+=x

    if x > maximum:
      maximum=x

    if x < minimum:
       minimum=x


print("Сумма ",totsum)
print("Количество ",count)
print("Максимум ",maximum)
print("Минимум ",minimum)
print("Среднее арифметическое ",totsum/count)