texto = input('Digite a mensagem a ser encriptada ou decifrada: ')
chave = int(input('Entre com o valor da chave (deslocamento): '))
modo = input('Escolha E para encriptar ou D para decriptar o texto: ')
CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
convertido = ''
texto = texto.upper()
for letra in texto:
  if letra in CARACTERES:
    posicaoLetra = CARACTERES.find(letra)
    if modo == 'E':
      posicaoLetra = posicaoLetra + chave
    elif modo == 'D':
      posicaoLetra = posicaoLetra - chave
  if posicaoLetra >= len(CARACTERES):
    posicaoLetra = posicaoLetra - len(CARACTERES)
  elif posicaoLetra < 0:
    posicaoLetra = posicaoLetra + len(CARACTERES)

  convertido = convertido + CARACTERES[posicaoLetra]
if modo == 'E':
  print('O texto criptografado é ', convertido)
if modo == 'D':
  print('O texto decriptado é ', convertido)
