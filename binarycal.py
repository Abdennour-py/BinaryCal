def Bincal():
    choice = input('(1) Binary To Dicimal (2) Dicimal To Binary (3) Text To Binary :')
    
    #Binary To Dicimal
    if choice == '1':
        binary = input('Enter Binary Number :')
        decimal = 0
        for digit in binary:
            decimal = decimal*2 + int(digit)
        print(decimal)
        
    #Dicimal To Binary 
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
 
    #Text To Binary 
    elif choice == '3':
        a_string = input('Enter Text :')
        a_byte_array = bytearray(a_string, "utf8")
        byte_list = []
        for byte in a_byte_array:
            binary_representation = bin(byte)
            byte_list.append(binary_representation)
        print(byte_list)
        

    else:
        print("Your Command Dose not Exist..? PLease Try Again !")
        Bincal()
Bincal()
