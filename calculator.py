import math
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
    if c=='sin':
        d=math.sin(math.radians(30))
def operations():
    print('addition(+)')
    print('subraction(-)')
    print('multiplication(*)')
    print('division(/)')    
a=int(input('enter the number: '))
operations()
c=input('chosse the operation you want to perform: ')
b=int(input('enter next number: '))
print(f"{a}{c}{b}={calculator(a,b,c)}")
d=input(f"enter 'y' to continue calculation with {calculator(a,b,c)} enter 'n' to start new calculation enter 'e' to exit: ").lower()
s=calculator(a,b,c)
while d!='e':
    if d=='y':
        operations()
        f=input('chosse the operation you want to perform: ')
        e=int(input('enter next number: '))
        print(f"{s}{f}{e}={calculator(s,e,f)}")
        d=input(f"enter 'y' to continue calculation with {calculator(s,e,f)} enter 'n' to start new calculation enter 'e' to exit: ").lower()
        s=calculator(s,e,f)
    if d=='n':
        a=int(input('enter the number: '))
        operations()
        c=input('chosse the operation you want to perform: ')
        b=int(input('enter next number: '))
        print(f"{a}{c}{b}={calculator(a,b,c)}")
        d=input(f"enter 'y' to continue calculation with {calculator(a,b,c)} enter 'n' to start new calculation enter 'e' to exit: ").lower()
if d=="e":
    print('thank you')         
    









    