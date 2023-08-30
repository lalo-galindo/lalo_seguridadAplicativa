sum = 0
min = None
max =None
best =[]
worst =[]

diccionario= {
    "Juan": 8,
    "Giselle": 9,
    "Damian": 5,
    "Ricardo": 6,
    "Yaotzin": 6,
    "Erick": 7,
    "Mario": 8,
    "Edgar": 9,
    "Fernanda": 5,
    "Daniel": 6,
    "Jesus": 7,
    "Damian": 8,
    "Yemahina": 6,
    "Eduardo": 9,
    "Bryan": 9,
    "Mariano": 10,
    "Alberto": 8,
}

for i in diccionario:
    sum += diccionario[i]

    if (min==None and max == None):
        min = diccionario[i]
        max = diccionario[i]
    elif(min>diccionario[i]):
        worst = [i]
        min = diccionario [i]
    elif (max<diccionario[i]):
        best =[i]
        max =diccionario[i]
    elif (min==diccionario[i]):
        worst.append(i)
    elif (max==diccionario[i]):
        best.append(i)

print ("El promedio es:",sum/len(diccionario))
print (worst, "sacó la peor calificación:",min)
print (best, "sacó la mejor calificación:",max)
