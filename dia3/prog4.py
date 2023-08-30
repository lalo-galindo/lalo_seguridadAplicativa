def b_w(a):
    sum = 0
    min = None
    max =None
    best =[]
    worst =[]
    for i in a:
        sum += a[i]
        if (min==None and max == None):
            min = a[i]
            max = a[i]
        elif(min>a[i]):
            worst = [i]
            min = a [i]
        elif (max<a[i]):
            best =[i]
            max =a[i]
        elif (min==a[i]):
            worst.append(i)
        elif (max==a[i]):
            best.append(i)
    print ("El promedio es:",sum/len(a))
    print (worst, "sacó la peor calificación:",min)
    print (best, "sacó la mejor calificación:",max)

alumnos= {
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
b_w(alumnos)
