#88
#Faça programa que ajude um jogador da MEGA SENA a criar palpites. O programa irá perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import radint

lista = []
jogos = []

print ("-" * 30)
print ("        APOSTA MEGA SENA       ")
print ("-" * 30)

quant = int (input("Quer osretar quantos jogos?"))
tot = 1
while tot <= quant:
  cont = 0
  while True:
    num = randint (1, 60) 
    if num not in lista:
      lista.append(num)
      cont += 1
    if cont >= 6:
      break
  lista.sort()  
  jogos.append(lista[:])
  lista.clear()
  tot += 1 

print ("-=" * 3, f"SORTEANDO {quant} JOGOS", "-=" * 3) 
for i, l in enumerate (jogos): 
  print (f"Jogo {i+1}: {l}")  