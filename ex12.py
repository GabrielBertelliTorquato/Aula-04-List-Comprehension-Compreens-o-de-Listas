# 12. Concatenar elementos de sub-listas em uma única lista


sub_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_concatenada = [elemento for sub_lista in sub_listas for elemento in sub_lista]
print(lista_concatenada)