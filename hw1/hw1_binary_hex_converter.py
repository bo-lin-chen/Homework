number=int(input("Enter number in decimal "))
number2=number
#binary
binary=[0,0,0,0,0,0,0,0]
if number<256 and number>=0:
    for i in range(0,8):
        if number >= 2**(7-i) :
            binary[i]=1
            number=number-2**(7-i)
        else:
            binary[i]=0
    print("The binary is ")
    print(binary)
else:
    print("Please enter number between 0 to 255")
#hex
hex=[0,0]
hex_number=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
if number2<256 and number2>=0:
    for i in range(0,2):
        if number2 >= 16**(1-i) :
            for j in range(0,16):
                if (number2-(16**(1-i))*j)<16 and (number2-(16**(1-i))*j)>=0:
                    if i ==0:
                        number2=number2-(16**(1-i))*j
                        hex[i]=hex_number[j]
                    else:
                        hex[i]=hex_number[number2]
        else:
            hex[i]=0
    print("The Hexadecimal is ")
    print(hex)
else:
    print("Please enter number between 0 to 255")
#binary to hex
hex2=[0,0]
number3=0
number4=0
for k in range(0,7):
    if k < 4:
        number3=number3+2**(3-k)*binary[k]
        hex2[0]=hex_number[number3]
    elif k>3:
        number4=number4+2**(7-k)*binary[k]
        hex2[1]=hex_number[number4+1]
print(hex2)
