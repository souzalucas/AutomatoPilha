import sys 

# class entrada ():

# class transicao ():

# class maquina ():

def lerArquivo (arquivo):
  arq = open(arquivo, 'r')
  conteudo = arq.readlines()
  # for linha in conteudo :
  #   linha = linha.split(' ')
  #   print (linha)
  alfaEntrada = conteudo[0].split()
  print(alfaEntrada)
  alfaPilha = conteudo[1].split()
  print(alfaPilha)
  conjEstados = conteudo[4].split()
  print(conjEstados)
  iniEstado = conteudo[5].split()
  print(iniEstado)
  arq.close()

lerArquivo(sys.argv[1])
  