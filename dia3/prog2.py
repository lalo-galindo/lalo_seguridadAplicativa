def suma (a,b): return a+b
def resta (a,b): return a-b
def mult (a,b): return a*b
def div (a,b): return a/b

def calcula (option,n1,n2):
    if option == 1: return suma(n1,n2)
    elif option == 2: return resta(n1,n2)
    elif option == 3: return mult (n1,n2)
    else: return div (n1,n2)

print ("Dame la opción")
option= int(input())

print ("Dame un número")
num1 = int (input())

print ("Dame otro número")
num2 = int (input())

print ("resultado:", calcula(option,num1,num2))

    



