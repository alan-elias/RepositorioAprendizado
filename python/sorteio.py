from random import sample

players = ['Insigne', 'Lukaku', 'Messi', 'Neymar' ,'Mbappe', 'Cristiano Ronaldo', 'Benzema'] #JOGADORES
list(set(players)) #DEIXANDO IMUTAVEL
pote1 = sample(players, 3) #ESCOLHENDO 3 PRA 1 TIME
list(set(pote1)) #DEIXANDO IMUTAVEL
pote2 = list(set(players)- set(pote1)) #RETIRANDO OS QUE NÃO FORAM SORTEADOS PARA O TIME 1

print(f'\033[1m{" JOGADORES ":=^50}\033[m')
print(f'\033[1;33m  TIME 1: {pote1} \033[m') #EXPORTANDO QUEM FOI SELECIONADO ANTES
print(f'\033[1;34m  TIME 2: {sample(pote2, 3)} \033[m') #SELECIONANDO E EXPORTANDO DE QUEM SOBROU
print(f'\033[1m{"":=^50}\033[m')