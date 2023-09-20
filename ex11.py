# 11. Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de
# nomes, mas sem as vogais.

def remover_vogais(nome):
    vogais = "aeiouAEIOU"
    return "".join([letra for letra in nome if letra not in vogais])

lista_de_nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Lúcia", "José", "Rita", "Mário", "Teresa", "Eduardo", "Sofia"]
primeiros_10_nomes = lista_de_nomes[:10]

nomes_sem_vogais = [remover_vogais(nome) for nome in primeiros_10_nomes]
print(nomes_sem_vogais)