#5. Crie uma lista com os números divisíveis por 3 e 5 de 1 a 30.

lista_numeros_divisiveis = [numero for numero in range(1, 31) if numero % 3 == 0 or numero % 5 == 0]
print(lista_numeros_divisiveis)