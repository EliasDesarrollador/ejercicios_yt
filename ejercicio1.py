
# Resolver el siguiente  ejercicio
# Ejercicio 1

# 1. Definir una función max() que tome como argumento dos numeros y
#devuelva el mayor de ellos.
#(Es cierto que python tiene una función max() incorporada,
#pero hacerla nosotros mismos es un muy buen ejercicio.
def custom_max(n1: int ,n2: int):
    """Dado dos numeros de entrada retorna el maximo de ambos

    Args:
        n1 (int): primer numero a comparar
        n2 (int): segundo numero a comparar
    Returns:
        int: Mayor  de ambos
    """
    if n2 > n1:
        return n2
    else:
        n1

print(custom_max(7,4))
 