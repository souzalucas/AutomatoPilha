import sys

class Pilha():

  def __init__(self, conteudo):
    self._conteudo = conteudo

  def isEmpty(self):
    return False if (len(self._conteudo)) else True

  def isTop(self, conteudo):
    length = len(conteudo)
    ## quantos caracteres irão ser comparados
    return (False) if (len(self._conteudo) < length) else (self._conteudo[0:length] == conteudo)
    ## retorna falso, se conteudo da pilha for menor que o conteudo comparado ou diferente dele
  ## desempilha valor antigo e empilha o novo independente de ser valor vazio
  def alterTop(self, old, new):
    if (self.isTop(old)):
      self._conteudo = self._conteudo.replace(old, new, 1)
    ## desempilha o valor antigo e empilha o novo valor no lugar

  def print(self):
    print(self._conteudo)
    ## exibe o conteudo da pilha

  pass

class Transicao():

  def __init__(self, transicao, estado, estados):
    data = transicao.split()
    self.estado = estado
    self.novoEstado = data[1]
    for state in estados:
      if(self.novoEstado == state.getCod()):
        self.novoEstado = state
        break
    self.valor = data[2]
    self.novoValor = data[3]

  pass

class Estado():
  ## inicializa o estado sem suas transições
  def __init__(self, cod, fStates):
    self.cod = cod
    self.isFinal = False
    for fS in fStates:
      if(fS == self.cod):
        self.isFinal = True
        break
    self.transicoes = []

  def getCod(self):
    return self.cod
  pass

class Maquina():

  pass

def lerArquivo (arquivo):
  arq = open(arquivo, 'r')
  conteudo = arq.read().split('\n')
  #print(conteudo)
  alfaEntrada = conteudo[0].split()
  #print(alfaEntrada)
  alfaPilha = conteudo[1].split()
  #print(alfaPilha)
  conjEstados = conteudo[4].split()
  #print(conjEstados)
  iniEstado = conteudo[5].split()
  #print(iniEstado)
  finEstados = conteudo[6].split()
  #print(finEstados)
  transicoes = conteudo[7:]
  #print(transicoes)
  arq.close()
  return [alfaEntrada, alfaPilha, conjEstados, iniEstado, finEstados, transicoes]

def main(arquivo, entrada):

  estrutura = lerArquivo(arquivo)
  print(estrutura[0])

  ## Testes da pilha
  pil = Pilha('ola mundo')

  print(pil.isTop(''))

  pil.alterTop('', '1')

  pil.print()

if __name__ == "__main__":
  if(len(sys.argv) != 3):
    print("Parametros insuficientes. Informe o nome do arquivo de entrada e a palavra de entrada")
    sys.exit(1)
  main(sys.argv[1], sys.argv[2])






### na transição 
  
#  def valida(self, fita, pilha):
#    if (fita.isTop(self.tapeContent)): ## valida a fita
#      ## esqueci de declarar o valor da fita na transição
#      if (pilha.isTop(self.valor)): ## valida a pilha
#        return True
#    ## retorna falso se a fita ou a pilha estiver invalida
#    return False

### na maquina 
#  def __init__(self, entrada, pilha, estado):
#    self.fita = Pilha(entrada)
#    self.pilha = Pilha(pilha)
#    self.estado = estado