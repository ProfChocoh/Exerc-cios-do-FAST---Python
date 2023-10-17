def registro(votos):
    for i in range(5):
        nome = str(input('Olá! Digite seu nome para prosseguirmos com a votação: '))
        voto = str(input(f'{nome}, digite a letra correspondente ao seu personagem favorito do desenho The Simpsons dentre os dois seguintes: \n[B]art ou [H]omer? \nQualquer outra opção anulará seu voto.\n')).upper()
        votos.append(voto)
    
def apuracao(votos):
    bart = 0
    homer = 0
    nulos = 0

    for voto in votos:
        if voto == 'B':
            bart +=1
        elif voto == 'H':
            homer +=1
        else:
            nulos +=1

    if bart > homer:
        vencedor = "Bart"
        mais_votos = bart
        perdedor = "Homer"
        menos_votos = homer
    else:
        vencedor = "Homer"
        mais_votos = homer
        perdedor = "Bart"
        menos_votos = bart
    
    
    return (vencedor, mais_votos, perdedor, menos_votos, nulos)

votos = []
registro(votos)

vencedor, mais_votos, perdedor, menos_votos, nulos = apuracao(votos)

print(f"\nO candidato mais votado foi {vencedor} com {mais_votos}")
print(f"O candidato menos votado foi {perdedor} com {menos_votos}")
print(f"Voto(s) nulo(s) :{nulos} voto(s) nulo(s).")