def method(a):
    even=0 
    odd=0
    for i in range(0,len(number)):
        if int(number[i])%2==0:
            even+=1

        elif int(number[i])%2==1:
            odd+=1
    print(even,"четных")
    print(odd,"нечетных")
number=input("Введите ваши числа:").split()
method(number)
