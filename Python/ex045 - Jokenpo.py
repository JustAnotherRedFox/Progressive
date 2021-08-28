from random import choice
from time import sleep
user = str(input("Vamos jogar jokenpo? qual voce escolhe?\nPapel, Pedra ou Tesoura: ")).strip().lower()

jokenpo = ['pedra', 'papel', 'tesoura']
cpu = choice(jokenpo)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

if cpu == 'papel' :
  if user == 'papel' :
    msg = 'EMPATE!! ambos jogaram papel'
  elif user == 'pedra' :
    msg = 'jogador jogou pedra e cpu jogou papel,\n jogador perde :('
  elif user == 'tesoura' :
    msg = 'jogador jogou tesoura e cpu jogou papel,\n jogador GANHOU!! :)'
  else:
    msg = 'JOGADA INVALIDA'
elif cpu == 'tesoura' :
  if user == 'tesoura' :
    msg = 'EMPATE!! ambos jogaram tesoura'
  elif user == 'pedra' :
    msg = 'jogador jogou pedra e cpu jogou tesoura,\n jogador GANHOU!! ^-^'
  elif user == 'papel' :
    msg = 'jogador jogou papel e cpu jogou tesoura,\n jogador PERDEU (╯︵╰,)'
  else:
    msg = 'JOGADA INVALIDA'
elif cpu == 'pedra' :
  if user == 'pedra' :
    msg = 'EMPATE!! ambos jogaram pedra'
  elif user == 'papel' :
    msg = 'jogador jogou papel e cpu jogou pedra,\n jogador GANHOU!! ;)'
  elif user == 'tesoura' :
    msg = 'jogador jogou tesoura e cpu jogou pedra,\n jogador perdeu (╥_╥)'
  else:
    msg = 'JOGADA INVALIDA'

print('=-='*20)
print(msg)
print('=-='*20)
