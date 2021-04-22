def Number():
    choice = input('(1) Binary To Dicimal (2) Dicimal To Binary :')

    if choice == '1':
        binary = input('Enter Binary Number :')
        decimal = 0
        for digit in binary:
            decimal = decimal*2 + int(digit)
        print(decimal)
    
    elif choice == '2':
        n=int(input('Enter Dicimal Number : '))
        k=[]
        while (n>0):
            a=int(float(n%2))
            k.append(a)
            n=(n-a)/2
        k.append(0)
        string=""
        for j in k[::-1]:
            string=string+str(j)
        print(string)     

    else:
        print("Your Command Dose not Exist..? PLease Try Again !")
        Number()
Number()
