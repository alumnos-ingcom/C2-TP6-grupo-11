################
# Mariela Carriqueo- @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Codificador
"""
a1 = input('Ingrese nombre de archivo de entrada (con extensión .txt):')
a2 = input('Ingrese nombre de nuevo archivo codificad')
valor_rot = int(input('Ingrese valor de rotación: '))
try:
    f = open(a1,'r')
    f2 = open(a2,'r+')
except:
    print('El archivo no existe')
for linea in f:
    f2.write(linea)
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    codificacion = ''
    linea = linea.upper()
    largo_alfabeto = len(alfabeto)
    for letra in linea:
        valor_letra = ord(letra)
        rotacion = (valor_letra - 65 + valor_rot) % largo_alfabeto
        codificacion += alfabeto[rotacion]
        

f.close()
f2.close()
print(f2)

    

