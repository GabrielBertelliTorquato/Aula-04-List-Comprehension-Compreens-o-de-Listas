# 8. Crie uma lista com as datas de todos os dias de janeiro em um ano bissexto
# (considerando que um ano bissexto é divisível por 4).

ano_bissexto = 2024  
dias_de_janeiro = [f"{ano_bissexto}-01-{str(d).zfill(2)}" for d in range(1, 32)]
print(dias_de_janeiro)