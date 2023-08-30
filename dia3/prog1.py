nombre = 'ana'

# for i in nombre[::-1]:
#     print (i,end ="")
normal = nombre[::1]
reverso = nombre[::-1]
if normal == reverso:
    print ("Palindromo")
else: 
    print ("No es palindromo")
