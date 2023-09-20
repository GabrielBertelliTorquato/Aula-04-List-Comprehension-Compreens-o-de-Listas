# 6. Crie uma lista com as palavras de uma string que tenham mais de 3 letras.

def palavras_com_mais_de_3_letras(string):
    palavras = string.split()
    palavras_compridas = [palavra for palavra in palavras if len(palavra) > 3]
    return palavras_compridas

frase = 'Quando se olha muito para o abismo, o abismo olha de volta pra você'
palavras_compridas = palavras_com_mais_de_3_letras(frase)

print(palavras_compridas)
