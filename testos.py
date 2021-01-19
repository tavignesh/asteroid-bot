inp = int(input("Type 1 for HCF \nType 2 For LCM\n"))

if inp == 1:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))

    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if((num1 % i == 0) and (num2 % i == 0)):
            hcf = i
    print(hcf)

if inp == 2:
    aha1 = int(input("Enter a number"))
    aha2 = int(input("Enter a number"))

    if aha1 > aha2:
        gr = aha1
    else:
        gr = aha2
    while(True):
        if((gr % aha1 == 0) and (gr % aha2 == 0)):
            lcm = gr
            break
        gr += 1
    print(lcm)