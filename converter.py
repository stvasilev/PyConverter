def toBinary(num):
    print("\nIn binary: ")
    num = int(num)
    num = bin(num).replace("0b","")
    return num

def toOctal(num):
    print("\nIn octal: ")
    num = int(num)
    num = oct(num).replace("0o", "")
    return num

def toDecimal(num,nType):
    print("\nIn decimal: ")
    if(nType == "d"):
        return num
    elif(nType == "b"):
        return int(num, 2)

def toHex(num, nType):
    print("\nIn hexadecimal: ")
    if(nType == "b"):
        num = int(num, 2)
    else:
        num = int(num)
    num = hex(num).replace("0x", "")
    return num

def main():
    loop = True
    while(loop):
        number = input("\nEnter a decimal or binary number: ")
        print("\n")

        inputIncorrect = True
        while(inputIncorrect):
            numType = input("Specify type - decimal or binary (d/b): ")
            if(numType == "d" or numType == "b"):
                inputIncorrect = False
                break
            else:
                print("\nEnter a valid type!\n")

        inputIncorrect = True
        while(inputIncorrect):
            print("\n")
            command = input("Convert the number to binary, octal, decimal or hexadecimal? (b/o/d/h) : ")
            if(command != "b" and command != "o" and command != "d" and command != "h"):
                print("\n")
                print("Invalid input! ")
            else:
                inputIncorrect = False
                break

        if (command == "b"):
            print(toBinary(number))

        elif (command == "o"):
            print(toOctal(number))

        elif (command == "d"):
            print(toDecimal(number,numType))

        elif (command == "h"):
            print(toHex(number,numType))
        
        inputIncorrect = True
        while(inputIncorrect):
            again = input("\nConvert another number? (y/n) : ")
            if (again == "y"):
                inputIncorrect = False
                break
            elif (again == "n"):
                inputIncorrect = False
                loop = False
            else:
                print("\nIncorrect input!\n")

if __name__ == "__main__":
    main()