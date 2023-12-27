def calc():
    print("0.exit")
    a=input("=>")
    if a=="0":
        return req
    else:
        print(eval(a))
        return calc


print("Choose one of this:\n1.Calculate\n2.other\n3.coming soon")
req=int(input("=>"))
if req==1:
    print(calc())