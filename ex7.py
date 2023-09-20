# 7. Crie uma lista com os números primos de 1 a 20. Dica: use uma função para
# verificar se o número é primo ou não.

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

primos = [numero for numero in range(1, 21) if eh_primo(numero)]

print(primos)
