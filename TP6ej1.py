################
# Mariela Carriqueo- @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def anagrama (texto1, texto2):
    """
    Esta función determina si dos cadenas son anagramas entre sí.
    """
    texto1 = str(input('Ingrese una palabra'))
    texto2 = str(input('Ingrese la palabra a comparar'))
    texto1_ord = sorted(texto1)
    texto2_ord = sorted(texto2)
    if texto1_ord == texto2_ord:
        return True
        print('Las palabras son anagramas entre sí')
    else:
        print('Las palabras no son anagramas entre sí')
    

if __name__ == "__main__":
    anagrama()
