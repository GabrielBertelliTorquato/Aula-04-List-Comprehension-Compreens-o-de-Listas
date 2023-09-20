# 4. Crie uma lista com o comprimento de cada palavra em uma string.

def compriemnto_str(string):
    palavras = string.split()
    comprimento = [len(palavra) for palavra in palavras]
    return comprimento


frase = 'Quando se olha muito para o abismo, o abismo olho de volta pra você'
comprimentos = compriemnto_str(frase)


print(comprimentos)