import math
print("do you wanth to perform trignometric operations or basic math")
e=input("give A to enter trignometric calculator and B to enter basic math calculator: ").upper()
def calculator(a,b,c):
    if c=='+':
        d=a+b
        return d
    if c=='-':
        d=a-b
        return d
    if c=='*':
        d=a*b
        return d
    if c=='/':
        d=a/b
        return d
def operations():
    print('addition(+)')
    print('subraction(-)')
    print('multiplication(*)')
    print('division(/)')
def calculator_s(a,b):
    if a=='sin':
        c=math.sin(math.radians(b))
        return c
    if a=='cos':
        c=math.cos(math.radians(b))
        return c
    if a=='tan':
        c=math.tan(math.radians(b))
        return c
    if a=='sec':
        c=1/math.cos(math.radians(b))
        return c
    if a=='cosec':
        c=1/math.cos(math.radians(b))
        return c
    if a=='cot':
        c=1/math.tan(math.radians(b))
        return c      
def operations_s():
    print('sin')
    print('cos')
    print('tan')
    print('cosec')
    print('sec')
    print('cot')
while e!='c':
    if e=='B':
        a=float(input('enter the number: '))
        operations()
        c=input('chosse the operation you want to perform: ')
        b=float(input('enter next number: '))
        print(f"{a}{c}{b}={calculator(a,b,c)}")
        d=input(f"enter 'y' to continue calculation with {calculator(a,b,c)} enter 'n' to start new calculation enter 'e' to exit: ").lower()
        s=calculator(a,b,c)
        while d!='e':
            if d=='y':
                operations()
                f=input('chosse the operation you want to perform: ')
                e=float(input('enter next number: '))
                print(f"{s}{f}{e}={calculator(s,e,f)}")
                d=input(f"enter 'y' to continue calculation with {calculator(s,e,f)} enter 'n' to start new calculation enter 'e' to exit basic math calculator: ").lower()
                s=calculator(s,e,f)
            if d=='n':
                a=float(input('enter the number: '))
                operations()
                c=input('chosse the operation you want to perform: ')
                b=float(input('enter next number: '))
                print(f"{a}{c}{b}={calculator(a,b,c)}")
                d=input(f"enter 'y' to continue calculation with {calculator(a,b,c)} enter 'n' to start new calculation enter 'e' to exit basic amth calculator : ").lower()
        if d=="e":
            print('thank you') 
            break        
    if e=='A':
        operations_s()
        a=(input('enter the operation you want to perform: '))
        b=int(input('enter the angle: '))
        print(calculator_s(a,b))
    if e=='E':
        print('thank you')
        break
    e=input("give A to enter trignometric calculatir and B to enter basic math calculator and e to exit : ").upper()        










    