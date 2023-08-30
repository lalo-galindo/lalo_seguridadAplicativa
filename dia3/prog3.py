a =[8,9,10,6,6,7,8,9,5,6,7,6,8,8,9,9,5,6,7,9,10,7,8,9,9]

def promedio(b): return sum(b)/len(b)

def reprobaron(b):
    reprobados=0
    for i in b:
        if i < 6: reprobados += 1
    return reprobados

print ("El promedio es:",promedio(a))
print ("Reprobados:",reprobaron(a))