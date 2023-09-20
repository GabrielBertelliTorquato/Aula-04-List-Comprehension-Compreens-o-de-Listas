# 10. Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de
# nomes, mas com as primeiras letras maiúsculas.

lista_de_nomes = ["joão", "maria", "pedro", "ana", "carlos", "lúcia", "josé", "rita", "mário", "teresa", "eduardo", "sofia"]
primeiros_10_nomes = lista_de_nomes[:10]

nomes_com_primeira_letra_maiuscula = [nome.capitalize() for nome in primeiros_10_nomes]
print(nomes_com_primeira_letra_maiuscula)

