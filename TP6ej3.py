################
# Mariela Carriqueo- @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Este programa solicita al usuario un archivo de entrada y uno de salida para copiar
el contenido de un archivo en el otro.
"""
a1 = input('Ingrese nombre de archivo de entrada (con extensión .txt):')
a2 = input('Ingrese nombre de archivo de salida (con extensión. txt: ')
f = open(a1,'r')
f2 = open(a2,'w')
for line in f:
    f2.write(line)
f.close()
f2.close()
print('Se copió el contenido del segundo archivo en el primero')