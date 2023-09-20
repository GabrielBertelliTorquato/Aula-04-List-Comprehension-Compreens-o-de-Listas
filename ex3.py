# 3. Crie uma lista com as letras maiúsculas de uma string qualquer.

def letras_maiusculas(string):
    maiusculas = [letra for letra in string if letra.isupper()]
    return maiusculas

string = 'Gabriel Bertelli Torquato'
lista_maiusculas = letras_maiusculas(string)

print(lista_maiusculas)



    
